from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Article, User
from .forms import UserChangeForm, UserCreationForm
# from django.contrib.auth import get_user_model

# Register your models here.
#User = get_user_model()
class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserCreationForm
    model = User
    list_display = ['email', 'username']


admin.site.register(User, UserAdmin)
admin.site.register(Article)