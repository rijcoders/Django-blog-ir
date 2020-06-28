from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.ArticleList.as_view(), name='list'),
    # path('<slug:slug>/', views.detail, name='article-detail'),
    path('<slug:slug>/', views.ArticleDetail.as_view(), name='detail'),
    path('page/<int:page>/', views.ListView.as_view()),
    path('category/<slug:slug>/', views.CategoryList.as_view(), name='category'),
    path('category/<slug:slug>/page/<int:page>/', views.CategoryList.as_view(), name='category'),

    path('author/<slug:username>/', views.AuthorList.as_view(), name='author'),
    path('author/<slug:username>/page/<int:page>/', views.AuthorList.as_view(), name='author'),


]
                                                         