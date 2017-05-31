function onEachFeature(feature, layer) {
    if (feature.properties && feature.properties.popup_content) {
        layer.bindPopup(
            feature.properties.popup_content
        );
    }
}

var dataurl = "{% url 'infracoes-geojson' %}";

// estilo para o mapa geral (webgis)
// mude depois de acordo com o seu estilo.
var style_all = {
    radius: 5,
    fillColor: "red",
    color: "black",
    weight: 1,
    opacity: 1,
    fillOpacity: 0.8
};

// estilo da feicao selecionada:
// mude depois de acordo com o seu estilo.
var style_selected = {
    radius: 10,
    fillColor: "yellow",
    color: "yellow",
    weight: 1,
    opacity: 1,
    fillOpacity: 0.7
};

var infracoes = L.geoJson([], {
    style: style_all,
    pointToLayer: function (feature, latlng) {
        return new L.CircleMarker(latlng);
    },
    onEachFeature: onEachFeature
});

$.getJSON(dataurl, function (data) {
    infracoes.addData(data);
});

// Descomentar no seu:
// var geoserver_url = "http://localhost:8080/geoserver/cesgis/wms";
//
// var fundiario = L.tileLayer.wms(geoserver_url, {
//     layers: 'cesgis:core_cesfundiario',
//     format: 'image/png',
//     transparent: true,
//     attribution: "WebGIS GeoGIS &copy;"
// });
//
// var cota = L.tileLayer.wms(geoserver_url, {
//     layers: 'cesgis:core_cota',
//     format: 'image/png',
//     transparent: true,
//     attribution: "WebGIS GeoGIS &copy;"
// });
//
// var app = L.tileLayer.wms(geoserver_url, {
//     layers: 'cesgis:core_app',
//     format: 'image/png',
//     transparent: true,
//     attribution: "WebGIS GeoGIS &copy;"
// });
//
// var vistoria = L.tileLayer.wms(geoserver_url, {
//     layers: 'cesgis:core_cesvistoria',
//     format: 'image/png',
//     transparent: true,
//     attribution: "WebGIS GeoGIS &copy;"
// });

var mbAttr = 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
        '<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
        'Imagery © <a href="http://mapbox.com">Mapbox</a>',
    mbUrl = 'https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw';

var grayscale = L.tileLayer(mbUrl, {id: 'mapbox.light', attribution: mbAttr}),
    streets = L.tileLayer(mbUrl, {id: 'mapbox.streets', attribution: mbAttr});

// config. iniciais se o mapa não estiver no detail:
var div_id = 'map';
var y_cen = -11.5769;
var x_cen = -55.6004;
var zoom_init = 10;
var infracao_selecionada = '';

// verifico se existe o detail:
var infracao = '{{ infracao }}';

// se estiver em detail, entro aqui:
if (infracao) {
    div_id = 'map-detail';
    y_cen = '{{ infracao.geom.y|safe }}';
    x_cen = '{{ infracao.geom.x|safe }}';
    zoom_init = 18;
    infracao_selecionada = L.geoJson(JSON.parse('{{ infracao.geom.json|safe }}'), {
        pointToLayer: function (feature, latlng) {
            return L.circleMarker(latlng, style_selected);
        }
    });
}

// aqui eu carrego ou as config. iniciais
// ou o do mapa detail:

var layers = [streets, infracoes];

var overlays = {
    // "Fundiário - CES": fundiario,
    // "Cota 302 m - Reservatório": cota,
    // "APP do Reservatório": app,
    // "Monitoramento Patrimonial": vistoria,
    "Infrações": infracoes,
};

// se estiver no mapa de detalhe,
// adicione a infração selecionada no mapa e no overlay
if (infracao_selecionada) {
    overlays["Infração Selecionada"] = infracao_selecionada;
    layers.push(infracao_selecionada);
}

var map = L.map(div_id, {
    center: [y_cen, x_cen],
    zoom: zoom_init,
    layers: layers
});

var baseLayers = {
    "Grayscale": grayscale,
    "Streets": streets
};

L.control.layers(baseLayers, overlays).addTo(map);

