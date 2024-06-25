# Generated by Django 5.0.6 on 2024-06-25 19:27

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Ponto",
            fields=[
                ("title", models.CharField(max_length=200)),
                ("ID", models.AutoField(primary_key=True, serialize=False)),
                (
                    "origem",
                    models.CharField(
                        choices=[("joao", "João"), ("benja", "Benja")],
                        default="joao",
                        max_length=5,
                    ),
                ),
            ],
        ),
    ]
