from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list'),
    path('<int:pr_id>/<slug:product_slug>/', views.product_detail, name='product_detail')
]

