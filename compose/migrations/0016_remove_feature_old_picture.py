# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compose', '0015_auto_20151105_0945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feature',
            name='old_picture',
        ),
    ]
