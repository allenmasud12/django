from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    text = {'name': 'Allen Masud', 'work': 'He is a android app developer'}
    return render(request, 'index.html', text)
    
def add(request):
    value1 = int(request.POST['num1'])
    value2 = int(request.POST['num2'])
    values = value1 + value2
    values1 = value1 - value2
    values2 = value1 * value2
    values3 = value1 / value2
    values4 = value1 % value2
    values5 = value1 ** value2
    values6 = value1 // value2
    return render(request, 'result.html', {'result': values, 'result1':values1, 'result2':values2, 'result3':values3, 'result4':values4, 'result5':values5, 'result6':values6})
