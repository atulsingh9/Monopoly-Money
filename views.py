from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST["name"]
        room_id = request.POST["create_room"]
        join_room_id = request.POST["join_room"]

        


        
        

    return render(request, "monopoly_money/index.html")

def dashboard(request):
    return render(request, "monopoly_money/dashboard.html")
