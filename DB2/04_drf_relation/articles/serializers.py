from rest_framework import serializers
from .models import Article, Comment


class CommentSerializer(serializers.ModelSerializer):
    article = serializers.StringRelatedField(read_only=True)  #??
    class Meta:
        model = Comment
        fields = ('__all__')
        # read_only_fields = ('article',)  # 해당 필드 유효성 검사에서 제외


class ArticleListSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(read_only=True, many=True)
    # comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    # comment_count = Article.comment_set.count()
    comment_count = serializers.SerializerMethodField()
    class Meta:
        model = Article
        # fields = ('id', 'title', 'content', 'comment_set', 'comment_count', )
        # fields = ('id', 'title', 'content', 'comment_count', )
        fields = ('__all__')

    def get_comment_count(self, obj):
        return obj.comment_set.count()
    


    # def to_representation(self, instance):
    #     rep = super().to_representation(instance)
    #     rep['comments'] = rep.pop('comment_set')
    #     return rep

