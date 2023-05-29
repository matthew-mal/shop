from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForms
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Category, Product


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    product = Product.objects.filter(available=True)

    # Количество элементов на странице
    items_per_page = 15

    # Получение значения параметра "q" из запроса (поисковый запрос)
    search_query = request.GET.get('q')
    if search_query:
        # Если есть поисковый запрос, фильтруем продукты по запросу
        product = product.filter(name__icontains=search_query)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        product = Product.objects.filter(category=category)

    # Создание объекта Paginator
    paginator = Paginator(product, items_per_page)

    # Получение номера запрошенной страницы из параметров запроса (если указан)
    page_number = request.GET.get('page')

    try:
        # Получение объекта Page для запрошенной страницы
        page = paginator.get_page(page_number)
    except PageNotAnInteger:
        # Если параметр page не является целым числом, показать первую страницу
        page = paginator.get_page(1)
    except EmptyPage:
        # Если номер страницы выходит за пределы допустимого диапазона, показать последнюю страницу
        page = paginator.get_page(paginator.num_pages)
    return render(request, 'list_of_products.html',
                  {'categories': categories, 'product': page, 'category': category, 'page': page})


def product_detail(request, pr_id, product_slug):
    products = get_object_or_404(Product, id=pr_id, slug=product_slug)
    cart_product_form = CartAddProductForms()
    category = products.category
    return render(request, 'product_detail.html',
                  {'products': products, 'cart_product_form': cart_product_form, 'category': category})
