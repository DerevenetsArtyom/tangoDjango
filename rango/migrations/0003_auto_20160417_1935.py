# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20160417_1805'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f', 'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438'},
        ),
        migrations.AlterModelOptions(
            name='page',
            options={'verbose_name': '\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430', 'verbose_name_plural': '\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u044b'},
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2016, 4, 17, 19, 35, 11, 83700, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='page',
            name='category',
            field=models.ForeignKey(verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f', to='rango.Category'),
        ),
        migrations.AlterField(
            model_name='page',
            name='url',
            field=models.URLField(verbose_name=b'\xd0\x90\xd0\xb4\xd1\x80\xd0\xb5\xd1\x81 \xd1\x81\xd0\xb0\xd0\xb9\xd1\x82\xd0\xb0'),
        ),
    ]
