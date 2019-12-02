import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def action_AB(request, *args, **kwargs):
    if request.method == 'POST':
        if request.body:
            data = None
            if request.body:
                data = json.loads(request.body)
                try:
                    a = int(data['A'])
                    b = int(data['B'])
                    return act_numbers(request, a, b)
                except ValueError:
                    return error('data are not numbers!')

        else:
            return error('No data provided!')

        # data are not numbers!


def error(text):
    response = JsonResponse({'error': text})
    response.status_code = 400
    return response


def add_numbers(a, b):

    answer = {
        'answer': a + b
    }
    return JsonResponse(answer)


def subtract_numbers(a, b):
    answer = {
        'answer': a - b
    }
    return JsonResponse(answer)


def multiply_numbers(a, b):
    answer = {
        'answer': a * b
    }
    return JsonResponse(answer)


def divide_numbers(a, b):
    if b != 0:
        answer = {
            'answer': a / b
        }
        return JsonResponse(answer)
    else:
        return error('Division by zero!')


def act_numbers(request, a, b):
    if request.path.endswith('add/'):
        return add_numbers(a, b)
    elif request.path.endswith('subtract/'):
        return subtract_numbers(a, b)
    elif request.path.endswith('multiply/'):
        return multiply_numbers(a, b)
    elif request.path.endswith('divide/'):
        return divide_numbers(a, b)