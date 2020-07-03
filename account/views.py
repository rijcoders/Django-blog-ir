from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView, CreateView,
    UpdateView, DeleteView
     
)
from django.urls import reverse_lazy

from blog.models import Category, Article
from .mixins import (
    FieldMixin, FormValidMixin,
    AuthorAccessMixin

)


class ArticleList(LoginRequiredMixin, ListView):
    template_name = 'registration/home.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Article.objects.all()
        else:
            return Article.objects.filter(author=self.request.user)

class ArticleCreate(LoginRequiredMixin, FormValidMixin, FieldMixin,  CreateView):
    model = Article
    template_name = 'registration/article-create-update.html'

class ArticleUpdate(AuthorAccessMixin, FormValidMixin, FieldMixin, UpdateView):
    model = Article
    template_name = 'registration/article-create-update.html'

class ArticleDelete(DeleteView):
    model = Article
    template_name = 'registration/article_confirm_delete.html'
    success_url = reverse_lazy("account:home")
