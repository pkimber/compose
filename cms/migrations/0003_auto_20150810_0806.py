# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_headerfooter_url_facebook'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HeaderFooter',
        ),
        migrations.AlterUniqueTogether(
            name='templatesection',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='templatesection',
            name='section',
        ),
        migrations.RemoveField(
            model_name='templatesection',
            name='template',
        ),
        migrations.DeleteModel(
            name='Template',
        ),
        migrations.DeleteModel(
            name='TemplateSection',
        ),
    ]
