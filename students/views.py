from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from students.forms import StudentCreateForm
from students.models import Student
from students.utils import format_records


def hello(request):
    return HttpResponse('Hello')
#
#
# @use_kwargs({
#     "count": fields.Int(
#         required=False,
#         missing=100,
#         validate=[validate.Range(min=1, max=999)]
#     )},
#     location="query"
# )
# def generate_students(request, count):
#     return HttpResponse('Hello')

from webargs.djangoparser import use_kwargs, use_args
from webargs import fields


@use_args({
    "first_name": fields.Str(
        required=False
    ),
    "first_name__startswith": fields.Str(
        required=False
    ),
    "last_name": fields.Str(
        required=False
    ),
    "birthdate": fields.Date(
        required=False
    )},
    location="query"
)
def get_students(request, args):

    students = Student.objects.all().order_by('id')

    for param_name, param_value in args.items():
        if param_value:
            students = students.filter(**{param_name: param_value})

        # if param_name == 'first_name':
        #     students = students.filter(first_name=param_value)
        # elif param_name == 'last_name':
        #     students = students.filter(last_name=param_value)

    records = format_records(students)

    html_form = """
    <form>
    
      <label for="fname">First name:</label>
      <input type="text" id="fname" name="first_name"><br><br>
      
      <label for="lname">Last name:</label>
      <input type="text" id="lname" name="last_name"><br><br>
      
      <label for="age">Age:</label>
      <input type="number" id="age" name="age"><br><br>
    
      <input type="submit" value="Submit">
      
    </form>
 
    """

    response = html_form + records

    return HttpResponse(response)

@csrf_exempt
def create_student(request):

    if request.method == 'GET':

        form = StudentCreateForm()

    elif request.method == 'POST':

        form = StudentCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/students')

    html_form = f"""
    <form method="post">

      {form.as_p()}

      <input type="submit" value="Submit">

    </form>

    """

    response = html_form

    return HttpResponse(response)