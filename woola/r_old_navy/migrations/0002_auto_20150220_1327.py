# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('r_old_navy', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='R_Old_Navy',
            new_name='Item',
        ),
    ]