from django.shortcuts import render
from difflib import SequenceMatcher
from .models import Item
from .models import Seller
from .models import Customer
from .models import Shoppingcart
from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import *
import datetime
import random
import string
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os





def randomString(stringLength=20):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()
# Create your views here.

def home(request, *args, **kwargs):
	CurrentUser.objects.all().delete()
	obj = Customer.objects.all();
	userName = request.POST["username"]
	password = request.POST["pass"]

	for ele in obj:
		if password == ele.hashpassword and userName == ele.emailaddress:
			Current= CurrentUser(userid=ele)
			Current.save()
			return render(request, "home.html", {"id":ele.userid})
	for ele in Seller.objects.all():
		if password == ele.hashpassword and userName == ele.emailaddress:
			
			return render(request, "home.html", {"id":ele.userid})

	return render(request, "loginpage.html", {"msg":"Incorrect Username or Password!"})

def home_page(request):
	return render(request, "home.html", {})


def about(request, *args, **kwargs):
	return render(request, "about.html", {})


def item_view(request):
	obj = Item.objects.all()
	xxx=list()
	for ele in obj:
		xxx.append(ele)

	for i in range(0, len(xxx)-1):
		for j in range(0,len(xxx)-1):
			if (xxx[j].soldnum < xxx[j+1].soldnum  ):
				xxx[j],xxx[j+1]= xxx[j+1], xxx[j]
		
	my_context ={ 
		"obj" :xxx,
		
	}
	return render(request, "item.html", my_context)


def item_search_view(request,**kwargs):
	obj = Item.objects.all()
	xxx=list()
	for ele in obj:
		xxx.append(ele)

	for i in range(0, len(xxx)-1):
		for j in range(0,len(xxx)-1):
			if (xxx[j].soldnum < xxx[j+1].soldnum  ):
				xxx[j],xxx[j+1]= xxx[j+1], xxx[j]
	obj = xxx
	txt=""
	try:
		txt= request.POST["search_text"]
		History.objects.all().delete()
		his= History(text=txt)
		his.save()
	except:
		txt = History.objects.first().text
	newobj=list()
	
	for ele in obj:
		if similar(ele.name, txt) >0.35:
			newobj.append(ele)
	num =len(newobj)
	my_context ={ 
		"obj" :newobj,
		"search":txt,
		"num" :num
	}
	return render(request, "item_search_view.html", my_context)



def login_view(request):
	return render(request, "loginpage.html", {"msg":""})


def shopping_cart(request, *args, **kwargs):
	obj= Shoppingcart.objects.all()
	cuser = CurrentUser.objects.first()
	newobj=list()
	items = list()
	for ele in obj:
		if cuser.userid == ele.userid:
			newobj.append(ele)
	for ele in newobj:
		itemsinfo = Item.objects.filter(itemid = str(ele.itemid.itemid)).first()
		items.append(itemsinfo)
		print("ok "+str(itemsinfo.itemid))
	sum = 0
	for ele in obj:
		if cuser.userid == ele.userid: 
			sum+= ele.price

	return render(request, "shoppingcart.html", { 'items': newobj , 'newitem':items, 'total':sum})

def add_to_cart(request,**kwargs):
	product= Item.objects.filter(itemid=kwargs.get("itemid","")).first()
	Current=CurrentUser.objects.first().userid.userid
	
	cus = Customer.objects.filter(userid=str(Current)).first()
	for ele in Shoppingcart.objects.all():
	
		if Current==ele.userid.userid and product.itemid == ele.itemid.itemid:
			xx= ele.quantity+1
			ele.quantity+=1
			ele.price = xx*product.price
			ele.save()
			return redirect(reverse('item_view'))
	newitem = Shoppingcart(increment_id=len(Shoppingcart.objects.all())+1,userid=cus,itemid=product,price=product.price,quantity =1)
	newitem.save()
	return redirect(reverse('item_view'))
	

