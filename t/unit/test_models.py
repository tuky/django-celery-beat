from __future__ import absolute_import, unicode_literals

import importlib

from django.test import TestCase, override_settings
from django.utils import six

from django_celery_beat import models


class ModelMigrationTests(TestCase):
    def test_periodic_task_name_max_length_defaults_to_200_in_model(self):
        six.moves.reload_module(models)
        self.assertEqual(
            200, models.PeriodicTask._meta.get_field('name').max_length)

    @override_settings(DJANGO_CELERY_BEAT_NAME_MAX_LENGTH=191)
    def test_periodic_task_name_max_length_changed_to_191_in_model(self):
        six.moves.reload_module(models)
        self.assertEqual(
            191, models.PeriodicTask._meta.get_field('name').max_length)

    def test_periodic_task_name_max_length_defaults_to_200_in_migration(self):
        initial_migration_module = importlib.import_module(
            'django_celery_beat.migrations.0001_initial')
        six.moves.reload_module(initial_migration_module)
        initial_migration = initial_migration_module.Migration
        periodic_task_creation = initial_migration.operations[2]
        fields = dict(periodic_task_creation.fields)

        self.assertEqual('PeriodicTask', periodic_task_creation.name)
        self.assertEqual(200, fields['name'].max_length)

    @override_settings(DJANGO_CELERY_BEAT_NAME_MAX_LENGTH=191)
    def test_periodic_task_name_max_length_changed_to_191_in_migration(self):
        initial_migration_module = importlib.import_module(
            'django_celery_beat.migrations.0001_initial')
        six.moves.reload_module(initial_migration_module)
        initial_migration = initial_migration_module.Migration
        periodic_task_creation = initial_migration.operations[2]
        fields = dict(periodic_task_creation.fields)

        self.assertEqual('PeriodicTask', periodic_task_creation.name)
        self.assertEqual(191, fields['name'].max_length)
