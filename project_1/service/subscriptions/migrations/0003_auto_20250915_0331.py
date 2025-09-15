from django.db import migrations


def assign_default_tariff(apps, schema_editor):
    UserSubscription = apps.get_model('subscriptions', 'UserSubscription')
    Tariff = apps.get_model('subscriptions', 'Tariff')

    default_tariff, created = Tariff.objects.get_or_create(
        name='Базовый тариф',
        defaults={
            'price': 250,
        }
    )

    # Обновляем все подписки без tariff
    UserSubscription.objects.filter(tariff__isnull=True).update(tariff=default_tariff)


class Migration(migrations.Migration):
    dependencies = [
        ('subscriptions', '0002_alter_usersubscription_tariff_and_more'),
    ]

    operations = [
        migrations.RunPython(assign_default_tariff),
    ]