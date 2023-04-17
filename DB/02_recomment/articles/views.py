from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment, Hashtag
from .forms import ArticleForm, CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    articles = Article.objects.all()
    tag_lst = Hashtag.objects.all()
    context = {
        'articles': articles,
        'tag_lst':tag_lst,
        }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    # comments = article.comment_set.all()  # 대댓글 없을 때
    # SELECT * from comment where parent is NULL;
    comments = article.comment_set.filter(parent__isnull = True)  # 댓글, 장고 문법사용
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            # Hash tag 저장
            for word in article.content.split():
                if word[0] == '#':
                    #word랑 같은 해시태그가 존재하면, 기존객체 반환, 없으면 새 객체 생성
                    hashtag, created = Hashtag.objects.get_or_create(content=word)
                    # [1] 현재 등록된 모든 해시태그 보기
                    # [2] 클릭 시 hashtag 기준으로 filter 해주기
                    # [3] 게시물 수정시, 새로 등록된 해시태그 검사
                    article.hashtags.add(hashtag)
                        

            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()

    context = {
        'form': form,
        }
    return render(request, 'articles/create.html', context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        article.delete()
        return redirect('articles:index')
    return redirect('articles:detail', article.pk)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, request.FILES, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', pk=article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:detail', article.pk)
    context = {'form': form, 'article': article}
    return render(request, 'articles/update.html', context)


def comments_create(request, pk):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    parent_pk = request.POST.get('parent_pk')

    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        # 얘가 댓글인지 대댓인지 확인
        if parent_pk:
            parent_comment = Comment.objects.get(pk=parent_pk)
            comment.parent = parent_comment

        comment.save()
    return redirect('articles:detail', article.pk)


def comments_delete(request, pk, comment_pk):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('articles:detail', pk)


# [2] 클릭 시 해시태그 기준으로 필터링
def hashtag_filtering(request, hash_pk):
    hashtag = get_object_or_404(Hashtag, pk=hash_pk)
    articles = hashtag.article_set.order_by('-pk')
    context = {
        'hashtag':hashtag,
        'articles':articles,
    }

    return render(request, 'articles/hashtag_filtering.html', context)