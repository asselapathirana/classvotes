from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def home_page(request):
    return render(request,"home.html")

def teacher_page(request):
    if request.method == 'POST':
        print (request.POST)
        return render(request, 'vote_page.html', 
                {'id_vote_number': request.POST['id_vote_number']}
                )
    return render(request,"teacher_page.html")
