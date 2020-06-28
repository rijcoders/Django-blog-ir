from django.urls import path
from django.contrib.auth import views

from .views import (
    ArticleList
)

app_name = 'account'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),

]

urlpatterns += [
    path('home/', ArticleList.as_view(), name='home'),
     
]


