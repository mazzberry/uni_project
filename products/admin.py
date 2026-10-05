from django.contrib import admin
from .models import Product, Comment

from jalali_date.admin import ModelAdminJalaliMixin
class CommentsInline(admin.TabularInline):# be jay tabularInline mitavan az stackedInline ham estefade kard
    model = Comment
    fields = ['author', 'product', 'text', 'stars', 'active', ]
    extra = 1



# Register your models here.
@admin.register(Product)
class ProductAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = [
        # 'name',
        # 'price',
        # 'stock',
        # 'image_url',
        'title',
        'price',
        'status',
        'id'
    ]
    
    
    inlines = [
        CommentsInline,
    ]
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'product', 'text', 'stars', 'active', 'datetime_created']