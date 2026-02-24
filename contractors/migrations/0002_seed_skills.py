from django.db import migrations


def create_skills(apps, schema_editor):

    Skill = apps.get_model('contractors', 'Skill')

    skills = [
        'Painting',
        'Tiling',
        'Plumbing',
        'Electrical',
        'Carpentry',
        'Flooring',
        'Drywall',
        'Renovation',
        'Masonry',
        'General Repair',
    ]

    for name in skills:
        Skill.objects.get_or_create(name=name)


def delete_skills(apps, schema_editor):

    Skill = apps.get_model('contractors', 'Skill')

    Skill.objects.filter(
        name__in=[
            'Painting',
            'Tiling',
            'Plumbing',
            'Electrical',
            'Carpentry',
            'Flooring',
            'Drywall',
            'Renovation',
            'Masonry',
            'General Repair',
        ]
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('contractors', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            create_skills,
            delete_skills,
        ),
    ]