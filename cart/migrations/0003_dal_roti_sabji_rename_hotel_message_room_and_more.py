# Generated by Django 4.1.1 on 2022-10-22 15:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0002_hotels_hotel_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Roti',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sabji',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='message',
            old_name='hotel',
            new_name='room',
        ),
        migrations.RemoveField(
            model_name='hotels',
            name='food',
        ),
        migrations.AddField(
            model_name='hotels',
            name='topic',
            field=models.ForeignKey(blank=b'I01\n', null=True, on_delete=django.db.models.deletion.SET_NULL, to='cart.food'),
        ),
        migrations.CreateModel(
            name='Customize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('dal', models.ForeignKey(blank=b'I01\n', null=True, on_delete=django.db.models.deletion.SET_NULL, to='cart.dal')),
                ('food', models.ForeignKey(blank=b'I01\n', null=True, on_delete=django.db.models.deletion.SET_NULL, to='cart.food')),
                ('host', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('roti', models.ForeignKey(blank=b'I01\n', null=True, on_delete=django.db.models.deletion.SET_NULL, to='cart.roti')),
                ('sabji', models.ForeignKey(blank=b'I01\n', null=True, on_delete=django.db.models.deletion.SET_NULL, to='cart.sabji')),
            ],
        ),
    ]
