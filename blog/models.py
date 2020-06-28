from django.db import models
from django.utils import timezone
from django.utils.html import format_html
from django.utils.text import slugify
from django.urls import reverse
# from django.contrib.auth.models import User

from account.models import User
from extensions.utils import jalali_converter

STATUS_CHOICE = (
    ('d', 'پیش نویش'),
    ('p', 'منتشر شده'),
    ('i', 'در حال بررسی'),
    ('b', 'برگشت داده شده'),
)
class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')



class Article(models.Model):

    title = models.CharField(max_length=100,verbose_name='عنوان مقاله')
    author = models.ForeignKey(User, on_delete=models.SET_NULL,    null=True, verbose_name='نویسنده', related_name='articles'
    )
    slug = models.SlugField(max_length=100, blank=True, null=True, verbose_name='تدرس مقاله')
    category = models.ManyToManyField('Category', related_name='articles', verbose_name='دسته بندی')
    description = models.TextField(verbose_name='محتوا')
    thumbnail = models.ImageField(upload_to='images',verbose_name='تصویر مقاله')
    publish = models.DateTimeField(default=timezone.now, verbose_name='زمان انتشار')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_special = models.BooleanField(default=False,verbose_name='مقاله ویژه')
    status = models.CharField(max_length=1, choices=STATUS_CHOICE,verbose_name='وضعیت')

    objects = ArticleManager()

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقاله ها'
        ordering = ['-publish']

    def save(self,*args, **kwargs):
        if not self.slug and self.title:
            self.slug = slugify(self.title)
        super(Article,self).save(*args, **kwargs)

    def get_article_url(self):
        return reverse('blog:detail', kwargs={'slug':self.slug})

    def jpublish(self):
        return jalali_converter(self.publish)

    # def category_published(self):
    #     return self.category.filter(status=True)

    def thumbnail_tag(self):
        return format_html("<img width=100 height=75 style='border-radius: 5px;' src='{}'>".format(self.thumbnail.url))
    thumbnail_tag.short_description = "عکس"	



        

    def __str__(self):
        return self.title
    

class CategoryManager(models.Manager):
	def active(self):
		return self.filter(status=True)


class Category(models.Model):
    parent = models.ForeignKey('self', default=None, blank=True, null=True,on_delete=models.SET_NULL, related_name='children', verbose_name='زیر دسته')
    title = models.CharField(max_length=200, verbose_name='عنوان دسته')
    slug = models.SlugField(max_length=100,blank=True, null=True, verbose_name='ادرس دسته بندی')
    status = models.BooleanField(default=True, verbose_name='ایا نمایش داده شود؟')
    position = models.IntegerField(default=0, verbose_name=' پوزیشن')

    objects = CategoryManager()

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دستع بندی ها'
        ordering = ('parent__id','position',)
    
    def save(self,*args, **kwargs):
        if not self.slug and self.title:
            self.slug = slugify(self.title)
        super(Category,self).save(*args, **kwargs)
        
    def __str__(self):
        return self.title