def add_to_cart2(request,**kwargs):
	product= Item.objects.filter(itemid=kwargs.get("itemid","")).first()
	Current=CurrentUser.objects.first().userid.userid
	
	cus = Customer.objects.filter(userid=str(Current)).first()
	for ele in Shoppingcart.objects.all():
		if Current==ele.userid.userid and product.itemid == ele.itemid.itemid:
			xx= ele.quantity+1
			ele.quantity+=1
			ele.price = xx*product.price
			ele.save()
			return redirect(reverse('item_search_view'))
	newitem = Shoppingcart(increment_id=len(Shoppingcart.objects.all())+1, userid=cus,itemid=product,price=product.price,quantity =1)
	newitem.save()
	return redirect(reverse('item_search_view'))


def increase_item(request,**kwargs):
	Current=CurrentUser.objects.first().userid.userid
	product= Item.objects.filter(itemid=kwargs.get("itemid","")).first()
	for ele in Shoppingcart.objects.all():
		if Current==ele.userid.userid and product.itemid == ele.itemid.itemid:
			xx= ele.quantity+1
			ele.quantity+=1
			ele.price = xx*product.price
			ele.save()
			

	return redirect(reverse('cart'))




def decrease_item(request,**kwargs):
	Current=CurrentUser.objects.first().userid.userid
	product= Item.objects.filter(itemid=kwargs.get("itemid","")).first()
	for ele in Shoppingcart.objects.all():
		if Current==ele.userid.userid and product.itemid == ele.itemid.itemid:
			xx= ele.quantity-1
			ele.quantity-=1
			ele.price = xx*product.price
			ele.save()
			if ele.quantity==0:
				ele.delete()
			
	
	return redirect(reverse('cart'))


def Proceed_to_check_out(request,**kwargs):
	Current=CurrentUser.objects.first().userid.userid
	shoppingcart = Shoppingcart.objects.filter(userid=Current)
	items = list()
	totalprice =0
	for ele in shoppingcart:
		print(ele.itemid.itemid)
		item=Item.objects.filter(itemid=ele.itemid.itemid).first()
		items.append(item)
		totalprice += item.price*ele.quantity


	return render(request, "Proceed_to_checkout.html", {"shoppingcart":shoppingcart, "items":items, "totalprice":totalprice})

def continue_to_checkout(request,**kwargs):
	if True:
		fullname= request.POST["firstname"]
		
		email = request.POST["email"]
		
		address = request.POST["address"]
	
		city =request.POST["city"]
		
		state = request.POST["state"]
	
		zips= request.POST["zip"]
	
		cardname =request.POST["cardname"]

		cardnum =request.POST["cardnumber"]
	
		expmon = request.POST["expmonth"]
	
		expyear =request.POST["expyear"]
	
		cvv =request.POST["cvv"]

		#afa
		if(fullname=='' or email=='' or address=='' or city == '' or state=='' or zips=='' or cardnum == '' or cardname=='' or expmon=='' or expyear=='' or cvv==''):
			return redirect(reverse('Proceed_to_check_out'))
		
	
		Current=CurrentUser.objects.first().userid.userid
		customer = Customer.objects.filter(userid=Current).first()
		if len(Payments.objects.filter(userid=Current,cardnum=str(cardnum)))==0:
			payment_object = Payments(paymentID=len(Payments.objects.all())+1, userid=customer,cardnum=str(cardnum),expiration=str(expmon)+"/"+str(expyear),billingaddress=str(address)+" "+str(city)+" "+str(state),zipcode=zips)
			payment_object.save()


		payment = Payments.objects.filter(userid=Current,cardnum=cardnum).first()
		orderid = len(Orders.objects.all())+1
		#create order first
		dates = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
		totalprice=0
		for ele in Shoppingcart.objects.filter(userid=Current):
			totalprice+=ele.price
		
		orders = Orders(orderid=orderid,userid =customer,totalprice=totalprice,dates=dates,cardnum=cardnum,shipaddress=str(address)+" "+str(city)+" "+str(state),shippingfee=0,taxes=0.1,shippedtype=1)
		orders.save()

		#oditem
		for ele in Shoppingcart.objects.filter(userid=Current):
			itemid=ele.itemid
			price =ele.price
			quantity =ele.quantity
			orderitemid= len(Orderitem.objects.all())+1
			name = Item.objects.filter(itemid=itemid.itemid).first().name
			des = Item.objects.filter(itemid=itemid.itemid).first().description
			orderitems =  Orderitem(orderitemid=orderitemid, orderid=Orders.objects.filter(orderid=orderid).first(),itemid=itemid,price=price,quantity=quantity,name=name,description=des,trackingnum=randomString())
			orderitems.save()

			newitemsss= Item.objects.filter(itemid=itemid.itemid).first()
			newitemsss.soldnum+=quantity
			newitemsss.save()
		
		
		#delete shopping cart
		Shoppingcart.objects.filter(userid=Current).delete()



		return render(request, "Confirmation_order.html", {"msg":orderid})
	else:
		
		return redirect(reverse('Proceed_to_check_out'))


