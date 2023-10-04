# django
from django.http import HttpResponse, JsonResponse

# utils
from datetime import datetime 
import json

def hello_word(request):
    """ Return a greeting"""
    import pdb; pdb.set_trace()
    return HttpResponse('Oh hi, current server time is {now} '.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')))

def sorted(request):
    """ Hi """
    numbers = request.GET['numbers'].split(',')
    numbers_sorted = [int(i) for i in numbers]
    data = {
        'status':'ok',
        'numbers': numbers_sorted,
        'message': 'Integer sorted correctly'
    }
    return HttpResponse(
        json.dumps(data, indent=4), 
        content_type='application/json')

def say_hi(request, name, age):
    """Return a greeting"""
    if age < 12:
        message = 'Sorry {}, you are not allower here'. format(name)
    else:
        message = 'Hello {}, welcome to platzigram'.format(name)
    
    return HttpResponse(
        message
    )
    