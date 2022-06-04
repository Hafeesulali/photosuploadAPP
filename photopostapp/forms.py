from django import forms
from photopostapp.models import PhotoUpload


class ImageForm(forms.ModelForm):
    class Meta:
        model = PhotoUpload
        fields = ["image",
                  "caption",
                  "author_name"
                  ]
        widgets = {
            "image": forms.FileInput(attrs={"class": "form-control"}),
            "caption": forms.TextInput(attrs={"class": "form-control"}),
            "author_name": forms.TextInput(attrs={"class": "form-control"})

        }
