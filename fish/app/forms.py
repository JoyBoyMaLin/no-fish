from django import forms
from django.core.validators import validate_image_file_extension
from django.utils.translation import gettext as _

from app.models import Detail, Photo


class PhotoAdminForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('title', 'cover', 'enabled', 'category')

    photos = forms.FileField(
        widget=forms.ClearableFileInput(attrs={"multiple": True}),
        label=_("Add photos"),
        required=False,
    )

    def clean_photos(self):
        """Make sure only images can be uploaded."""
        for upload in self.files.getlist("photos"):
            validate_image_file_extension(upload)

    def save_photos(self, photo):
        """Process each uploaded image."""
        for upload in self.files.getlist("photos"):
            detail = Detail(photo=photo, image=upload)
            detail.save()
