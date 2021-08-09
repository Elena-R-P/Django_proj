from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from time import gmtime, strftime

# def index(request):
#     favorite_colors = ['Red', 'Blue', 'Green']
#     context = {
#         'time': strftime("%a, %d %b %Y %I:%M %p", gmtime()),
#         'colors': favorite_colors
#     }
#     return render(request, 'index.html', context)

# def create(request):
#     if request.method == 'POST':
#         print ("*"*50)
#         print (request.POST)
#         print (request.POST['name'])
#         print (request.POST['desc'])
#         request.session['name'] = "test"
#         print ("*"*50)
#         return redirect("/")
#     else:
#         return redirect('/')


def index(request):
    return render(request, 'index.html')

def hello(request):
    return render(request, 'about.html')

def contact(request):
    staff = [
        'A',
        'B',
        'C'
    ]
    context = {
        'staff': staff
    }
    return render(request, 'contact.html', context)

def success(request):
    print('****************************')
    print(request.POST)
    name = request.POST['name']
    comment = request.POST['comment']
    context = {
        'name': name,
        'comment': comment
    }
    return render(request, 'success.html', context)
