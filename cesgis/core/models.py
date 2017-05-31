from django.contrib.gis.db import models
from django.urls import reverse


class CesVistoria(models.Model):
    codigo = models.CharField('Código da Vistoria', max_length=50)
    sign_cod = models.CharField('Descrição do Código', max_length=50)
    cod_fazend = models.CharField('Código da Fazenda', max_length=50)
    proprietar = models.CharField('Nome Proprietário', max_length=100)
    situacao = models.CharField('Situação da Negociação', max_length=50)
    acesso = models.CharField('Tipo de Acesso', max_length=50)
    nome_infra = models.CharField('Nome do Infrator', max_length=50)
    tipo_infra = models.CharField('Tipo de Infração', max_length=50)
    desc_infra = models.CharField('Descrição da Infração', max_length=254)
    data_infra = models.CharField('Data da Infração', max_length=50)
    hora_infra = models.CharField('Hora da Infração', max_length=50)
    flagrante = models.CharField('Houve Flagrante?', max_length=50)
    notificado = models.CharField('Houve Notificação?', max_length=50)
    observacao = models.CharField('Observação', max_length=254)
    point_x = models.DecimalField('Coordenada E', max_digits=15, decimal_places=0)
    point_y = models.DecimalField('Coordenada N', max_digits=15, decimal_places=0)
    # modifiquei aqui
    geom = models.PointField(srid=4326)

    def __str__(self):
        return self.codigo

    class Meta:
        verbose_name = 'Infracão'
        verbose_name_plural = 'Infrações'
        ordering = ['codigo']

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])

    @property
    def popup_content(self):
        popup = "<strong>Código da Infração: </strong>{}<br>".format(self.codigo)
        popup += "<strong>Código da Fazenda: </strong>{}<br>".format(self.cod_fazend)
        popup += "<strong>Nome do Infrator: </strong>{}<br>".format(self.nome_infra)
        popup += "<strong>Tipo de Infração: </strong>{}<br>".format(self.tipo_infra)
        popup += "<strong>Descrição da Infração: </strong>{}<br>".format(self.desc_infra)
        popup += "<strong>Data da Infração: </strong>{}<br>".format(self.data_infra)
        popup += "<strong>Houve Flagrante?: </strong>{}<br>".format(self.flagrante)
        popup += "<strong>Houve Notificaçao?: </strong>{}<br>".format(self.notificado)
        popup += "<strong><a href={}>Informações Adicionais</a></strong>".format(self.get_absolute_url())
        return popup


class CesFundiario(models.Model):
    processo = models.CharField('Número do Processo', max_length=50)
    proprietar = models.CharField('Nome do Proprietário', max_length=50)
    cpf_cnpj = models.CharField('CPF', max_length=50)
    munic_uf = models.CharField('Município da Residência', max_length=50)
    end_prop = models.CharField('Endereço da Residência', max_length=100)
    telefone = models.CharField('Telefone', max_length=50)
    tipo_imove = models.CharField('Tipo de Imóvel', max_length=20)
    cert_sigef = models.CharField('Certificado pelo SIGEF?', max_length=10)
    area_total = models.DecimalField('Área do Imóvel', max_digits=10, decimal_places=4)
    lote = models.CharField('Lote', max_length=15)
    loc_geogra = models.CharField('Município Localizado', max_length=50)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.processo

    class Meta:
        verbose_name = 'Informação Fundiária (CES)'
        verbose_name_plural = 'Informações Fundiária (CES)'
        ordering = ['processo']


class Cota(models.Model):
    layer = models.CharField('Nome', max_length=254)
    area = models.DecimalField('Área', max_digits=10, decimal_places=4)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.layer

    class Meta:
        verbose_name = 'Cota de Nível'
        verbose_name_plural = 'Cotas de Nível'
        ordering = ['layer']


class App(models.Model):
    layer = models.CharField('Nome', max_length=254)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.layer

    class Meta:
        verbose_name = 'APP'
        verbose_name_plural = 'APP'
        ordering = ['layer']
