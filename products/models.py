from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

from django.utils.translation import gettext_lazy as _
from django.utils import timezone
# from ckeditor.fields import RichTextField
# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(verbose_name=_('Product description'))
    price = models.PositiveIntegerField(default=0)
    status = models.BooleanField(default=True)
    cover = models.ImageField(verbose_name=_('Product image'), upload_to='product/product_cover/', blank=True)

    datetime_created = models.DateTimeField(default=timezone.now, verbose_name=_('Date time of Creation')) #vid 259
    datetime_modified = models.DateTimeField(auto_now_add=True)



    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])  #'product_detail', args=([self.id])

    def __str__(self):
        return self.title


class ActiveCommentsManager(models.Manager):  #vid 216
    def get_queryset(self):
        return super(self, ActiveCommentsManager).get_queryset().filter(active=True)


class Comment(models.Model):
    PRODUCT_STARS = [
        ('1', _('very bad')),
        ('2', _('bad')),
        ('3', _('normal')),
        ('4', _('good')),
        ('5', _('perfect')),
    ]

    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    product = models.ForeignKey("Product", on_delete=models.CASCADE, related_name='comments')

    text = models.TextField(verbose_name=_('comment text'))
    stars = models.CharField(max_length=10, choices=PRODUCT_STARS, verbose_name=_('rating!'))

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now_add=True)

    active = models.BooleanField(default=True)

    #Manager vid 216
    objects = models.Manager()
    active_comments_manager = ActiveCommentsManager()

    def __str__(self):
        return self.text

# class comments(models.Model):
#     user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
#     book = models.ForeignKey(books, on_delete=models.CASCADE, related_name='comments')

#     text = models.TextField()

#     recommend = models.BooleanField(default=True)
#     is_active = models.BooleanField(default=True)
#     datetime_created = models.DateField(auto_now_add=True)


#     def __str__(self):
#         return self.text
