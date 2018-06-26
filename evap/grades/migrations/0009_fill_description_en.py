# Generated by Django 1.9.1 on 2016-01-04 18:32

from django.db import migrations


def fill_description_en(apps, _schema_editor):
    GradeDocument = apps.get_model("grades", "GradeDocument")
    gradeDocuments = GradeDocument.objects.all()
    for gradeDocument in gradeDocuments:
        gradeDocument.description_en = gradeDocument.description_de
        gradeDocument.save()


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0008_add_gradedocument_description_en'),
    ]

    operations = [
        migrations.RunPython(fill_description_en, reverse_code=migrations.RunPython.noop),
    ]
