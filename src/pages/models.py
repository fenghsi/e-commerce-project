from django.db import models

# Create your models here.

class Seller(models.Model):
    sellerid = models.IntegerField(db_column='SellerID', primary_key=True)  # Field name made lowercase.
    rates = models.FloatField(db_column='Rates', blank=True, null=True)  # Field name made lowercase.
    storename = models.CharField(db_column='StoreName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='Firstname', max_length=20)  # Field name made lowercase.
    lastname = models.CharField(db_column='Lastname', max_length=20)  # Field name made lowercase.
    emailaddress = models.CharField(db_column='EmailAddress', unique=True, max_length=50)  # Field name made lowercase.
    hashpassword = models.CharField(db_column='HashPassword', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Seller'


class Item(models.Model):
    itemid = models.IntegerField(db_column='ItemID', primary_key=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price')  # Field name made lowercase.
    rates = models.FloatField(db_column='Rates', blank=True, null=True)  # Field name made lowercase.
    stock = models.IntegerField(db_column='Stock', blank=True, null=True)  # Field name made lowercase.
    sellerid = models.ForeignKey('Seller', models.DO_NOTHING, db_column='SellerID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=200, blank=True, null=True)  # Field name made lowercase.
    condit = models.CharField(db_column='Condit', max_length=10, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    image = models.CharField(db_column='image', max_length=50)
    soldnum = models.IntegerField(db_column='Soldnum', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'Item'

class Category(models.Model):
    categoryid = models.IntegerField(db_column='categoryid', primary_key=True)
    itemid = models.ForeignKey('Item', models.DO_NOTHING, db_column='ItemID')  # Field name made lowercase.
    types = models.CharField(db_column='Type', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Category'
        unique_together = (('itemid', 'types'),)


class Customer(models.Model):
    userid = models.IntegerField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='Firstname', max_length=20)  # Field name made lowercase.
    lastname = models.CharField(db_column='Lastname', max_length=20)  # Field name made lowercase.
    emailaddress = models.CharField(db_column='EmailAddress', unique=True, max_length=50)  # Field name made lowercase.
    shipaddress = models.CharField(db_column='ShipAddress', max_length=100)  # Field name made lowercase.
    hashpassword = models.CharField(db_column='HashPassword', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Customer'

class Shoppingcart(models.Model):
    increment_id = models.IntegerField(db_column='increment_id', primary_key=True)
    userid = models.ForeignKey(Customer, models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    itemid = models.ForeignKey(Item, models.DO_NOTHING, db_column='ItemID')  # Field name made lowercase.
    price = models.FloatField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ShoppingCart'
        unique_together = [('userid', 'itemid'),]




class Payments(models.Model):
    paymentID=models.IntegerField(db_column='paymentID', primary_key=True)
    userid = models.ForeignKey(Customer, models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    cardnum = models.CharField(db_column='Cardnum',max_length=100)  # Field name made lowercase.
    expiration = models.CharField(db_column='Expiration', max_length=5, blank=True, null=True)  # Field name made lowercase.
    billingaddress = models.CharField(db_column='BillingAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='ZipCode', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Payments'
        unique_together = (('userid', 'cardnum'),)




class Orders(models.Model):
    orderid = models.IntegerField(db_column='OrderId', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Customer', models.DO_NOTHING, related_name='userid_set',db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    totalprice = models.FloatField(db_column='TotalPrice', blank=True, null=True)  # Field name made lowercase.
    dates = models.CharField(db_column='Dates', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cardnum = models.CharField(db_column='Cardnum',max_length=100, blank=True, null=True)  # Field name made lowercase.
    shipaddress = models.CharField(db_column='ShipAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
    shippingfee = models.FloatField(db_column='ShippingFee', blank=True, null=True)  # Field name made lowercase.
    taxes = models.FloatField(db_column='Taxes', blank=True, null=True)  # Field name made lowercase.
    shippedtype = models.IntegerField(db_column='ShippedType', blank=True, null=True)  # Field name made lowercase.
    
    class Meta:
        managed = False
        db_table = 'Orders'




class Orderitem(models.Model):
    orderitemid = models.IntegerField(db_column='Orderitemid', primary_key=True)
    orderid = models.ForeignKey('Orders', models.DO_NOTHING, db_column='OrderId')  # Field name made lowercase.
    itemid = models.ForeignKey(Item, models.DO_NOTHING, db_column='ItemId')  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=200, blank=True, null=True)  # Field name made lowercase.
    condit = models.CharField(db_column='Condit', max_length=10, blank=True, null=True)  # Field name made lowercase.
    trackingnum = models.CharField(db_column='Trackingnum', max_length=50, blank=True, null=True)
    DeliveryDay = models.CharField(db_column='DeliverredDay', max_length=100, blank=True, null=True)
    DeliveryStatus = models.CharField(db_column='DeliverredStatus', max_length=100, blank=True, null=True)
    DeliveryCompany = models.CharField(db_column='DeliveryCompany', max_length=100, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'OrderItem'
        


class Delivery(models.Model):
    orderid = models.ForeignKey('Orders', models.DO_NOTHING, db_column='OrderId', blank=True, null=True)  # Field name made lowercase.
    itemid = models.ForeignKey('Item', models.DO_NOTHING, db_column='ItemId', primary_key=True)  # Field name made lowercase.
    trackingnum = models.IntegerField(db_column='TrackingNum')  # Field name made lowercase.
    deliverredday = models.CharField(db_column='DeliverredDay', max_length=8, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    company = models.CharField(db_column='Company', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Delivery'
        unique_together = (('itemid', 'trackingnum'),)





class Reviews(models.Model):
    reviewid = models.IntegerField(db_column='ReviewsID', primary_key=True)
    userid = models.ForeignKey(Customer, models.DO_NOTHING, db_column='UserId')  # Field name made lowercase.
    itemid = models.ForeignKey(Item, models.DO_NOTHING, db_column='ItemId')  # Field name made lowercase.
    rates = models.FloatField(db_column='Rates', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=5000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Reviews'
        unique_together = (('userid', 'itemid'),)


class ReviewsSeller(models.Model):
    userid = models.ForeignKey(Customer, models.DO_NOTHING, db_column='UserId', primary_key=True)  # Field name made lowercase.
    sellerid = models.ForeignKey('Seller', models.DO_NOTHING, db_column='SellerId')  # Field name made lowercase.
    rates = models.FloatField(db_column='Rates', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Reviews_Seller'
        unique_together = (('userid', 'sellerid'),)





class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

class CurrentUser(models.Model):
    """docstring for CurrentUser"""
    userid = models.ForeignKey(Customer, models.DO_NOTHING, db_column='UserId', primary_key=True)
    class Meta:
        managed = False
        db_table = 'CurrentUser'


   
class History(models.Model):
    """docstring for CurrentUser"""
    text = models.CharField(db_column='txt', max_length=100 , primary_key=True)
    class Meta:
        managed = False
        db_table = 'History'











    
        