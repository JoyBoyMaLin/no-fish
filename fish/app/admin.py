from django.contrib import admin

from app.forms import PhotoAdminForm
from app.models import Detail, Photo, Category


class DetailInline(admin.StackedInline):
    model = Detail
    extra = 0
    fk_name = 'photo'


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    inlines = [DetailInline]
    form = PhotoAdminForm

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        form.save_photos(form.instance)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['title', 'cover', 'enabled']
    list_display = ['title', 'cover_data', 'enabled', 'views']
