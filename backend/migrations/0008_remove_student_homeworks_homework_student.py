# Generated by Django 4.2.5 on 2023-11-25 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0007_admin_admin_id_c0fa98_idx_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="homeworks",
        ),
        migrations.AddField(
            model_name="homework",
            name="student",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="backend.student",
            ),
        ),
    ]
