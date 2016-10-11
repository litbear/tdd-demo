from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from lists.models import Item


# Create your views here.
# 在这儿编写视图
@csrf_exempt
def home_page(request):
              
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/') 
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
