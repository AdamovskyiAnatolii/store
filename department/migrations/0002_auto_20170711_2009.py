# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-11 17:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(decimal_places=2, max_digits=2)),
                ('phone_number', models.PositiveIntegerField(blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='in_basket',
        ),
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='product',
            name='type_of_product',
            field=models.CharField(choices=[('MB', 'Mobile'), ('LP', 'Laptop'), ('TB', 'Tablet'), ('CN', 'Consoles')], default='', max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='desire',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='department.Product'),
        ),
        migrations.AddField(
            model_name='seller',
            name='pub_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.Product'),
        ),
        migrations.AddField(
            model_name='user',
            name='seller',
            field=models.OneToOneField(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='department.Seller'),
            preserve_default=False,
        ),
    ]
