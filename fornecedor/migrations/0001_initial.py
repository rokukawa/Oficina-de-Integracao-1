# Generated by Django 3.2.6 on 2021-08-25 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_fornecedor', models.CharField(blank=True, max_length=100)),
                ('cnpj', models.CharField(blank=True, max_length=45)),
                ('celular', models.CharField(blank=True, max_length=20)),
                ('comercial', models.CharField(blank=True, max_length=20)),
                ('residencial', models.CharField(blank=True, max_length=20)),
                ('rua', models.CharField(blank=True, max_length=45)),
                ('numero', models.CharField(blank=True, max_length=45)),
                ('cidade', models.CharField(blank=True, max_length=45)),
                ('cep', models.CharField(blank=True, max_length=45)),
                ('bairro', models.TextField(blank=True, max_length=45)),
                ('complemento', models.TextField(blank=True, max_length=45, null=True)),
            ],
        ),
    ]