from django import forms
from django.utils import timezone

from django.db import models
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    title = models.CharField(_('title'), max_length=255)
    cover = models.ImageField(_('cover'), upload_to='static/uploads/images/photos/', null=False, blank=False)
    enabled = models.BooleanField(_('enabled'), default=True)
    views = models.BigIntegerField(default=0)
    created = models.DateField(_('created'), default=timezone.now)

    def cover_data(self):
        return format_html(
            '<img src="{}" width="100px"/>',
            self.cover.url,
        )

    cover_data.short_description = _('cover')

    def __str__(self):
        return self.title


class Photo(models.Model):
    class Meta:
        verbose_name = _('photo')
        verbose_name_plural = _('photos')

    title = models.CharField(_('title'), max_length=255)
    cover = models.ImageField(_('cover'), upload_to='static/uploads/images/photos/', null=False, blank=False)
    enabled = models.BooleanField(_('enabled'), default=True)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title


class Slider(models.Model):
    class Meta:
        verbose_name = _('slider')
        verbose_name_plural = _('sliders')

    title = models.CharField(_('title'), max_length=255)
    image = models.ImageField(_('image'), upload_to='static/uploads/images/photos/', null=False, blank=False)
    url = models.URLField(_('url'), null=False)
    enabled = models.BooleanField(_('enabled'), default=True)

    def __str__(self):
        return self.title


class Detail(models.Model):
    class Meta:
        verbose_name = _('detail')
        verbose_name_plural = _('details')

    photo = models.ForeignKey(Photo, default=None, on_delete=models.CASCADE)
    image = models.ImageField(_('image'), upload_to='static/uploads/images/photos/', null=True, blank=True)

    def __str__(self):
        return self.photo.title
