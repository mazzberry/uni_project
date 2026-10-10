from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name = 'home'),
    path('aboutUs', views.AboutUsPageView.as_view(), name = 'about-us'),

]