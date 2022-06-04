from django.shortcuts import render
from django.views.generic import CreateView, ListView
from photopostapp.models import PhotoUpload
from photopostapp.forms import ImageForm
from django.urls import reverse_lazy


# Create your views here.
class PhotoAddView(CreateView):
    model = PhotoUpload
    form_class = ImageForm
    template_name = "add_image.html"
    success_url = reverse_lazy("image list")


class ImageHome(ListView):
    model = PhotoUpload
    template_name = "image_home.html"
    context_object_name = "images"
