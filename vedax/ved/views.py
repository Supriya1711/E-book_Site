from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')


def about(request):
    return render(request,'index.html')


def contact(request):
    return render(request,'contact.html')


def blog(request):
    return render(request,'index.html')


def blog_detail(request):
    return render(request,'index.html')


def ebooks(request):
    return render(request,'ebooks.html')


def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def ads(request):
    return render(request,'ads page.html')


def listings(request):
    return render(request,'ads page.html')

def post(request):
    return render(request,'post.html')

def element(request):
    return render(request,'index.html')


def courses(request):
    return render(request,'index.html')