from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from .models import Article
from django.core import serializers
from .serializers import ArticleSerializer, CommentSerializer
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def article_list(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many = True)
    # print(serializer)
    return Response(serializer.data)


@api_view(['GET'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    serializer = ArticleSerializer(article)
    print(serializer.data['content'])
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def article_list_create(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    else:
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=status.HTTP_400_BAD_REQUEST):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
# @authentication_classes(['AllowAny'])
# @authentication_classes(['Is_Authenticated'])
def comment(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == "POST":
        serializer = CommentSerializer(data=request.data)
        # serializer.initial_data['article'] = article_pk
        if serializer.is_valid(raise_exception=status.HTTP_400_BAD_REQUEST):
            serializer.save(article = article)
            return Response(serializer.data, status=status.HTTP_201_CREATED)



#=======================================================================
def article_html(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/article.html', context)


def article_json_1(request):
    articles = Article.objects.all()
    articles_json = []

    for article in articles:
        articles_json.append(
            {
                'id':article.pk,
                'title':article.title,
                'content':article.content,
                'created_at':article.created_at,
                'updated_at':article.updated_at,
            }
        )
    return JsonResponse(articles_json, safe=False)

def article_json_2(request):
    articles = Article.objects.all()
    data = serializers.serialize('json', articles)
    return HttpResponse(data, content_type = 'application/json')

@api_view(['GET'])
def article_json_3(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many = True)
    return Response(serializer.data)
