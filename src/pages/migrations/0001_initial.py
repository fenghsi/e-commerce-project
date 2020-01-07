# Generated by Django 2.0.7 on 2019-04-19 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('userid', models.IntegerField(db_column='UserID', primary_key=True, serialize=False)),
                ('firstname', models.CharField(db_column='Firstname', max_length=20)),
                ('lastname', models.CharField(db_column='Lastname', max_length=20)),
                ('emailaddress', models.CharField(db_column='EmailAddress', max_length=20, unique=True)),
                ('shipaddress', models.CharField(db_column='ShipAddress', max_length=30)),
                ('hashpassword', models.CharField(blank=True, db_column='HashPassword', max_length=20, null=True)),
            ],
            options={
                'db_table': 'Customer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('itemid', models.IntegerField(db_column='ItemID', primary_key=True, serialize=False)),
                ('price', models.FloatField(db_column='Price')),
                ('rates', models.FloatField(blank=True, db_column='Rates', null=True)),
                ('stock', models.IntegerField(blank=True, db_column='Stock', null=True)),
                ('name', models.CharField(db_column='Name', max_length=50)),
                ('description', models.CharField(blank=True, db_column='Description', max_length=200, null=True)),
                ('condit', models.CharField(blank=True, db_column='Condit', max_length=10, null=True)),
                ('status', models.IntegerField(blank=True, db_column='Status', null=True)),
            ],
            options={
                'db_table': 'Item',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('orderid', models.IntegerField(db_column='OrderId', primary_key=True, serialize=False)),
                ('totalprice', models.FloatField(blank=True, db_column='TotalPrice', null=True)),
                ('dates', models.CharField(blank=True, db_column='Dates', max_length=8, null=True)),
                ('shipaddress', models.CharField(blank=True, db_column='ShipAddress', max_length=30, null=True)),
                ('shippingfee', models.FloatField(blank=True, db_column='ShippingFee', null=True)),
                ('taxes', models.FloatField(blank=True, db_column='Taxes', null=True)),
                ('shippedtype', models.IntegerField(blank=True, db_column='ShippedType', null=True)),
            ],
            options={
                'db_table': 'Orders',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('sellerid', models.IntegerField(db_column='SellerID', primary_key=True, serialize=False)),
                ('rates', models.FloatField(blank=True, db_column='Rates', null=True)),
                ('storename', models.CharField(blank=True, db_column='StoreName', max_length=20, null=True)),
                ('status', models.IntegerField(blank=True, db_column='Status', null=True)),
                ('firstname', models.CharField(db_column='Firstname', max_length=20)),
                ('lastname', models.CharField(db_column='Lastname', max_length=20)),
                ('emailaddress', models.CharField(db_column='EmailAddress', max_length=50, unique=True)),
                ('hashpassword', models.CharField(blank=True, db_column='HashPassword', max_length=20, null=True)),
            ],
            options={
                'db_table': 'Seller',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('itemid', models.ForeignKey(db_column='ItemID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='pages.Item')),
                ('type', models.CharField(db_column='Type', max_length=20)),
            ],
            options={
                'db_table': 'Category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('itemid', models.ForeignKey(db_column='ItemId', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='pages.Item')),
                ('trackingnum', models.IntegerField(db_column='TrackingNum')),
                ('deliverredday', models.CharField(blank=True, db_column='DeliverredDay', max_length=8, null=True)),
                ('status', models.IntegerField(blank=True, db_column='Status', null=True)),
                ('company', models.CharField(blank=True, db_column='Company', max_length=20, null=True)),
            ],
            options={
                'db_table': 'Delivery',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Orderitem',
            fields=[
                ('orderid', models.ForeignKey(db_column='OrderId', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='pages.Orders')),
                ('price', models.FloatField(blank=True, db_column='Price', null=True)),
                ('quantity', models.IntegerField(blank=True, db_column='Quantity', null=True)),
                ('name', models.CharField(db_column='Name', max_length=50)),
                ('description', models.CharField(blank=True, db_column='Description', max_length=200, null=True)),
                ('condit', models.CharField(blank=True, db_column='Condit', max_length=10, null=True)),
            ],
            options={
                'db_table': 'OrderItem',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('userid', models.ForeignKey(db_column='UserID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='pages.Customer')),
                ('cardnum', models.BigIntegerField(db_column='Cardnum')),
                ('expiration', models.CharField(blank=True, db_column='Expiration', max_length=5, null=True)),
                ('billingaddress', models.CharField(blank=True, db_column='BillingAddress', max_length=30, null=True)),
                ('zipcode', models.CharField(blank=True, db_column='ZipCode', max_length=5, null=True)),
            ],
            options={
                'db_table': 'Payments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('userid', models.ForeignKey(db_column='UserId', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='pages.Customer')),
                ('rates', models.FloatField(blank=True, db_column='Rates', null=True)),
                ('description', models.CharField(blank=True, db_column='Description', max_length=500, null=True)),
            ],
            options={
                'db_table': 'Reviews',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ReviewsSeller',
            fields=[
                ('userid', models.ForeignKey(db_column='UserId', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='pages.Customer')),
                ('rates', models.FloatField(blank=True, db_column='Rates', null=True)),
                ('description', models.CharField(blank=True, db_column='Description', max_length=500, null=True)),
            ],
            options={
                'db_table': 'Reviews_Seller',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Shoppingcart',
            fields=[
                ('userid', models.ForeignKey(db_column='UserID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='pages.Customer')),
                ('price', models.FloatField(blank=True, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ShoppingCart',
                'managed': False,
            },
        ),
    ]