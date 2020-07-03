from django.http import Http404


class FieldMixin():
    def dispatch(self, request, *args, **kwargs):

        if self.request.user.is_superuser:
            self.fields = [
            'title','author','slug',
            'category','description','thumbnail',
            'publish','is_special','status'
        ]
        elif self.request.user.is_author:
            self.fields = [
                'title','slug',
                'category','description','thumbnail',
                'publish','is_special',
            ]
        else:
            raise Http404("You cant access this page.")

        return super().dispatch(request, *args, **kwargs)


class FormValidMixin:
    def form_valid(self, form):
        if self.request.user.is_superuser:
            form.save()
        else:
            self.obj = form.save(commit=False)
            self.obj.author = self.request.user
            self.obj.status = 'd'

        return super().form_valid(form)

from django.shortcuts import get_object_or_404
from blog.models import Article, Category

class AuthorAccessMixin:
    def dispatch(self, request, pk, *args, **kwargs):
        article = get_object_or_404(Article, pk=pk)
        if article.author == request.user or request.user.is_superuser and article.status == 'd':
            return super().dispatch(request, pk, kwargs)
        else:
            raise Http404("You dont have permission to access this page.")


class SuperUserAccessMixin:
    def dispatch(self, request, pk, *args, **kwargs):
        if request.is_superuser:
            return super().dispatch(request, pk)
        else:
            raise Http404("You dont have permission to access this page.")