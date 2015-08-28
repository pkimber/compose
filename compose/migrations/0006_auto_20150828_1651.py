# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import block.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0007_auto_20150821_2228'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('compose', '0005_remove_article_picture_old'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('date_moderated', models.DateTimeField(blank=True, null=True)),
                ('order', models.IntegerField()),
                ('title', models.TextField()),
                ('description', models.TextField(blank=True)),
                ('picture', models.ImageField(blank=True, upload_to='block')),
            ],
            options={
                'verbose_name_plural': 'Feature blocks',
                'verbose_name': 'Feature block',
            },
        ),
        migrations.CreateModel(
            name='FeatureBlock',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('page_section', models.ForeignKey(to='block.PageSection')),
            ],
            options={
                'verbose_name_plural': 'Blocks',
                'abstract': False,
                'verbose_name': 'Block',
            },
        ),
        migrations.CreateModel(
            name='FeatureStyle',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('css_class_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Feature Styles',
                'verbose_name': 'Feature Style',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('date_moderated', models.DateTimeField(blank=True, null=True)),
                ('order', models.IntegerField()),
                ('title', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Headers',
                'verbose_name': 'Header',
            },
        ),
        migrations.CreateModel(
            name='HeaderBlock',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('page_section', models.ForeignKey(to='block.PageSection')),
            ],
            options={
                'verbose_name_plural': 'Blocks',
                'abstract': False,
                'verbose_name': 'Block',
            },
        ),
        migrations.CreateModel(
            name='HeaderStyle',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('css_class_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Header styles',
                'verbose_name': 'Header style',
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='header',
            name='block',
            field=models.ForeignKey(to='compose.HeaderBlock', related_name='content'),
        ),
        migrations.AddField(
            model_name='header',
            name='edit_state',
            field=models.ForeignKey(to='block.EditState', default=block.models._default_edit_state),
        ),
        migrations.AddField(
            model_name='header',
            name='moderate_state',
            field=models.ForeignKey(to='block.ModerateState', default=block.models._default_moderate_state),
        ),
        migrations.AddField(
            model_name='header',
            name='style',
            field=models.ForeignKey(null=True, to='compose.HeaderStyle', blank=True),
        ),
        migrations.AddField(
            model_name='header',
            name='user_moderated',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, blank=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='feature',
            name='block',
            field=models.ForeignKey(to='compose.FeatureBlock', related_name='content'),
        ),
        migrations.AddField(
            model_name='feature',
            name='edit_state',
            field=models.ForeignKey(to='block.EditState', default=block.models._default_edit_state),
        ),
        migrations.AddField(
            model_name='feature',
            name='link',
            field=models.ForeignKey(null=True, to='block.Link', blank=True, related_name='feature_link'),
        ),
        migrations.AddField(
            model_name='feature',
            name='moderate_state',
            field=models.ForeignKey(to='block.ModerateState', default=block.models._default_moderate_state),
        ),
        migrations.AddField(
            model_name='feature',
            name='style',
            field=models.ForeignKey(null=True, to='compose.FeatureStyle', blank=True),
        ),
        migrations.AddField(
            model_name='feature',
            name='user_moderated',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, blank=True, related_name='+'),
        ),
        migrations.AlterUniqueTogether(
            name='header',
            unique_together=set([('block', 'moderate_state')]),
        ),
        migrations.AlterUniqueTogether(
            name='feature',
            unique_together=set([('block', 'moderate_state')]),
        ),
    ]
