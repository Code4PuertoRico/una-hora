from django.shortcuts import render

# Create your views here.
def search_page(request):
    print("hola")
    return render(request,"./search/search_page.html")