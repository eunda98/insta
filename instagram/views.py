import numbers
from django.http import HttpResponse
import json

def hi(request):
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sortd_ints= sorted(numbers)
    data={
        'status': 'ok',
        'numbers':sortd_ints,
        'message': 'integers sorted successfully'
    }
    return HttpResponse( json.dumps(data), content_type='application/json')