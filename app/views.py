from django.shortcuts import HttpResponse
from .tasks import test_func


def test (request) :
    test_func.delay()
    return HttpResponse('Done')
