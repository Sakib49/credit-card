# Generated by Django 2.1 on 2018-12-02 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommender', '0002_person_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_name', models.CharField(max_length=150)),
                ('bank_name', models.CharField(max_length=150)),
                ('url', models.CharField(max_length=300)),
                ('card_type', models.CharField(max_length=100)),
                ('interest_rate', models.FloatField()),
                ('cash_withdrawal_limit_per_transaction', models.FloatField()),
                ('cash_withdrawal_limit_per_day', models.FloatField()),
                ('max_credit_limit', models.FloatField()),
                ('international_transaction_available', models.BooleanField(default=False)),
                ('balance_transfer_available', models.BooleanField(default=False)),
                ('dual_currency', models.BooleanField(default=False)),
                ('reward_supplementary_card', models.BooleanField(default=False)),
                ('reward_airport_lounge', models.BooleanField(default=False)),
                ('reward_cashback_available', models.BooleanField(default=False)),
                ('reward_luxary_resort_hotel', models.BooleanField(default=False)),
                ('reward_insurance_plan', models.BooleanField(default=False)),
                ('reward_travel_benefits', models.BooleanField(default=False)),
                ('reward_fine_dining', models.BooleanField(default=False)),
                ('reward_buffet_discount', models.BooleanField(default=False)),
                ('reward_medical_discount', models.BooleanField(default=False)),
                ('reward_shopping', models.BooleanField(default=False)),
                ('reward_airlines_ticket', models.BooleanField(default=False)),
                ('reward_point_program', models.BooleanField(default=False)),
                ('reward_emi_available', models.BooleanField(default=False)),
            ],
        ),
    ]