# Generated by Django 4.2.11 on 2024-04-25 08:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_user_password_hash'),
    ]

    operations = [
        migrations.CreateModel(
            name='EggGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=79)),
            ],
            options={
                'db_table': 'egg_groups',
            },
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=79)),
                ('category_id', models.IntegerField()),
                ('cost', models.IntegerField()),
                ('fling_power', models.IntegerField(blank=True, null=True)),
                ('fling_effect_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'items',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_id', models.IntegerField(blank=True, null=True)),
                ('identifier', models.CharField(max_length=79)),
            ],
            options={
                'db_table': 'locations',
            },
        ),
        migrations.CreateModel(
            name='Move',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=79)),
                ('generation_id', models.IntegerField()),
                ('type_id', models.IntegerField()),
                ('power', models.SmallIntegerField(null=True)),
                ('pp', models.SmallIntegerField(null=True)),
                ('accuracy', models.SmallIntegerField(null=True)),
                ('priority', models.SmallIntegerField()),
                ('target_id', models.IntegerField()),
                ('damage_class_id', models.IntegerField()),
                ('effect_id', models.IntegerField()),
                ('effect_chance', models.IntegerField(null=True)),
                ('contest_type_id', models.IntegerField(null=True)),
                ('contest_effect_id', models.IntegerField(null=True)),
                ('super_contest_effect_id', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'moves',
            },
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=79)),
                ('species_id', models.IntegerField()),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('base_experience', models.IntegerField()),
                ('order', models.IntegerField()),
                ('is_default', models.BooleanField()),
            ],
            options={
                'db_table': 'pokemon',
            },
        ),
        migrations.CreateModel(
            name='PokemonFormGeneration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pokemon_form_id', models.IntegerField()),
                ('generation_id', models.IntegerField()),
                ('game_index', models.IntegerField()),
            ],
            options={
                'db_table': 'pokemon_form_generations',
            },
        ),
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('damage_class_id', models.IntegerField(blank=True, null=True)),
                ('identifier', models.CharField(max_length=79)),
                ('is_battle_only', models.BooleanField()),
                ('game_index', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'stats',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=79)),
                ('generation_id', models.IntegerField()),
                ('damage_class_id', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'types',
            },
        ),
        migrations.AlterField(
            model_name='user',
            name='password_hash',
            field=models.CharField(default='pbkdf2_sha256$600000$To3ygpy30MoQtmo9RE2fzP$szKi/9scLLaNwWPUZcpFDkbNh6RKA1P4t2b5tTJkHNg=', max_length=255),
        ),
        migrations.CreateModel(
            name='PokemonUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_caught', models.DateTimeField()),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owners', to='api.pokemon')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pokemons', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_',
            },
        ),
        migrations.CreateModel(
            name='PokemonType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot', models.IntegerField()),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.pokemon')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.type')),
            ],
            options={
                'db_table': 'pokemon_types',
            },
        ),
        migrations.CreateModel(
            name='PokemonStat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_stat', models.IntegerField()),
                ('effort', models.IntegerField()),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pokemon_stats', to='api.pokemon')),
                ('stat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.stats')),
            ],
            options={
                'db_table': 'pokemon_stats',
            },
        ),
        migrations.CreateModel(
            name='PokemonMove',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField()),
                ('order', models.IntegerField(null=True)),
                ('move', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.move')),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.pokemon')),
            ],
            options={
                'db_table': 'pokemon_moves',
            },
        ),
        migrations.CreateModel(
            name='PokemonEggGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('egg_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.egggroup')),
                ('species_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.pokemon')),
            ],
            options={
                'db_table': 'pokemon_egg_groups',
            },
        ),
    ]
