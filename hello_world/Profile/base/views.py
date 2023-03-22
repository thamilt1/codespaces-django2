from django.shortcuts import render
  
def home(request):
    return render(request, "home.html")
  
def projects(request):
    return render(request, "projects.html")
  
def contact(request):
    return render(request, "contact.html")
# Create your views here.

					# create a function
def geeks_view(request):
    # create a dictionary
    context = {
        "data" : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    }
    # return response
    return render(request, "geeks.html", context)