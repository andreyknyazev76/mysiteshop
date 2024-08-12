from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Products
from blog.models import Post
from goods.utils import q_search
from goods.views import Paginator
from blog.views import Paginator




def index(request):

    blog = Post.objects.all().filter(status=1).order_by("created_on")
    page = request.GET.get('post', 1)
    paginator = Paginator(blog, 1)
    current_page_blog = paginator.page(int(page))
  

    goods = Products.objects.all().filter(status=1).order_by("created_at")
    page = request.GET.get('page', 1)
    paginator = Paginator(goods, 1)
    current_page_goods = paginator.page(int(page))


    context = {
        'blog' : current_page_blog , 
        "goods": current_page_goods,
       
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'About - О нас',
        'content': "О нас",
        'text_on_page': "Текст о том почему этот магазин такой классный, и какой хороший товар."
    }

    return render(request, 'main/about.html', context)

