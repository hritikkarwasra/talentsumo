# Generated by Django 4.1 on 2022-08-06 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0009_rename_test_id_interaction_test"),
    ]

    operations = [
        migrations.AddField(
            model_name="candidate",
            name="access_code",
            field=models.CharField(default=True, max_length=255),
        ),
    ]
