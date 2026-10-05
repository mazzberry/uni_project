from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, resolve_url
from .models import Product, Comment
from django.views import generic
from .forms import CommentForm
from django.contrib.auth import mixins
from django.urls import reverse

# from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _
from django.contrib import messages

from cart.forms import AddToCartProductForm

PRODUCTS_PER_PAGE = 1


def test_translation(request):
    result = _('hello world')
    messages.success(request, "this's success message.")
    messages.warning(request, "this is a warn to u.")
    messages.error(request, "this is a error to u.")

    return render(request, 'products/test_hello.html')

class ProductListView(generic.ListView):
    # model = Product #agar too in halat bashe yani : Products.objects.all()
    queryset = Product.objects.filter(status=True).order_by('-datetime_created', '-id') #migim ke tanha tooye chizayi ke mikaym query bezan va namayesh bede na hamash

    template_name = 'products/product_list.html'
    context_object_name = 'products'

    paginate_by = PRODUCTS_PER_PAGE

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        page_obj = context['page_obj']
        context['page_numbers'] = page_obj.paginator.get_elided_page_range(page_obj.number)
        return context


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
    
    def get_context_data(self, **kwargs: Any):#in method ro overwrite mikonim ta context ezafi be class based view bedim
        context = super().get_context_data(**kwargs) #mikhaym bere tooye context forme moon ta dar safe detail dade ro daryaft konim
        context['comment_form'] = CommentForm
        # context['add_to_cart_form'] = AddToCartProductForm() vid 245
        return context
    
    
class CommentCreateView(generic.CreateView, mixins.LoginRequiredMixin): # vid 214 vajeb be moroor
    modle = Comment
    form_class = CommentForm #form_class
    
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user # vid 214 / 215 vajeb be moroor
        
        product_id = int(self.kwargs['product_id'])
        product = get_object_or_404(Product, id=product_id)  # vid  214 / 215 vajeb be moroor
        
        obj.product= product

        messages.success(self.request, _('Your comment has been added.'))
        
        return super().form_valid(form)

    def get_success_url(self):
        product_id = self.kwargs['product_id']
        return reverse('product_detail', kwargs={'pk': product_id})
    
    # def get_success_url(self):
    #     return reverse('product_list')

