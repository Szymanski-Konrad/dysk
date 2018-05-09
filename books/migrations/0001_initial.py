# Generated by Django 2.0.5 on 2018-05-08 07:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dysk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Katalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Konto',
            fields=[
                ('konto', models.IntegerField(primary_key=True, serialize=False)),
                ('pojemnosc', models.IntegerField()),
                ('uzytkownik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Plik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=50)),
                ('adres', models.TextField()),
                ('czy_udostepniony', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Struktura_Konta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('konto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Konto')),
                ('lista_katalogow', models.ManyToManyField(to='books.Katalog')),
            ],
        ),
        migrations.AddField(
            model_name='katalog',
            name='lista_plikow',
            field=models.ManyToManyField(to='books.Plik'),
        ),
        migrations.AddField(
            model_name='dysk',
            name='lista_kont',
            field=models.ManyToManyField(to='books.Konto'),
        ),
    ]