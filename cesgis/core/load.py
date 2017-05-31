from django.contrib.gis.utils import LayerMapping
from .models import CesVistoria, CesFundiario, Cota, App

cesvistoria_mapping = {
    'codigo': 'CODIGO',
    'sign_cod': 'SIGN_COD',
    'cod_fazend': 'COD_FAZEND',
    'proprietar': 'PROPRIETAR',
    'situacao': 'SITUACAO',
    'acesso': 'ACESSO',
    'nome_infra': 'NOME_INFRA',
    'tipo_infra': 'TIPO_INFRA',
    'desc_infra': 'DESC_INFRA',
    'data_infra': 'DATA_INFRA',
    'hora_infra': 'HORA_INFRA',
    'flagrante': 'FLAGRANTE',
    'notificado': 'NOTIFICADO',
    'observacao': 'OBSERVACAO',
    'point_x': 'POINT_X',
    'point_y': 'POINT_Y',
    'geom': 'MULTIPOINT',
}

cesfundiario_mapping = {
    'processo': 'PROCESSO',
    'proprietar': 'PROPRIETAR',
    'cpf_cnpj': 'CPF_CNPJ',
    'munic_uf': 'MUNIC_UF',
    'end_prop': 'END_PROP',
    'telefone': 'TELEFONE',
    'tipo_imove': 'TIPO_IMOVE',
    'cert_sigef': 'CERT_SIGEF',
    'area_total': 'AREA_TOTAL',
    'lote': 'LOTE',
    'loc_geogra': 'LOC_GEOGRA',
    'geom': 'MULTIPOLYGON25D',
}

cota_mapping = {
    'layer': 'Layer',
    'area': 'area',
    'geom': 'MULTIPOLYGON25D',
}

app_mapping = {
    'layer': 'Layer',
    'geom': 'MULTIPOLYGON25D',
}

lm1 = LayerMapping(CesFundiario, 'data/ces_03_fundiario.shp', cesfundiario_mapping)
lm2 = LayerMapping(Cota, 'data/ces_02_cota.shp', cota_mapping)
lm3 = LayerMapping(App, 'data/ces_01_app.shp', app_mapping)
lm4 = LayerMapping(CesVistoria, 'data/ces_04_vistoria.shp', cesvistoria_mapping)
