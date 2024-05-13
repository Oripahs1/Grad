from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('goods/', views.GoodsPageView.as_view(), name='goods'),
]