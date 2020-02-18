# Generated by Django 2.2.4 on 2019-09-30 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('numeroDeIntentos', models.IntegerField(default=0)),
                ('tieneRetroalimentacion', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Calificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calificacion', models.DecimalField(decimal_places=2, max_digits=10)),
                ('retroalimentacion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('punto', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pregunta', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='RespuestaAbiertaEstudiante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta', models.CharField(max_length=200)),
                ('nota', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='RespuestaEstudianteVoF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta', models.BooleanField()),
                ('nota', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='RespuestaVoF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('esCorrecta', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Respuestmultiple',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta', models.CharField(max_length=200)),
                ('esCorrecta', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='RespuestmultipleEstudiante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seleccionada', models.BooleanField()),
            ],
        ),
        migrations.RemoveField(
            model_name='activitytype',
            name='polymorphic_ctype',
        ),
        migrations.RemoveField(
            model_name='filequestion',
            name='activitytype_ptr',
        ),
        migrations.RemoveField(
            model_name='multiplequestion',
            name='activitytype_ptr',
        ),
        migrations.RemoveField(
            model_name='togglequestion',
            name='related_question',
        ),
        migrations.DeleteModel(
            name='Activity',
        ),
        migrations.DeleteModel(
            name='ActivityType',
        ),
        migrations.DeleteModel(
            name='FileQuestion',
        ),
        migrations.DeleteModel(
            name='Marker',
        ),
        migrations.DeleteModel(
            name='MultipleQuestion',
        ),
        migrations.DeleteModel(
            name='ToggleQuestion',
        ),
    ]