def Order_view(request,**kwargs):
	Current=CurrentUser.objects.first().userid.userid
	orders = Orders.objects.filter(userid=Current)
	order = list()
	for i in range(len(orders)-1, -1,-1):
		order.append(orders[i])

	orderitem=list()
	items = Item.objects.all()
	for ele in Orderitem.objects.all():
		for od in order:
			if ele.orderid.orderid == od.orderid:
				orderitem.append(ele)
	review = Reviews.objects.filter(userid=Current)
	reviews = list()
	for ele in orderitem:
		reviews.append(ele)

	for item in orderitem:
		for ele in review:
			if item.itemid.itemid == ele.itemid.itemid:
				reviews.remove(item)
	for ele in reviews:
		for ele2 in reviews:
			if ele.itemid.itemid==ele2.itemid.itemid and ele.orderitemid!=ele2.orderitemid:
				reviews.remove(ele2)

	return render(request, "orders.html", {"order":order, "orderitem":orderitem, "items":items,"review":reviews})




def Item_details_view(request,**kwargs):
	product= Item.objects.filter(itemid=kwargs.get("itemid","")).first()
	reviews=Reviews.objects.filter(itemid=product.itemid)
	users= list()
	for ele in reviews:
		x= Customer.objects.filter(userid=ele.userid.userid).first()
		users.append(x)
	print("defghnjmk,xdcfvgbhnjmk,dfgthyjukil")
	return render(request, "item_details.html", {"item":product, "reviews":reviews, "users":users})







def Order_details_view(request,**kwargs):
	order= Orders.objects.filter(orderid=kwargs.get("orderid","")).first()
	payment = Payments.objects.filter(userid=order.userid.userid,cardnum=order.cardnum).first()

	x = payment.cardnum[len(payment.cardnum)-4:len(payment.cardnum)]

	Current=CurrentUser.objects.first().userid.userid
	orders = Orders.objects.filter(userid=Current)
	orderss = list()
	for i in range(len(orders)-1, -1,-1):
		orderss.append(orders[i])

	orderitem=list()
	items = Item.objects.all()
	for ele in Orderitem.objects.all():
		for od in orderss:
			if ele.orderid.orderid == od.orderid:
				orderitem.append(ele)
	taxes = round(order.totalprice * 0.0875,2)

	return render(request, "order_details.html", {"order":order, "payment":x,"orderss":orderss, "orderitem":orderitem, "items":items , "taxes":taxes ,'aftertaxes':(taxes +order.totalprice)})




def register_account(request,**kwargs):

	return render(request, "cus_register_page.html", {})







