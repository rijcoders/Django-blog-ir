from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.ArticleList.as_view(), name='list'),
    # path('<slug:slug>/', views.detail, name='article-detail'),
    path('<slug:slug>/', views.ArticleDetail.as_view(), name='article-detail'),
    path('page/<int:page>/', views.ListView.as_view()),
    path('category/<slug:slug>/', views.CategoryList.as_view(), name='category-list'),
    path('category/<slug:slug>/page/<int:page>/', views.CategoryList.as_view(), name='category-list'),


]
                                                         