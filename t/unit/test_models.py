from __future__ import absolute_import, unicode_literals

import importlib

from django.test import TestCase

from django_celery_beat.models import PeriodicTask


class ModelMigrationTests(TestCase):
    def test_periodic_task_name_max_length_defaults_to_200_in_model(self):
        self.assertEqual(200, PeriodicTask._meta.get_field('name').max_length)

    def test_periodic_task_name_max_length_defaults_to_200_in_migration(self):
        initial_migration = importlib.import_module('django_celery_beat.migrations.0001_initial').Migration
        periodic_task_creation = initial_migration.operations[2]
        fields = dict(periodic_task_creation.fields)

        self.assertEqual('PeriodicTask', periodic_task_creation.name)
        self.assertEqual(200, fields['name'].max_length)
