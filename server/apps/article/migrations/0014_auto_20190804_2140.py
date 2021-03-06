# Generated by Django 2.2 on 2019-08-04 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0013_auto_20190804_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic_image',
            name='index',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='话题图片索引'),
        ),
        migrations.AlterField(
            model_name='topic_image',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='Topic/%Y/%m/%d', verbose_name='话题图片'),
        ),
    ]
