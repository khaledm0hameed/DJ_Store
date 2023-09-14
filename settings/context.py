from .models import Company

def context(request):
    data = Company.objects.last()
    return {'data':data}