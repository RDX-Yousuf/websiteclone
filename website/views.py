from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def courses(request):
    return render(request, 'courses.html')

def course_detail(request,data):
    return render(request, 'course_detail.html',{'data':data})

def Bootcamp(request):
    return render (request,'Bootcamp.html')


def signin(request):
    return render (request,'signin.html')