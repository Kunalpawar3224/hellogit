from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    context = {
        'employee_name': "kunal",
        'employee_name2': "Harbhajan"
    }
    return render(request, 'index.html', context)
    #return HttpResponse("this is home page")

def about(request):
    return render(request, 'about.html')
       

def services(request):
    return render(request, 'services.html')

def contacts(request):
    return render(request, 'contacts.html')     
