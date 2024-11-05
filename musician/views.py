from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from rest_framework import viewsets

from .models import Musician
from .serializers import MusicianSerializer


class MusicianListView(ListView):
    model = Musician
    template_name = "catalog/musician_list.html"


class MusicianDetailView(DetailView):
    model = Musician
    template_name = "catalog/musician_detail.html"


class MusicianCreateView(CreateView):
    model = Musician
    fields = ["first_name", "last_name", "instrument", "age"]
    template_name = "catalog/musician_form.html"
    success_url = reverse_lazy("musician:musician_list")


class MusicianUpdateView(UpdateView):
    model = Musician
    fields = ["first_name", "last_name", "instrument", "age"]
    template_name = "catalog/musician_form.html"
    success_url = reverse_lazy("musician:musician_list")


class MusicianDeleteView(DeleteView):
    model = Musician
    template_name = "catalog/musician_confirm_delete.html"
    success_url = reverse_lazy("musician:musician_list")


class MusicianViewSet(viewsets.ModelViewSet):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer
