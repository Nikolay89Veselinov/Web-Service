import json
import requests

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def test(request):

    data = request.GET
    result = []
    numbers = []

    if data != {}:
        for k in data: 
            numbers.append(data[k])

        x = int(numbers[0])
        y = int(numbers[1])
        operation = numbers[2]

        if operation == '+':
            result = x + y
        elif operation == '-':
            result = x - y
        elif operation == '*':
            result = x * y
        elif operation == '/':
            result = x / y

    json_content = json.dumps(result).encode('utf-8')
    return HttpResponse(json_content, 'application/json; charset=utf-8')
