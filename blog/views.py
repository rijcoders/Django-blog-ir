from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView

from .models import Article, Category


class ArticleList(ListView):
    # model = Article
    queryset = Article.objects.published()
    paginate_by = 2
    template_name = 'blog/home.html'

    

class ArticleDetail(DetailView):
	def get_object(self):
		slug = self.kwargs.get('slug')
		return get_object_or_404(Article.objects.published(), slug=slug)


class CategoryList(ListView):
    model = Category
    paginate_by = 2
    template_name = 'blog/category_list.html'

    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.active(), slug=slug)
        return category.articles.published()

    def get_context_data(self, **kwargs):
        context = super(CategoryList, self).get_context_data(**kwargs)
        context["category"] = category
        return context
    



# def detail(request, slug):

#     context = {
#         'object':get_object_or_404(Article.objects.published(), slug=slug)
#     }

#     return render(request, 'blog/detail.html', context)