# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0014_auto_20160610_0516'),
    ]

    operations = [
        migrations.CreateModel(
            name='AptitudeTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marks', models.FloatField(verbose_name='Mark', blank=True)),
                ('student', models.ForeignKey(to='registration.Student')),
                ('test', models.ForeignKey(to='registration.Test')),
            ],
        ),
        migrations.CreateModel(
            name='EligibilityTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marks', models.FloatField(verbose_name='Mark', blank=True)),
                ('student', models.ForeignKey(to='registration.Student')),
                ('test', models.ForeignKey(to='registration.Test')),
            ],
        ),
        migrations.CreateModel(
            name='HRTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marks', models.FloatField(verbose_name='Mark', blank=True)),
                ('student', models.ForeignKey(to='registration.Student')),
                ('test', models.ForeignKey(to='registration.Test')),
            ],
        ),
        migrations.CreateModel(
            name='QuantitativeTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marks', models.FloatField(verbose_name='Mark', blank=True)),
                ('student', models.ForeignKey(to='registration.Student')),
                ('test', models.ForeignKey(to='registration.Test')),
            ],
        ),
        migrations.CreateModel(
            name='ReasoningTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marks', models.FloatField(verbose_name='Mark', blank=True)),
                ('student', models.ForeignKey(to='registration.Student')),
                ('test', models.ForeignKey(to='registration.Test')),
            ],
        ),
        migrations.CreateModel(
            name='TechTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marks', models.FloatField(verbose_name='Mark', blank=True)),
                ('student', models.ForeignKey(to='registration.Student')),
                ('test', models.ForeignKey(to='registration.Test')),
            ],
        ),
        migrations.CreateModel(
            name='VerbalTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marks', models.FloatField(verbose_name='Mark', blank=True)),
                ('student', models.ForeignKey(to='registration.Student')),
                ('test', models.ForeignKey(to='registration.Test')),
            ],
        ),
    ]
