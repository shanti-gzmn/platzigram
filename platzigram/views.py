# django
from django.http import HttpResponse, JsonResponse

# utils
from datetime import datetime 

def hello_word(request):
    """ Return a greeting"""
    import pdb; pdb.set_trace()
    return HttpResponse('Oh hi, current server time is {now} '.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')))

def hi(request):
    """ Hi """
    numbers = request.GET['numbers'].split(',')
    numbers = [int(i) for i in numbers]
    return JsonResponse({
        'numbers': sorted(numbers)
    })