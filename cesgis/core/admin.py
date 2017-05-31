from django.contrib.admin import AdminSite
from django.contrib.gis import admin
from django.forms.widgets import Textarea
from .models import *


class CesFundiarioAdmin(admin.OSMGeoAdmin):
    model = CesFundiario
    list_display = ['processo', 'proprietar', 'cpf_cnpj', 'tipo_imove', 'lote', 'area_total']
    search_fields = ['processo', 'proprietar', 'cpf_cnpj', 'tipo_imove', 'lote', 'area_total']


admin.site.register(CesFundiario, CesFundiarioAdmin)


class CotaAdmin(admin.OSMGeoAdmin):
    model = Cota
    list_display = ['layer']
    search_fields = ['layer']


admin.site.register(Cota, CotaAdmin)


class CesVistoriaAdmin(admin.ModelAdmin):
    model = CesVistoria
    list_display = ['codigo', 'cod_fazend', 'proprietar', 'situacao', 'nome_infra', 'tipo_infra', 'notificado']
    search_fields = ['codigo', 'cod_fazend', 'proprietar', 'situacao', 'nome_infra', 'tipo_infra', 'notificado']

    formfield_overrides = {
        models.PointField: {'widget': Textarea}
    }


admin.site.register(CesVistoria, CesVistoriaAdmin)


class MyAdminSite(AdminSite):
    AdminSite.site_header = "GeoGIS Web - Painel de Controle da Companhia Energética de Sinop"
    AdminSite.index_title = "CES - Administração do Sistema"
