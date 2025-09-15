from django.db import migrations


def assign_default_category(apps, schema_editor):
    Product = apps.get_model('products', 'Product')
    Category = apps.get_model('products', 'Category')

    default_category, created = Category.objects.get_or_create(
        name='Без категории',
    )

    Product.objects.filter(category__isnull=True).update(category=default_category)


class Migration(migrations.Migration):
    dependencies = [
        ('products', '0002_alter_product_category'),
    ]

    operations = [
        migrations.RunPython(assign_default_category),
    ]