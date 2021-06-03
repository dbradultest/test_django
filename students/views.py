from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from webargs.djangoparser import use_kwargs




def hello(request):
    return HttpResponse('Hello')


@use_kwargs({
    "count": fields.Int(
        required=False,
        missing=100,
        validate=[validate.Range(min=1, max=999)]
    )},
    location="query"
)
def generate_students(request, count):
    return HttpResponse('Hello')