def thank_register(request,**kwargs):
	firstname= request.POST["FirstName_reg"]
	lastname = request.POST["LastName_reg"]
	email = request.POST["Email_reg"]		
	address1 = request.POST["Address_reg"]
	password =request.POST["Password_reg"]
	re_password = request.POST["re_Password_reg"]
	address2 = request.POST["Address2_reg"]
	if(firstname == '' or lastname=='' or email=='' or address1=='' or password=='' or address2=='' or re_password=='' or re_password!=password):
		return redirect(reverse('register_account'))
	for ele in Customer.objects.all():
		if ele.emailaddress == email:
			return redirect(reverse('register_account'))
	customer= Customer(userid=len(Customer.objects.all())+1,shipaddress=address1+' '+address2,firstname=firstname,lastname=lastname,emailaddress=email,hashpassword =password)
	customer.save()


	return render(request, "thank_register.html", {})

		
def seller_register_account(request,**kwargs):
	

	return render(request, "seller_register_page.html", {})


def thank_seller_register(request,**kwargs):
	firstname= request.POST["seller_FirstName_reg"]
	lastname = request.POST["seller_LastName_reg"]
	email = request.POST["seller_Email_reg"]
	password =request.POST["seller_Password_reg"]
	re_password = request.POST["seller_re_Password_reg"]
	storename= request.POST["seller_store"]
	if(firstname == '' or lastname=='' or email==''  or password=='' or storename=='' or password!=re_password):
		return redirect(reverse('seller_register_account'))

	for ele in Seller.objects.all():
		if ele.emailaddress == email:
			return redirect(reverse('seller_register_account'))


	seller = Seller(rates=0,sellerid= len(Seller.objects.all()),storename = storename, status=1,firstname = firstname,lastname =lastname , emailaddress=email,hashpassword=password)
	seller.save()
	return render(request, "thank_register.html", {})





def sell_item_view(request,**kwargs):

	return render(request, "sell_item_view.html", {'msg':""})






def posted_item(request,**kwargs):


	email =request.POST.get("email_post_item")
	password =request.POST.get("password_post_item")
	name =request.POST.get("item_sell_name")
	price=request.POST.get("item_sell_price")
	stock=request.POST.get("item_sell_stock")
	des =request.POST.get("item_sell_des")
	condit =request.POST.get("item_sell_condit")
	myfile = request.FILES.get('myFile')
	some_var = request.POST.getlist('checks')

	
	if (name=='' or price=='' or stock=='' or des == '' or condit == '' or myfile == '' or len(some_var)==0):
		return render(request, "sell_item_view.html", {'msg2':"Please fill in all the boxes!!"})

	for ele in Seller.objects.all():
		if ele.emailaddress== email and ele.hashpassword ==password:
			fs = FileSystemStorage()
			filename = fs.save(str(len(Item.objects.all())+1)+myfile.name, myfile)
			item = Item(itemid=len(Item.objects.all())+1, price=price,rates =0,stock = stock,sellerid=Seller.objects.filter(hashpassword=password, emailaddress=email).first(),name=name,description=des,condit=condit,status=1,image="images/"+str(len(Item.objects.all())+1)+str(myfile.name),soldnum=0)
			item.save()
			for ele in some_var:
				xxxxx=Category(categoryid=len(Category.objects.all())+1, itemid=Item.objects.filter(itemid= len(Item.objects.all())).first(), types=ele)
				xxxxx.save()
			return render(request, "thank_post_item.html", {})
	

	return render(request, "sell_item_view.html", {'msg':"Invalid userName or password"})



def rate_item(request,**kwargs):
	item=Item.objects.filter(itemid=kwargs.get("itemid","")).first()

	return render(request, "rate_item.html", {"item":item})





def rate_item_finsih(request,**kwargs):
	Current=CurrentUser.objects.first().userid.userid
	description =request.POST.get("rate_item_des")
	rates =request.POST.get("rate_item_num")
	item=Item.objects.filter(itemid=kwargs.get("itemid","")).first()
	customer=Customer.objects.filter(userid=Current).first()
	review = Reviews(reviewid=len(Reviews.objects.all())+1,userid=customer,itemid=item,rates=rates,description=description)
	review.save()
	return render(request, "thank_rate_item.html", {})





