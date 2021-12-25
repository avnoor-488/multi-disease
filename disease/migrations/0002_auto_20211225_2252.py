# Generated by Django 3.2.9 on 2021-12-25 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disease', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='breastcancer',
            name='area_se',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='breastcancer',
            name='area_worst',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='breastcancer',
            name='compactness_se',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='breastcancer',
            name='compactness_worst',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='breastcancer',
            name='concave_points_se',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='breastcancer',
            name='concave_points_worst',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='breastcancer',
            name='concavity_se',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='breastcancer',
            name='concavity_worst',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='breastcancer',
            name='fractal_dimension_se',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='breastcancer',
            name='fractal_dimension_worst',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='breastcancer',
            name='perimeter_se',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='breastcancer',
            name='perimeter_worst',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='breastcancer',
            name='radius_worst',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='breastcancer',
            name='smoothness_worst',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='breastcancer',
            name='symmetry_worst',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='breastcancer',
            name='texture_worst',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='breastcancer',
            name='area_mean',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='breastcancer',
            name='compactness_mean',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='breastcancer',
            name='concave_points_mean',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='breastcancer',
            name='concavity_mean',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='breastcancer',
            name='perimeter_mean',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='breastcancer',
            name='radius_mean',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='breastcancer',
            name='radius_se',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='breastcancer',
            name='smoothness_mean',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='breastcancer',
            name='symmetry_mean',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='breastcancer',
            name='texture_mean',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]
