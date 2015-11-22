# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conserve', '0002_auto_20151122_0139'),
    ]

    operations = [
        migrations.AddField(
            model_name='billdata',
            name='current_unit',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
