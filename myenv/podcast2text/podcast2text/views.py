from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')  # This is the home page

def aboutMe(request):
    return render(request, 'about.html')  # This is the home page
