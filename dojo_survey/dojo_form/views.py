from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def result(request):
   name = request.POST["name"]
   location = request.POST["location"]
   language = request.POST["language"]
   context={
       'name': name,
       'location': location,
       'language': language
   }
   return render(request, "result.html", context)