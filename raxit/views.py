from tempfile import template
from turtle import title
from xmlrpc.client import MAXINT
from django.shortcuts import get_object_or_404, render,redirect,HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages
from django.core.paginator import Paginator , EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from .models import newProduct as myProducts
from .models import pages as mypages
from .models import contectusemail as mycontectusemail
from django.template import loader
from .serializers import pagesserializers
from rest_framework.generics import ListAPIView

def contectusemail(request):
    if request.method == 'POST':
        obj = mycontectusemail()
        obj.email = request.POST['email']
        obj.save()
        return redirect('frontdpage')

# Create your views here.
def front(request):
    sel = myProducts.objects.filter(Product_status='published')
    return render(request,'usersite/front.html',{'sel':sel})

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('logins')
    return render(request,'usersite/dashboard.html')

def searchpages(request):
        query=request.GET.get('q')
        sel = mypages.objects.filter(page_title=query).values()
        template = loader.get_template('usersite/searchpage.html')
        return HttpResponse(template.render({'sel':sel},request))     

# class pageslist(ListAPIView):
#     queryset = mypages.objects.all()
#     serializer_class = pagesserializers

def showpagerecords(request):
    if request.method == "POST":
        sel = mypages.objects.all()[:int(request.POST.get("showpagerecords"))]
        return render(request,'usersite/pages.html',{'sel':sel}) 
    else:
        sel = mypages.objects.all()
        return render(request,'usersite/pages.html',{'sel':sel})

def pages(request):
    if not request.user.is_authenticated:
        return redirect('logins')
    sel1 = mypages.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(sel1, 2)
    try:
        sel = paginator.page(page)
    except PageNotAnInteger:
        sel = paginator.page(1)
    except EmptyPage:
        sel = paginator.page(paginator.num_pages)
    return render(request,'usersite/pages.html',{'sel':sel}) 
    # sel = mypages.objects.all()
    # return render(request,'usersite/pages.html',{'sel':sel})

def editPages(request,id):
    sel=get_object_or_404(mypages,id=id)
    return render(request,'usersite/edit_page.html',{'sel':sel})

def updataPage(request):
        id = request.POST['myid']
        obj = get_object_or_404(mypages,id=id)
        obj.page_title = request.POST['page_title']
        obj.page_content = request.POST['page_content']
        obj.Page_status = request.POST['Page_status']
        obj.save()
        return redirect('pagespage')

def showproductsrecords(request):
    if request.method == "POST":
        sel = myProducts.objects.all()[:int(request.POST.get("showproductsrecords"))]
        return render(request,'usersite/products.html',{'sel':sel})
    else:
        sel = myProducts.objects.all()
        return render(request,'usersite/products.html',{'sel':sel})

def product(request):
    if not request.user.is_authenticated:
        return redirect('login')
    sel1 = myProducts.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(sel1, 3)
    try:
        sel = paginator.page(page)
    except PageNotAnInteger:
        sel = paginator.page(1)
    except EmptyPage:
        sel = paginator.page(paginator.num_pages)
    return render(request,'usersite/products.html',{'sel':sel}) 

def idproduct(request):
    if not request.user.is_authenticated:
        return redirect('login')
    query=request.GET.get('q')
    sel = myProducts.objects.filter(id=query).values()
    
    return render(request,'usersite/products.html',{'sel':sel}) 
    
def search(request):
        query=request.GET.get('q')
        sel = myProducts.objects.filter(product_name=query).values()
        return render(request,'usersite/search.html',{'sel':sel}) 

        # template = loader.get_template('usersite/search.html')
        # return HttpResponse(template.render({'sel':sel},request)) 

def searchid(request):
        query=request.GET.get('myid')
        sel = myProducts.objects.get(pk=query)
        template = loader.get_template('usersite/searchid.html')
        return HttpResponse(template.render({'sel':sel},request)) 


def addProduct(request):
    if not request.user.is_authenticated:
        return redirect('logins')
    return render(request,'usersite/add_products.html')

def addProducts(request):
    if request.method == 'POST':
        obj = myProducts()
        obj.product_name = request.POST['product_name']
        obj.product_disc = request.POST['product_disc']
        obj.youtube_link = request.POST['youtube_link']
        obj.Product_status = request.POST['Product_status']
        obj.save()
        return redirect('product')
    else:
        return HttpResponse('404 - Not Found')

def editProducts(request,id):
    sel=get_object_or_404(myProducts,id=id)
    return render(request,'usersite/edit_products.html',{'sel':sel}) 

def updataProducts(request):
        id = request.POST['myid']
        obj = get_object_or_404(myProducts,id=id)
        obj.product_name = request.POST['product_name']
        obj.product_disc = request.POST['product_disc']
        obj.youtube_link = request.POST['youtube_link']
        obj.Product_status = request.POST['Product_status']
        obj.save()
        return redirect('product')

def deleteProducts(request,id):
    sel=get_object_or_404(myProducts,id=id)
    sel.delete()
    return redirect('product')

def techtip(request):
    if not request.user.is_authenticated:
        return redirect('logins')
    return render(request,'usersite/tech_tip.html')

def configuration(request):
    if not request.user.is_authenticated:
        return redirect('logins')
    return render(request,'usersite/change_password.html')

def registration(request):
    return render(request,'registration/registrations.html')

def logins(request):
    return render(request,'registration/login.html')
    
def handlesignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 != pass2 :
            msg="Passwords do not match"
            return render(request,'registration/registrations.html',{'msg':msg})

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        msg="Your account has been successfully created"
        return render(request,'registration/login.html',{'msg':msg})

    else:
        return HttpResponse('404 - Not Found')


def handlelogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername,password=loginpassword)

        if user is not None:
            login(request, user) 
            msg="Successfully Logged In"
            return render(request,'usersite/dashboard.html',{'msg':msg})
        else:
            msg="Invalid detail, Please try again"
            return render(request,'registration/login.html',{'msg':msg})
    else:
        return HttpResponse('404 - Not Found')

def changepassword(request):
    if request.method == 'POST':
       pass1 = request.POST.get('pass1')
       npass1 = request.POST.get('npass1')

       user = User.objects.get(id=request.user.id)
       check =user.check_password(pass1)
       if check==True:
            user.set_password(npass1)
            user.save()
            msg = "Your password was successfully updated!"
            return render(request,'registration/login.html',{'msg':msg})

       else:
            msg="Old Passwords do not match"
            return render(request,'usersite/change_password.html',{'msg':msg})
    else:
        return HttpResponse('404 - Not Found')

def handlelogout(request):
    logout(request)
    return render(request,'registration/logout.html')



