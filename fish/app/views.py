from django.shortcuts import render
from app.models import Photo, Detail, Category
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils.translation import ugettext_lazy as _


# Create your views here.
def index(request):
    page = request.GET.get("page", default=1)
    page_size = request.GET.get('page_size', 16)

    categories = Category.objects.filter(enabled=True).order_by("-views")
    paginator = Paginator(categories, page_size)
    try:
        categories = paginator.page(page)
    except PageNotAnInteger:
        categories = paginator.page(1)
    except EmptyPage:
        categories = paginator.page(paginator.num_pages)
    return render(request, f'index.html',
                  context={'categories': categories, 'page': page, 'page_size': page_size})


def photo(request):
    category_id = request.GET.get('category_id')
    photos = Photo.objects.filter(enabled=True)
    category_title = _('all category')
    page = request.GET.get("page", default=1)
    page_size = request.GET.get('page_size', 16)
    categories = Category.objects.filter(enabled=True)
    if category_id:
        photos = photos.filter(category=category_id)
        category = categories.filter(id=category_id).get()
        category_title = category.title
    paginator = Paginator(photos, page_size)
    try:
        photos = paginator.page(page)
    except PageNotAnInteger:
        photos = paginator.page(1)
    except EmptyPage:
        photos = paginator.page(paginator.num_pages)
    return render(request, 'photo.html',
                  context={'photos': photos, 'category_title': category_title, 'categories': categories,
                           'category_id': category_id})


def photo_detail(request):
    photo_id = request.GET.get('photo_id')
    page = request.GET.get("page", default=1)
    page_size = request.GET.get('page_size', 12)
    detail = Detail.objects.filter(photo__id=photo_id)
    paginator = Paginator(detail, page_size)
    photo = Photo.objects.get(id=photo_id)
    try:
        detail = paginator.page(page)
    except PageNotAnInteger:
        detail = paginator.page(1)
    except EmptyPage:
        detail = paginator.page(paginator.num_pages)
    return render(request, 'photo-detail.html',
                  context={'photo_details': detail, 'photo_id': photo_id, 'title': photo.title})
