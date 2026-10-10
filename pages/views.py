from django.views.generic import TemplateView

from products.models import Product


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_products'] = (
            Product.objects
            .filter(status=True)
            .order_by('-datetime_created', '-id')[:8]
        )
        context['newest_products'] = (
            Product.objects
            .filter(status=True)
            .order_by('-datetime_created', '-id')[:4]
        )
        return context


class AboutUsPageView(TemplateView):
    template_name = 'pages/aboutus.html'
