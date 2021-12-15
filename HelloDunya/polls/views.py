from django.http import HttpResponse

def index(request):
    return HttpResponse("""
    Hello, Dunya.
    This is Milestone 1 Group 3
Muhammad Fikri Kamiil Azhari A18KE0318
Muhammad Hadhari Koko Hermaja A18KE0319
Rifat Rachim Khatami Fasha A18KE0325""")

# Create your views here.
