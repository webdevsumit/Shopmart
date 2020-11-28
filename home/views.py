from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.



def searchEngine(path):
    lastindexForProduct = len(path)+5
    searchItem = ''
    for i in path:
        if not i in ['a','e','i','o','u']:
            searchItem+=i
    searchItem=searchItem.upper()
    AllProducts = list(product.objects.all())
    filteredProduct=[]
    for searching_product in AllProducts:
        search_product=searching_product.Name.upper()
        putIt = True
        firstindex = 0
        lastindex = 7
        if len(searchItem)<lastindex:
            lastindex=len(searchItem)+1
        for PathLetter in searchItem[:lastindex]:
            if PathLetter in search_product[firstindex:lastindexForProduct]:
                firstindex = search_product.index(PathLetter)
            else:
                putIt = False
        if putIt:
            filteredProduct.append(searching_product)
    return list(filteredProduct)




def home(request):
    Carts = list(cartitem.objects.filter(Username=request.user.username))
    CartItemName = ""
    for item in Carts:
        CartItemName+=item.Product+','
    try:
        trendvideo = list(videos.objects.filter(Trending=True))[0]
    except:
        trendvideo = None
    try:
        favoriteview = list(favorite.objects.get(Username=request.user.username).FavItems.all())
    except:
        favoriteview = list(product.objects.all())
    if len(favoriteview)>7:
        favoriteview = favoriteview[-7:]
    context = {
            'trendvideo':trendvideo,
            'productview':list(product.objects.filter(onHomeScreen=True)),
            'favoriteview':favoriteview,
            'dealAdd':list(product.objects.order_by('Rating'))[-1],
            'Carts':Carts,
            'CartsProductName':CartItemName,
            'catagories':list(catagory.objects.filter(onHomeScreen=True))
        }
    if "already_login" in request.session:
        context['logined']=True
        context['user']=request.session.get('already_login')
        return render(request,'home.html',context)
    else:
        context['logined']=False
        return render(request,'home.html',context)

def signuphome(request):
    if request.method=='POST':
        Username = request.POST['Username']
        userdata = User.objects.filter(username=Username)
        if userdata:
            message = 'Username exist choose another one!!'
            return render(request, 'signup.html',{'message':message})
        Firstname = request.POST['Firstname']
        Lastname = request.POST['Lastname']
        Email = request.POST['Email']
        Password = request.POST['Password']
        Password1 = request.POST['Password1']
        if Password!=Password1:
            message = 'Make sure passwords are matching!!'
            return render(request, 'signup.html',{'message':message})
        else:

            user = User.objects.create_user(username=Username,first_name=Firstname,last_name=Lastname,email=Email,password=Password)
            user.save()
            user = auth.authenticate(username=Username,password=Password)
            auth.login(request,user)
            request.session['already_login']=Username
            return redirect('home')

    context = {
        'logined':False
    }
    return render(request,'home.html',context)

def loginhome(request):
    if request.method=='POST':
        Username = request.POST['Username']
        userdata = User.objects.filter(username=Username)
        if userdata:
            Password = request.POST['Password']
            user = auth.authenticate(username=Username,password=Password)
            if user is not None and user.is_active:
                auth.login(request,user)
                request.session['already_login']=Username
                return redirect('home')
            else:
                message = 'Incorrect password or user is not ative!!'
                return render(request, 'login.html',{'message':message})
        else:
            message = 'Username not exist!!'
            return render(request, 'login.html',{'message':message})
    else:
        context = {
            'logined':False
        }
        return render(request,'home.html',context)

def logouthome(request):
    auth.logout(request)
    context = {
        'logined':False
    }
    return redirect('home')

def search(request, path):
    context = {
        'logined':False,
        'searchData':'',
        'catagories':list(catagory.objects.filter(onHomeScreen=True))
    }
    if path=='fav':
        if request.user.username:
            context['searchData'] = list(favorite.objects.get(Username=request.user.username).FavItems.all())
        else:
            context['searchData'] = list(product.objects.all())

    if request.user.username:
        context['logined']=True
        searchedData = searched.objects.create(Username = request.user.username,SearchedName=path)
        searchedData.save()

    if path=='account':
        return redirect('account')
    elif path=='login':
        return redirect('login')
    elif path=='logouthome':
        return redirect('logouthome')
    elif path=='signup':
        return redirect('signup')
    elif path=='cart':
        return redirect('cart')
    else:
        return render(request,'search.html',context)

def searching(request):
    path = request.GET['searchinput']
    context = {
        'logined':False,
        'searchData':searchEngine(path),
        'catagories':list(catagory.objects.filter(onHomeScreen=True))
    }
    if request.user.username:
        context['logined']=True
        searchedData = searched.objects.create(Username = request.user.username,SearchedName=path)
        searchedData.save()
    return render(request,'search.html',context)

