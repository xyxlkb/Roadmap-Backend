# Generated by Django 2.1.8 on 2020-05-27 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roadmapData', '0015_auto_20200527_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='roadmap',
            name='tag',
            field=models.ManyToManyField(blank=True, to='roadmapData.Tag'),
        ),
    ]