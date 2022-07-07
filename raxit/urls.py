from django.contrib import admin
from django.urls import path , include
from raxit import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.front, name='frontdpage'),
    path('dashboard', views.dashboard, name='dashboardpage'),
    path('pages', views.pages, name='pagespage'),
    # path('pageslist',views.pageslist.as_view(),name='pagespage'),
    path('edpages(?p<id>[0-9]+)',views.editPages,name='editpage'),
    path('upppage',views.updataPage,name='updatepage'),
    path('searchpages',views.searchpages,name='searchpages'),
    path('showpagerecords',views.showpagerecords,name='showpagerecords'),



    path('contectusemail',views.contectusemail,name='contectusemail'),

    path('product', views.product, name='product'),
    path('showproductsrecords',views.showproductsrecords,name='showproductsrecords'),
    path('idproduct', views.idproduct, name='products'),
    path('products', views.addProduct, name='productspage'),
    path('addproducts', views.addProducts, name='addproductspage'),
    path('edproducts(?p<id>[0-9]+)',views.editProducts,name='editproductspage'),
    path('upproducts',views.updataProducts,name='updateproductspage'),
    path('delproducts(?p<id>[0-9]+)',views.deleteProducts,name='deleteproducts'),
    path('search',views.search,name='searchpage'),
    path('search',views.searchid,name='searchid'),

    path('techtip', views.techtip, name='techtippage'),
    path('configuration', views.configuration, name='configurationpage'),
    path('registrations', views.registration, name='registrationpage'),
    path('signup', views.handlesignup, name='handlesignup'),
    path('logins', views.logins,name='logins'),
    path('login', views.handlelogin,name='loginpage'),
    path('logout', views.handlelogout,name='logoutpage'),
    path('changepassword',views.changepassword,name='change_password'),
]