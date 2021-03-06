# Generated by Django 3.1.4 on 2021-01-06 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agente',
            fields=[
                ('matricula', models.IntegerField(primary_key=True, serialize=False)),
                ('dataContratacao', models.IntegerField()),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('velocidadeMax', models.FloatField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(blank=True, max_length=30)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modelos', to='app.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Proprietario',
            fields=[
                ('cpf', models.IntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('bairro', models.CharField(max_length=50)),
                ('logradouro', models.CharField(max_length=50)),
                ('numero', models.IntegerField()),
                ('cidade', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=2)),
                ('cep', models.IntegerField(default=0)),
                ('complemento', models.CharField(max_length=200)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], default='M', max_length=2)),
                ('dataNascimento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoInfracao',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('preco', models.FloatField()),
                ('descricao', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('placa', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('chassi', models.CharField(max_length=8, unique=True)),
                ('cor', models.CharField(max_length=20)),
                ('anoFabricacao', models.IntegerField()),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='veiculos', to='app.modelo')),
                ('proprietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='veiculos', to='app.proprietario')),
            ],
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefone', models.IntegerField()),
                ('proprietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='telefones', to='app.proprietario')),
            ],
        ),
        migrations.CreateModel(
            name='Infracao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('hora', models.TimeField()),
                ('velocidadeAferida', models.FloatField()),
                ('agente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='infracoes', to='app.agente')),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='infracoes', to='app.local')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='infracoes', to='app.tipoinfracao')),
                ('veiculo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='infracoes', to='app.veiculo')),
            ],
        ),
    ]
