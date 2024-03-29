# Generated by Django 4.2.7 on 2023-12-02 18:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ContactMessage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("message", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Currency",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("code", models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name="Feedback",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("message", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "cryptocurrency_experience",
                    models.IntegerField(
                        choices=[(1, "Novice"), (2, "Intermediate"), (3, "Advanced")],
                        default=1,
                    ),
                ),
                (
                    "platform_satisfaction",
                    models.IntegerField(
                        choices=[
                            (1, "Not satisfied"),
                            (2, "Satisfied"),
                            (3, "Very satisfied"),
                        ],
                        default=2,
                    ),
                ),
                (
                    "security_confidence",
                    models.IntegerField(
                        choices=[(1, "Low"), (2, "Moderate"), (3, "High")], default=2
                    ),
                ),
                ("future_expectations", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="StockData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("symbol", models.CharField(max_length=10)),
                ("price", models.DecimalField(decimal_places=2, max_digits=20)),
                ("market_cap", models.DecimalField(decimal_places=2, max_digits=20)),
                (
                    "change_percentage",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("volume_24h", models.DecimalField(decimal_places=2, max_digits=20)),
                ("lasthour", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "volume_change_24h",
                    models.DecimalField(decimal_places=2, max_digits=20),
                ),
                ("last24h", models.DecimalField(decimal_places=2, max_digits=10)),
                ("week", models.DecimalField(decimal_places=2, max_digits=10)),
                ("month", models.DecimalField(decimal_places=2, max_digits=10)),
                ("TwoMonths", models.DecimalField(decimal_places=2, max_digits=10)),
                ("ThreeMonths", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=20, null=True)),
                ("last_name", models.CharField(max_length=20, null=True)),
                ("date_of_birth", models.DateField(null=True)),
                ("email", models.EmailField(max_length=254, null=True)),
                ("phone_no", models.IntegerField(null=True)),
                (
                    "profile_image",
                    models.ImageField(blank=True, upload_to="profile_images"),
                ),
                (
                    "user",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PaymentHistory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "payment_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "transaction_id",
                    models.CharField(blank=True, max_length=8, null=True, unique=True),
                ),
                ("stock_name", models.CharField(max_length=100)),
                ("quantity_purchased", models.IntegerField(default=1)),
                ("updated_quantity", models.IntegerField(default=0)),
                ("purchased_currency", models.CharField(default="CAD", max_length=3)),
                (
                    "purchase_price_per_unit",
                    models.DecimalField(decimal_places=2, default=1, max_digits=10),
                ),
                (
                    "total_purchase_amount",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                (
                    "updated_total_amount",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                (
                    "payment_method",
                    models.CharField(
                        choices=[("OL", "ONLINE"), ("CARD", "CARD")],
                        default="OL",
                        max_length=4,
                    ),
                ),
                (
                    "transaction_type",
                    models.CharField(
                        choices=[("B", "BUY"), ("S", "SELL")],
                        default="B",
                        max_length=10,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("A", "ACTIVE"), ("I", "INACTIVE")],
                        default="A",
                        max_length=4,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-payment_date"],
            },
        ),
    ]
