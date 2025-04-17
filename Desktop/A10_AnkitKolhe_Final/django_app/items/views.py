from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm

def home(request):
    items = Item.objects.all().order_by('-created_at')
    
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ItemForm()
    
    return render(request, 'items/home.html', {'items': items, 'form': form})