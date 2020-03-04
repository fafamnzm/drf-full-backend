from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions, generics
# from django.contrib.auth.models import User

from .models import Article, User
from .serializers import ArticleSerializer, UserSerializer
from .permissions import IsAthourOrReadOnly

# Create your views here.

""" 
    Don't mind the comment parts
    They are just for demonstrating other ways to do things!!! =)
        """

# class ArticleList(generics.ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAthourOrReadOnly,)
    
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAthourOrReadOnly,)
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    def get_queryset(self):
        # if self.request.user.is_superuser:
        #     return Article.objects.all()
        # else:
        #     return Article.objects.filter(id=self.request.user.id)
        queryset = Article.objects.all()
        # username = self.request.query_params.get('username', None)
        # if username is not None:
        #     queryset = queryset.filter(author__username = username)
        return queryset

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
