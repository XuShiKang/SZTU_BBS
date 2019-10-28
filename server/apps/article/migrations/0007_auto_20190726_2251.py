# Generated by Django 2.2 on 2019-07-26 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_remove_reply_reply_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic_image',
            name='image_1',
            field=models.ImageField(blank=True, default='', null=True, upload_to='Reply/%Y%m%d', verbose_name='话题图片1'),
        ),
        migrations.AlterField(
            model_name='topic_image',
            name='image_2',
            field=models.ImageField(blank=True, default='', null=True, upload_to='Reply/%Y%m%d', verbose_name='话题图片2'),
        ),
        migrations.AlterField(
            model_name='topic_image',
            name='image_3',
            field=models.ImageField(blank=True, default='', null=True, upload_to='Reply/%Y%m%d', verbose_name='话题图片3'),
        ),
        migrations.AlterField(
            model_name='topic_image',
            name='image_4',
            field=models.ImageField(blank=True, default='', null=True, upload_to='Reply/%Y%m%d', verbose_name='话题图片4'),
        ),
        migrations.AlterField(
            model_name='topic_image',
            name='image_5',
            field=models.ImageField(blank=True, default='', null=True, upload_to='Reply/%Y%m%d', verbose_name='话题图片5'),
        ),
        migrations.AlterField(
            model_name='topic_image',
            name='image_6',
            field=models.ImageField(blank=True, default='', null=True, upload_to='Reply/%Y%m%d', verbose_name='话题图片6'),
        ),
    ]