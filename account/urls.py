from django.urls import path
from django.contrib.auth import views

from .views import (
    ArticleList, ArticleCreate,
    ArticleUpdate, ArticleDelete,
    Profile,
    #  Login, PasswordChange
)

app_name = 'account'

# urlpatterns = [
#     path('login/', Login.as_view(), name='login'),
#     path('logout/', views.LogoutView.as_view(), name='logout'),
#     path('password_change/', PasswordChange.as_view(), name='password_change'),
#     path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),

# ]

urlpatterns = [
    path('home/', ArticleList.as_view(), name='home'),
    path('article/create', ArticleCreate.as_view(), name='article-create'),
    path('article/update/<int:pk>/', ArticleUpdate.as_view(), name='article-update'),
    path('article/delete/<int:pk>/', ArticleDelete.as_view(), name='article-delete'),
    path('profie/', Profile.as_view(), name='profile'),
]


