# Generated by Django 4.2.6 on 2023-10-29 21:02

from django.db import migrations
import nanoid_field.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', nanoid_field.fields.NanoidField(default=nanoid_field.fields.NanoidField.nanoid, editable=False, max_length=21, primary_key=True, serialize=False)),
                ('override', nanoid_field.fields.NanoidField(default=nanoid_field.fields.NanoidField.nanoid, max_length=2)),
            ],
        ),
    ]
