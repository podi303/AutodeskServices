from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, ResType
from .forms import ItemForm


def detail(request, id):
    item = get_object_or_404(Item, pk=id)
    return render(request, "items/detail.html", {"item": item})


def type_pg(request):
    return render(request, "items/types.html", {"type": ResType.objects.all()})


def add_new_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = ItemForm()
    return render(request, 'items/new_item.html', {"form": form})


