# Generated by Django 3.0.5 on 2020-04-22 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roadmapData', '0005_auto_20200422_2217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='article_references',
        ),
        migrations.AddField(
            model_name='article',
            name='article_references',
            field=models.ManyToManyField(blank=True, null=True, to='roadmapData.Article'),
        ),
        migrations.RemoveField(
            model_name='roadmap',
            name='road_maps',
        ),
        migrations.AddField(
            model_name='roadmap',
            name='road_maps',
            field=models.ManyToManyField(blank=True, null=True, to='roadmapData.RoadMap'),
        ),
    ]