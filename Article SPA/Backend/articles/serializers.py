from rest_framework import serializers
from .models import Article, User
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    #user = serializers.Field(source='user.email')
    
    class Meta:
        model = User # get_user_model()
        fields = '__all__'
        #lookup_field = 'username'

class ArticleSerializer(serializers.ModelSerializer):
    #author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    
    class Meta:
        model = Article
        fields = ('id','author', 'title', 'body', 'created_at', 'updated_at')
