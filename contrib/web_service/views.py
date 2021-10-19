import math
import json
import requests

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def check_is_fibonacci_number(number_of_terms):
    counter = 0
    num1 = 1
    num2 = 1
    is_fibonacci = False

    if number_of_terms == 0 or number_of_terms == 1:
        is_fibonacci = True
    else:
        while counter < number_of_terms:
            counter = num1 + num2
            num2 = num1
            num1 = counter
        if counter == number_of_terms:
            is_fibonacci = True
    return is_fibonacci


def findIndex(n):
    fibo = 2.078087 * math.log(n) + 1.672276
    return round(fibo)

@csrf_exempt
def return_response(request):

    data = request.GET
    context = {}
    result = 0

    if isinstance(data, dict) and len(data) > 0:
        x = int(data.get('x', False))
        y = int(data.get('y', False))
        operation = data.get('operation')

        if operation == '+':
            result = x + y
        elif operation == '-':
            result = x - y
        elif operation == '*':
            result = x * y
        elif operation == '/':
            result = x / y

    context.update({
        'result': result,
        'is_fibonacci': check_is_fibonacci_number(result),
        'counter': findIndex(result),
    })

    json_content = json.dumps(context).encode('utf-8')
    return HttpResponse(json_content, 'application/json; charset=utf-8')
