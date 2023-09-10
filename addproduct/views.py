from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import AddProductForm
# Create your views here.
def add_product(request):
    if request.method == "POST":
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user  # Assign the current user to the product
            myform.save()
            return redirect('shop')  # Redirect to the product list page after adding the product
    else:
        form = AddProductForm()

    return render(request, 'shop/add_product.html', {'form': form})