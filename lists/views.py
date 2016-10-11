from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
# 在这儿编写视图
@csrf_exempt
def home_page(request):
#     if request.method == 'POST':
#         return HttpResponse(request.POST['item_text'])
    return render(request, 'home.html',{
        'new_item_text': request.POST.get('item_text', ''),
    })
