from rest_framework import serializers
from .models import Article, Comment

class CommentSerializer(serializers.ModelSerializer):
    article = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
        # fields = ('content', 'ac')



class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many = True, read_only=True)
    # cnt = serializers.IntegerField(read_only=True, )
    class Meta:
        model = Article
        fields = (
            'id', 
            'title', 
            'content',
            'comment_set',
            # 'cnt',
            )
