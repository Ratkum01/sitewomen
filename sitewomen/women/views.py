from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render

from .models import Category, TagPost, Women

# Create your views here.

menu = [
    {"title": "About", "url_name": "about"},
    {"title": "Add Page", "url_name": "add_page"},
    {"title": "Contact", "url_name": "contact"},
    {"title": "Login", "url_name": "login"},
]
data_db = [
    {"id": 1, "title": "Anjela", "content": "Bio Anjela Joli", "is_published": True},
    {"id": 2, "title": "Anjela", "content": "Bio Anjela Joli", "is_published": False},
    {"id": 3, "title": "Anjela", "content": "Bio Anjela Joli", "is_published": True},
]
cats_db = [
    {
        "id": 1,
        "name": "Актрисы",
    },
    {
        "id": 2,
        "name": "Певицы",
    },
    {
        "id": 3,
        "name": "Спортсменки",
    },
]


def index(request):
    posts= Women.published.all()
    data = {
        "menu": menu,
        "posts": posts,
        "cat_selected": 0,
    }

    return render(request, "women/index.html", data)


def about(request):
    data = {"menu": menu, "posts": data_db}
    return render(request, "women/about.html", data)


def add_page(request):
    return HttpResponse("Add Page")


def contact(request):
    return HttpResponse("contact contact")


def login(request):
    return HttpResponse("login login")


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)
    
    data = {
        "title": post.title,
        "menu": menu,
        "post": post,
        "cat_selected": 1,
    }
    return render(request, 'women/post.html', data)


def show_category(request, cat_slug):
    category= get_object_or_404(Category,slug= cat_slug)
    posts= Women.published.filter(cat_id= category.pk)
    data = {
        'title': f'Рубрика {category.name}',
        'menu':menu,
        'posts':posts,
        'cat_selected': category.pk
    }
    
    return render(request, "women/index.html", context=data)
    


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>ERRRRRRRRRRRRRRRRRRORRRR</h1>")

def show_tag(request, tag_slug):
    tag= get_object_or_404(TagPost, slug=tag_slug)
    posts= tag.tags.filter(is_published= Women.Status.PUBLISHED)
    data={
        'title': f'tag {tag.tag}',
        'menu':menu,
        'posts':posts,
        'cat_selected':None
    }
    return render (request, 'women/index.html', data)

