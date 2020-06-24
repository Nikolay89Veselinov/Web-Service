import json
import requests

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def return_response(request):

    data = request.GET
    result = []

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

    json_content = json.dumps(result).encode('utf-8')
    return HttpResponse(json_content, 'application/json; charset=utf-8')
