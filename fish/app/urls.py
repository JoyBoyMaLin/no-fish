from django.urls import path, include
from django.views.generic import RedirectView

from app.views import index, photo_detail, photo

urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url=r'static/img/favicon.ico')),
    path('', index, name='index'),
    path('index.html', index, name='index'),
    path('photo.html', photo, name='photo'),
    path('photo-detail.html', photo_detail, name='photo detail'),
    # path('<path:page>', views)
]
