from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Steel Sword',
        'category': 'Weapon'
    }

    return render(request, "main.html", context)