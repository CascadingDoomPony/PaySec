# Generated by Django 2.2.13 on 2020-07-02 19:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("server", "0004_auto_20200427_2302"),
    ]

    operations = [
        migrations.AddField(
            model_name="polarisstellaraccount",
            name="memo",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="polarisstellaraccount",
            name="memo_type",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="polarisstellaraccount",
            name="account",
            field=models.CharField(
                max_length=56,
                validators=[django.core.validators.MinLengthValidator(56)],
            ),
        ),
        migrations.AlterUniqueTogether(
            name="polarisstellaraccount",
            unique_together={("memo", "account")},
        ),
    ]
