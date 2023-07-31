from django.shortcuts import render
from django.http import JsonResponse
from .models import results 

# Create your views here.
def index(request):
    return render(request, 'results/index.html')

def result(request, id):
    id = id.split(',')
    print(id)
    resultsView = []
    for seat in id:
        try :
            seat = int(seat)
            result = results.objects.get(seat_no=seat).serialize()
            resultsView.append(result)
        except :
            print(f'Error with {seat}')
    return JsonResponse({'results' : resultsView})
    