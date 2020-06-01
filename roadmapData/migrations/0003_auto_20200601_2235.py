# Generated by Django 2.1.8 on 2020-06-01 14:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roadmapData', '0002_auto_20200531_1303'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(blank=True, default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='essay',
            name='like',
            field=models.ManyToManyField(blank=True, to='roadmapData.Like'),
        ),
        migrations.AddField(
            model_name='roadmap',
            name='like',
            field=models.ManyToManyField(blank=True, to='roadmapData.Like'),
        ),
    ]
