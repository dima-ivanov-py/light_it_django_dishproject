# Generated by Django 3.2.5 on 2021-07-15 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('amount', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dishes.ingredient')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dishes.order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='ingredients',
            field=models.ManyToManyField(through='dishes.OrderIngredient', to='dishes.Ingredient'),
        ),
        migrations.CreateModel(
            name='DishIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dishes.dish')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dishes.ingredient')),
            ],
        ),
        migrations.AddField(
            model_name='dish',
            name='ingredients',
            field=models.ManyToManyField(through='dishes.DishIngredient', to='dishes.Ingredient'),
        ),
    ]
