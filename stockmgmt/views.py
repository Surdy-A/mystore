from django.shortcuts import render
from .models import Stock
from .forms import StockCreateForm
from django.shortcuts import render, redirect

def home(request):
	title = 'Welcome: This is the Home Page'
	context = {
	"title": title,
	}
	return render(request, "home.html",context)


def list_item(request):
	title = 'List of Items'
	queryset = Stock.objects.all()
	context = {
		"title": title,
		"queryset": queryset,
	}

	return render(request, "list_item.html", context)


def add_items(request):
	form = StockCreateForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/list_items')

	context = {
		"form": form,
		"title": "Add Item",
	}
	return render(request, "add_items.html", context)


