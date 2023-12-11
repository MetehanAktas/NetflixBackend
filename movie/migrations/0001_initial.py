# Generated by Django 4.1.1 on 2023-08-14 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=50)),
                ('resim', models.FileField(blank=True, null=True, upload_to='filmler', verbose_name='resim giriniz')),
                ('kategori', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='movie.kategori')),
            ],
        ),
    ]
