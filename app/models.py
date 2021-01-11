from django.db import models

class Proprietario(models.Model):
    class Genero(models.TextChoices):
        MASCULINO = 'M'
        FEMININO = 'F'
    
    cpf =   models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    logradouro = models.CharField(max_length=50)
    numero = models.IntegerField()
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)
    cep = models.IntegerField(default=0)
    complemento = models.CharField(max_length=200)
    sexo = models.CharField(
        max_length=2,
        choices=Genero.choices,
        default=Genero.MASCULINO,
    )
    dataNascimento = models.DateField()

    

class Telefone(models.Model):
    class Meta:
        unique_together = [['proprietario', 'telefone']]
    proprietario = models.ForeignKey(
        Proprietario,
        on_delete=models.CASCADE,
        related_name="telefones")
    telefone = models.IntegerField()


class Categoria(models.Model):
    codigo = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=30, blank=True)


class Modelo(models.Model):
    codigo = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=30, blank=True)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name="modelos")


class Veiculo(models.Model):
    placa = models.CharField(primary_key=True, max_length=8)
    chassi = models.CharField(max_length=8, unique=True)
    cor = models.CharField(max_length=20)
    anoFabricacao = models.IntegerField()
    proprietario = models.ForeignKey(
        Proprietario,
        on_delete=models.CASCADE,
        related_name="veiculos")
    modelo = models.ForeignKey(
        Modelo,
        on_delete=models.CASCADE,
        related_name="veiculos")
 

class Agente(models.Model):
    matricula = models.AutoField(primary_key=True)
    dataContratacao = models.IntegerField()
    nome = models.CharField(max_length=50)


class Local(models.Model):
    codigo = models.AutoField(primary_key=True)
    velocidadeMax = models.FloatField()
    latitude = models.FloatField()
    longitude = models.FloatField()


class TipoInfracao(models.Model):
    codigo = models.IntegerField(primary_key=True)
    preco = models.FloatField()
    descricao = models.CharField(max_length=200)


class Infracao(models.Model):
    data = models.DateField()
    hora = models.TimeField()
    velocidadeAferida = models.FloatField()
    veiculo = models.ForeignKey(
        Veiculo,
        on_delete=models.PROTECT,
        related_name="infracoes")
    agente = models.ForeignKey(
        Agente,
        on_delete=models.PROTECT,
        related_name="infracoes")
    local = models.ForeignKey(
        Local,
        on_delete=models.PROTECT,
        related_name="infracoes")
    tipo = models.ForeignKey(
        TipoInfracao,
        on_delete=models.PROTECT,
        related_name="infracoes")