def description(request, path):
    if path == 'addRating':
        if request.method=='POST':
            ProductName = request.POST['product']
            path = ProductName
            if request.user.username:
                Rating = int(request.POST['Rating'])
                if Rating<=5 and Rating>=0:
                    try:        
                        data = list(product.objects.filter(Name=path))[0]       
                    except:
                        data = None
                    savingRating = list(ratings.objects.get_or_create(Username=request.user.username,Product=data))[0]
                    savingRating.Rating=Rating
                    savingRating.save()
                    rate = int(data.Rating)
                    data.Rating = (rate+Rating)/2
                    data.save()
            return redirect('/description/%s'%path)    
    if path == 'addToCart':
        if request.method=='POST':
            ProductName = request.POST['product']
            path = ProductName
            if request.user.username:
                quantity = int(request.POST['quantity'])
                savingCartItem = cartitem.objects.get_or_create(Username=request.user.username,Quantity=quantity,Product=ProductName)[0]
                data = product.objects.get(Name=ProductName)
                if data.Offer or data.SpecialOffer:
                    price = data.OfferPrice
                else:
                    price = data.Price
                savingCartItem.Price = int(price)*int(quantity)
                savingCartItem.save()
            return redirect('/description/%s'%path)
    try:        
        data = list(product.objects.filter(Name=path))[0]       
    except:
        data = None

    AddedToCart = False
    notLogined = True
    Rated = False
    try:
        checkRated = ratings.objects.get(Username=request.user.username,Product=data)
    except:
        checkRated = False
    if checkRated:
        Rated = True
    if request.user.username:
        notLogined = False
        cartdata = list(cartitem.objects.filter(Username=request.user.username))
        for item in cartdata:
            if item.Product==path:
                if not item.Ordered:
                    AddedToCart = True
        fav = favorite.objects.get_or_create(Username=request.user.username)[0]
        fav.FavItems.add(data)
        fav.save()
    context = {
        'data':data,
        'AddedToCart':AddedToCart,
        'notLogined':notLogined,
        'Rated':Rated
    }
    return render(request,'description.html',context)

def account(request):
    username = request.user.username
    userdata= User.objects.values()
    for i in userdata:
        if i['username']==username:
            userdata=i
            break
    try:
        profiledata=list(profile.objects.filter(Username=username))[0]
    except:
        profiledata=None
    context = {
        'logined':True,
        'username':userdata['username'],
        'firstname':userdata['first_name'],
        'lastname':userdata['last_name'],
        'email':userdata['email'],
        'superuser':userdata['is_superuser'],
        'userdata':userdata,
        'profiledata':profiledata,
        'searchdata':list(searched.objects.filter(Username=username)),
        'cartdata':list(carts.objects.filter(Username=username)),
        'ratingdata':list(ratings.objects.filter(Username=username)),
        'catagories':list(catagory.objects.filter(onHomeScreen=True))
    }
    return render(request,'account.html',context)

def YourOrder(request, path):
    data = carts.objects.get(id=path)
    context = {
        'data':data.Items.all()
    }
    return render(request,'YourOrder.html',context)

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')


@login_required()
def cart(request):
    Total = 0
    cartitems = list(cartitem.objects.filter(Username=request.user.username))
    for item in cartitems:
        if not item.Ordered:
            Total += item.Price

    context={
        'cartitems':cartitems,
        'Total':Total
    }
    return render(request,'cart.html',context)

def deleteFromCart(request, path):
    cartdata = cartitem.objects.filter(Username=request.user.username,Product=path)
    cartdata.delete()
    return redirect('cart')

def PaymentDone(request, path):
    cartitems = cartitem.objects.filter(Username=request.user.username,Ordered=False)
    try:
        Profile = profile.objects.get(Username=request.user.username)
        cart = carts.objects.create(Username=request.user.username,Address=Profile.Address,Phoneno=Profile.Phoneno,PaymentMethod=path)
    except:
        return redirect('edit')
    
    for item in cartitems:
        cart.Items.add(item)
        item.Ordered = True
        item.save()
    cart.save()
    return redirect('/')

@login_required()
def addToCart(request):
    if request.method=='POST':
        ProductName = request.POST['product']
        quantity = request.POST['quantity']
        print(ProductName,':',quantity)
    return redirect('cart')

def edit(request):
    username = request.user.username
    userdata= User.objects.values()
    for i in userdata:
        if i['username']==username:
            userdata=i
            break
    try:
        profiledata=list(profile.objects.filter(Username=username))[0]
    except:
        profiledata=None
    context = {
        'userdata':userdata,
        'profiledata':profiledata,
    }
    return render(request,'edit.html',context)

def editaccount(request):
        if request.method=='POST':
            profileimage = request.POST['profileimage']
            Firstname = request.POST['Firstname']
            Lastname = request.POST['Lastname']
            Email = request.POST['Email']
            Address = request.POST['Address']
            Phoneno = request.POST['Phoneno']
            
            userdata = User.objects.get(username=request.user.username)
            userdata.first_name = Firstname
            userdata.last_name = Lastname
            userdata.email = Email
            userdata.save()
            profiledata = profile.objects.get_or_create(Username=request.user.username)[0]
            profiledata.Image = profileimage
            profiledata.Address = Address
            profiledata.Phoneno = Phoneno
            profiledata.save()
        return redirect('account')


def catagories(request, path):
    try:
        productCatagory = catagory.objects.filter(Catagory=path)[0]
    except:
        productCatagory = None
    context = {
        'logined':False,
        'searchData':list(product.objects.filter(Catagory=productCatagory))
    }

    if request.user.username:
        context['logined']=True
        
    return render(request, 'search.html',context)
