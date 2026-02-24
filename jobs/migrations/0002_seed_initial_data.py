from django.db import migrations


def create_initial_data(apps, schema_editor):

    City = apps.get_model('jobs', 'City')
    Category = apps.get_model('jobs', 'Category')

    cities = [
        'Sofia',
        'Plovdiv',
        'Varna',
        'Burgas',
        'Ruse',
        'Stara Zagora',
    ]

    for name in cities:
        City.objects.get_or_create(name=name)


    categories = [
        'PAINTING',
        'TILING',
        'PLUMBING',
        'ELECTRICAL',
        'CARPENTRY',
        'FLOORING',
        'DRYWALL',
        'RENOVATION',
        'MASONRY',
        'GENERAL_REPAIR',
    ]

    for name in categories:
        Category.objects.get_or_create(name=name)


def delete_initial_data(apps, schema_editor):

    City = apps.get_model('jobs', 'City')
    Category = apps.get_model('jobs', 'Category')

    City.objects.filter(
        name__in=[
            'Sofia',
            'Plovdiv',
            'Varna',
            'Burgas',
            'Ruse',
            'Stara Zagora',
        ]
    ).delete()

    Category.objects.filter(
        name__in=[
            'PAINTING',
            'TILING',
            'PLUMBING',
            'ELECTRICAL',
            'CARPENTRY',
            'FLOORING',
            'DRYWALL',
            'RENOVATION',
            'MASONRY',
            'GENERAL_REPAIR',
        ]
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            create_initial_data,
            delete_initial_data,
        ),
    ]