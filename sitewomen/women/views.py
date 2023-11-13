from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render

from women.forms import AddPostForm, UploadFileForm

from .models import Category, TagPost, UploadFiles, Women

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
    posts = Women.published.all().select_related("cat")
    data = {
        "menu": menu,
        "posts": posts,
        "cat_selected": 0,
    }

    return render(request, "women/index.html", data)


def about(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            fp = UploadFiles(file=form.cleaned_data['file'])
            fp.save()
    else:
        form = UploadFileForm()
    return render(request, 'women/about.html',
                  {'title': 'О сайте', 'menu': menu, 'form': form})



def add_page(request):
    if request.method == "POST":
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            # print(form.cleaned_data)
            # print('hello')
            # try:
            #     Women.objects.create(**form.cleaned_data)
            #     return redirect("home")
            # except:
            #     form.add_error(None, "Ошибка добавления поста")
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    data = {"menu": menu, "title": "ADD PAGE", "form": form}
    return render(request, "women/addpage.html", data)


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
    return render(request, "women/post.html", data)


def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Women.published.filter(cat_id=category.pk).select_related("cat")
    data = {
        "title": f"Рубрика {category.name}",
        "menu": menu,
        "posts": posts,
        "cat_selected": category.pk,
    }

    return render(request, "women/index.html", context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>ERRRRRRRRRRRRRRRRRRORRRR</h1>")


def show_tag(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = tag.tags.filter(is_published=Women.Status.PUBLISHED).select_related("cat")
    data = {
        "title": f"tag {tag.tag}",
        "menu": menu,
        "posts": posts,
        "cat_selected": None,
    }
    return render(request, "women/index.html", data)
