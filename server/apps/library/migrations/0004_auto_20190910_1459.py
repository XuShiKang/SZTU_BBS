# Generated by Django 2.2 on 2019-09-10 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0023_auto_20190828_1333'),
        ('library', '0003_discuss_room_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='discuss_room',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='user.User', verbose_name='申请用户id'),
        ),
        migrations.AddField(
            model_name='discuss_room',
            name='user_name',
            field=models.CharField(default='', max_length=10, verbose_name='申请人姓名'),
        ),
    ]
