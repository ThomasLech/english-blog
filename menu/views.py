from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from models import Tiles, Menu


class IndexView(ListView):
    context_object_name = "menu_nodes"
    template_name = "index.html"
    model = Menu.objects.all()

    def get_queryset(self):
        return Menu.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['tile_nodes'] = Tiles.objects.all()
        return context


# class IndexView(ListView):
#     context_object_name = "kodes"
#     queryset = Tiles.objects.all()
#     template_name = "index.html"


class TilesView(ListView):
    context_object_name = "menu_nodes"
    template_name = "tiles.html"
    model = Menu.objects.all()

    def get_queryset(self):
        return Menu.objects.all()

    def get_context_data(self, **kwargs):
        context = super(TilesView, self).get_context_data(**kwargs)
        context['tile_nodes'] = Tiles.objects.all()
        return context


class TileDetailView(ListView):
    context_object_name = "nodes"
    queryset = Tiles.objects.all()
    template_name = "tile_detail.html"

    def get_object(self):
        return get_object_or_404(Tiles, pk=self.kwargs.get("pk"))

    def get_context_data(self, **kwargs):
        kwargs["objekt"] = Tiles.objects.get(id=self.kwargs.get("pk"))
        return super(TileDetailView, self).get_context_data(**kwargs)
