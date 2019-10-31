from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='despesa',
            options={'ordering': ('vencimento', 'formaDePagamento'), 'verbose_name': 'despesa', 'verbose_name_plural': 'despesas'},
        ),
    ]
