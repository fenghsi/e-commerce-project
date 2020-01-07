"""CSE305Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from pages.views import home
from pages.views import about
from pages.views import item_view
from pages.views import item_search_view
from pages.views import login_view
from pages.views import *
from django.conf import settings
from django.conf.urls.static import static
app_name='pages'
urlpatterns = [

    path('base/', home,name='home'),
    path('about/', about,name='about'),
    path('item/', item_view,name='item_view'),
    path('admin/', admin.site.urls),
    path('item_search/', item_search_view,name='item_search_view'),
    path('login/', login_view,name='login_view'),
    path('home/', home_page,name='homes'),
    path('cart/', shopping_cart,name='cart'),
    path('Order_view/', Order_view,name='Order_view'),
    path('register_account/', register_account,name='register_account'),
    path('Comfirmation_order/', continue_to_checkout,name='Comfirmation_order'),
    path('thank_register/', thank_register,name='thank_register'),
    path('thank_seller_register/', thank_seller_register,name='thank_seller_register'),
    path('Proceed_to_check_out/', Proceed_to_check_out,name='Proceed_to_check_out'),
    path('seller_register_account/', seller_register_account,name='seller_register_account'),
    path('posted_item/', posted_item,name='posted_item'),
    path('sell_item_view/', sell_item_view,name='sell_item_view'),
    path('top_seller_view/', top_seller_view,name='top_seller_view'),
    url(r'^item_search_view_by_category/(?P<types>[-\w]+)/$', item_search_view_by_category,name='item_search_view_by_category'),
    url(r'^add_to_cart/(?P<itemid>[-\w]+)/$',add_to_cart,name="add_to_cart"),
    url(r'^add_to_cart2/(?P<itemid>[-\w]+)/$',add_to_cart2,name="add_to_cart2"),
    url(r'^increase_item/(?P<itemid>[-\w]+)/$',increase_item,name="increase_item"),
    url(r'^decrease_item/(?P<itemid>[-\w]+)/$',decrease_item,name="decrease_item"),
    url(r'^Item_details_view/(?P<itemid>[-\w]+)/$',Item_details_view,name="Item_details_view"),
    url(r'^Order_details_view/(?P<orderid>[-\w]+)/$',Order_details_view,name="Order_details_view"),
    url(r'^rate_item/(?P<itemid>[-\w]+)/$',rate_item,name="rate_item"),
    url(r'^rate_item_finsih/(?P<itemid>[-\w]+)/$',rate_item_finsih,name="rate_item_finsih"),
    url(r'^top_seller_pages/(?P<sellerid>[-\w]+)/$',top_seller_pages,name="top_seller_pages"),
    url(r'^add_to_cart_detail/(?P<itemid>[-\w]+)/$',add_to_cart_detail,name="add_to_cart_detail"),
    url(r'^return_item/(?P<itemid>[-\w]+)/(?P<orderid>[-\w]+)/$',return_item,name="return_item")
    
    
   
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
