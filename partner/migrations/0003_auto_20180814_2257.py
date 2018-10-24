# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-08-14 14:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0002_partner_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=50)),
                ('price', models.PositiveIntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='partner',
            name='address',
            field=models.CharField(max_length=200, verbose_name='주소'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='contact',
            field=models.CharField(max_length=50, verbose_name='전화 번호'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='description',
            field=models.TextField(verbose_name='상세 정보'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='name',
            field=models.CharField(max_length=50, verbose_name='업체 이름'),
        ),
        migrations.AddField(
            model_name='menu',
            name='partner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partner.Partner'),
        ),
    ]