from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse, HttpResponseNotFound
from main.forms import ItemForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.urls import reverse
from main.models import Item
import datetime
import json

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    items = Item.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
        'class': 'PBP C',
        'items' : items,
        'total_item' : items.count,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {
        'form': form,
        'name': request.user.username,
        'class': 'PBP C',  
    }
    return render(request, "create_item.html", context)

def get_item_json(request):
    product_item = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_item))

@csrf_exempt
def add_item_ajax(request):
    if request.method == 'POST':

        name = request.POST.get("name")
        power = request.POST.get("power")
        category = request.POST.get("category")
        price = request.POST.get("price")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        user = request.user

        new_item = Item(name=name, power=power, category=category, price=price, amount=amount, description=description, user=user)
        new_item.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def add_item_amount(request, item_id):
    item = Item.objects.get(id=item_id, user=request.user)
    item.amount += 1
    item.save()

    return redirect('main:show_main')

@csrf_exempt
def add_amount_ajax(request):
    if request.method == 'PATCH':
        pk = json.loads(request.body).get('pk')
        item = Item.objects.get(pk=pk)
        item.amount += 1
        item.save()
        return HttpResponse(b"ADDED", 201)
    
    return HttpResponseNotFound

def dec_item_amount(request, item_id):
    item = Item.objects.get(id=item_id, user=request.user)
    if (item.amount == 1):
        item.delete()
    else:
        item.amount -= 1
        item.save()
        
    return redirect('main:show_main')

@csrf_exempt
def dec_amount_ajax(request):
    if request.method == 'PATCH':
        pk = json.loads(request.body).get('pk')
        item = Item.objects.get(pk=pk)
        item.amount -= 1
        item.save()
        return HttpResponse(b"ADDED", 201)
    
    return HttpResponseNotFound

def remove_item(request, item_id):
    item = Item.objects.get(id=item_id, user=request.user)
    item.delete()

    return redirect('main:show_main')

@csrf_exempt
def remove_item_ajax(request):
    if request.method == 'DELETE':
        pk = json.loads(request.body).get('pk')
        item = Item.objects.get(pk=pk)
        item.delete()
        return HttpResponse(b"DELETED", 201)
    
    return HttpResponseNotFound()

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Item.objects.create(
            user = request.user,
            name = data["name"],
            power = int(data["power"]),
            price = int(data["price"]),
            amount = int(data["amount"]),
            description = data["category"],
            description = data["description"],
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)