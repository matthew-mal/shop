from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='list_of_products'),
    path('<slug:category_slug>/', views.product_list, name='list_of_products'),
    path('<int:pr_id>/<slug:product_slug>/', views.product_detail, name='product_detail')
]

