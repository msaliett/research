# Generated by Django 4.2.2 on 2023-06-30 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datein', models.DateField()),
                ('dateout', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Investigator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('budget', models.DecimalField(decimal_places=2, max_digits=12)),
                ('investigators', models.ManyToManyField(through='researchprojects.Assignment', to='researchprojects.investigator')),
                ('pi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='led_projects', to='researchprojects.investigator')),
            ],
        ),
        migrations.CreateModel(
            name='HourEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours', models.PositiveIntegerField()),
                ('date', models.DateField()),
                ('investigator', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='researchprojects.investigator')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='researchprojects.project')),
            ],
        ),
        migrations.AddField(
            model_name='assignment',
            name='investigator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='researchprojects.investigator'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='researchprojects.project'),
        ),
    ]
