

from django.shortcuts import render
from .tasks import test 
from django.http import HttpResponse

def run_test(request): 
    test.delay()  
    return HttpResponse("Done!")
