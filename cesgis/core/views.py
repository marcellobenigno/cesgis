from django.contrib.gis.geos import GEOSGeometry
from django.shortcuts import render
from djgeojson.views import GeoJSONLayerView

from .models import CesVistoria


def home(request):
    return render(request, 'index.html')


def webgis(request):
    return render(request, 'webgis.html')


def search(request):
    ces_vistoria_list = CesVistoria.objects.all()
    context = {
        'ces_vistorias': ces_vistoria_list
    }
    return render(request, 'search.html', context)


def search_lnglat(request, lng, lat):
    point = GEOSGeometry('POINT({} {})'.format(lng, lat))
    infracao = CesVistoria.objects.filter(geom__contains=point).first()
    context = {
        'infracao': infracao,
    }
    return render(request, 'search_lnglat.html', context)


def detail(request, pk):
    ces_vistoria = CesVistoria.objects.get(pk=pk)
    context = {
        # mudei aqui
        'infracao': ces_vistoria,
    }
    return render(request, 'detail.html', context)


class InfracaoGeoJson(GeoJSONLayerView):
    model = CesVistoria
    properties = ('propriedade', 'popup_content',)


infracao_geojson = InfracaoGeoJson.as_view()
