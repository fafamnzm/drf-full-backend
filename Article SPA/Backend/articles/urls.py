from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import  UserViewSet, ArticleViewSet #, ArticleList, ArticleDetail

# urlpatterns = [
#     path('<int:pk>/', ArticleDetail.as_view()),
#     path('', ArticleList.as_view()),
# ]

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', ArticleViewSet, basename='articles')

urlpatterns = router.urls
