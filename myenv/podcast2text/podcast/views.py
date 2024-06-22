from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'podcast/home.html')  # This is the home page
