import json
from django.http import HttpResponse
# from restframework.decorators import api_view
# @api_view(['POST'])

def counter(request):

    s1 = {"id": 1, "value": 26,"title":"آیفون"}
    s2 = {"id": 2, "value": 123,"title":"مک بوک 2021 M1"}
    s3 = {"id": 3, "value": 5,"title":"قاب گوشی آیفون"}
    s4 = {"id": 4, "value": 2,"title":"کیف لپ تاپ"}
    s5 = {"id": 5, "value": 1,"title":"کنترل تلویزیون"}

    list = [s1, s2, s3, s4, s5]

    final = {"counters": list}
    return HttpResponse(json.dumps(final), content_type='application/json')

def test(request):

    return HttpResponse('<h1 style="color:red">Hello</h1>')