from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse('''<button><i>Hello welcome to my world</i></button><br>
                            <button>hi welocome you too my worldd</button>''')