def top_seller_view(request,**kwargs):
	seller = Seller.objects.all()

	x = list()

	for ele in seller:
		x.append(ele)

	for i in range(0, len(x)-1):
		for j in range(0,len(x)-1):
			totalsold_i = 0
			totalsold_j = 0
			item_i = Item.objects.filter(sellerid = x[j])
			item_j = Item.objects.filter(sellerid = x[j+1]) 
			for ele in item_i:
				totalsold_i+= ele.soldnum
			for ele in item_j:
				totalsold_j+= ele.soldnum
			if (totalsold_i < totalsold_j ):
				x[j],x[j+1]= x[j+1], x[j]

	allitems = list()
	for ele in x:
		item = Item.objects.filter(sellerid = ele)
		allitems.append(item)

	return render(request, "top_seller.html", {"allitems":allitems, "sellers":x})


def top_seller_pages(request,**kwargs):
	seller = Seller.objects.filter(	sellerid=kwargs.get("sellerid","")).first()
	items = Item.objects.filter(sellerid=seller)

	return render(request, "top_seller_pages.html", {"seller":seller, "items":items})



def add_to_cart_detail(request,**kwargs):
	product= Item.objects.filter(itemid=kwargs.get("itemid","")).first()
	Current=CurrentUser.objects.first().userid.userid
	cus = Customer.objects.filter(userid=str(Current)).first()
	for ele in Shoppingcart.objects.all():
		print("sxdcfvgbhnjmkxdcfvgbhnjmk,ldcfvgbhnj")
		if Current==ele.userid.userid and product.itemid == ele.itemid.itemid:
			xx= ele.quantity+1
			ele.quantity+=1
			ele.price = xx*product.price
			ele.save()
			return render(request, "thank_add_to_cart.html", {})
	newitem = Shoppingcart(increment_id=len(Shoppingcart.objects.all())+1,userid=cus,itemid=product,price=product.price,quantity =1)
	newitem.save()
	print("defghnjmk,xdcfvgbhnjmk,dfgthyjukil")
	return render(request, "thank_add_to_cart.html", {})



def return_item(request,**kwargs):
	print("?davghdadhajda")
	od=Orders.objects.filter(orderid=0).first()
	xx=Orderitem.objects.filter(orderid=kwargs.get("orderid",""), itemid=kwargs.get("itemid","")).first()
	xx.orderid=od
	xx.save()
	x= Orderitem.objects.filter(orderid=kwargs.get("orderid",""))
	if len(x) ==0:
			nww=Orders.objects.filter(orderid=kwargs.get("orderid","")).first()
			nww.userid=Customer.objects.filter(userid=0).first()
			nww.save()
	item = Item.objects.filter(itemid=kwargs.get("itemid","")).first()
	item.soldnum-=1
	item.save()
	return render(request, "return_item.html", {})



def item_search_view_by_category(request,**kwargs):
	obj = Item.objects.all()
	types= kwargs.get("types","")
	xxx=list()
	for ele in obj:
		xxx.append(ele)

	for i in range(0, len(xxx)-1):
		for j in range(0,len(xxx)-1):
			if (xxx[j].soldnum < xxx[j+1].soldnum  ):
				xxx[j],xxx[j+1]= xxx[j+1], xxx[j]
	obj = xxx
	txt=types
	
	newobj=list()
	
	for ele in obj:
		for ele2 in Category.objects.all():
			if ele.itemid == ele2.itemid.itemid and types==ele2.types:
				newobj.append(ele)
	num =len(newobj)
	my_context ={ 
		"obj" :newobj,
		"search":txt,
		"num" :num
	}
	return render(request, "item_search_view_by_cate.html", my_context)



	


