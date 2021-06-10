# Generated by Django 3.2.3 on 2021-06-04 15:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("peering", "0074_add_configcontext")]

    operations = [
        migrations.AlterModelOptions(
            name="directpeeringsession",
            options={
                "ordering": [
                    "service_reference",
                    "local_autonomous_system",
                    "autonomous_system",
                    "ip_address",
                ]
            },
        ),
        migrations.AlterModelOptions(
            name="internetexchangepeeringsession",
            options={
                "ordering": [
                    "service_reference",
                    "autonomous_system",
                    "ixp_connection",
                    "ip_address",
                ]
            },
        ),
        migrations.AddField(
            model_name="directpeeringsession",
            name="service_reference",
            field=models.CharField(
                blank=True,
                help_text="Optional internal service reference",
                max_length=255,
                null=True,
                unique=True,
            ),
        ),
        migrations.AddField(
            model_name="internetexchangepeeringsession",
            name="service_reference",
            field=models.CharField(
                blank=True,
                help_text="Optional internal service reference",
                max_length=255,
                null=True,
                unique=True,
            ),
        ),
    ]