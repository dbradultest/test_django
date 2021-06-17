import datetime

from django.core.exceptions import ValidationError
from django.forms import ModelForm, DateInput, IntegerField


from students.models import Student


class StudentBaseForm(ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            # 'age',
            'birthdate',
            'email',
            'enroll_date',
            'graduate_date',
            'phone_number',
        ]
        # fields = '__all__'
        widgets = {'birthdate': DateInput(attrs={'type': 'date'})}

    @staticmethod
    def normalize_name(value):
        return value.lower().capitalize()

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        result = self.normalize_name(first_name)
        return result

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        result = self.normalize_name(last_name)
        return result

    # def clean_birthdate(self):
    #     birthdate = self.cleaned_data['birthdate']
    #     age = datetime.datetime.now().year - birthdate.year
    #     if age < 18:
    #         raise ValidationError('Age should be greater than 18 y.o.')
    #
    #     return birthdate

    def clean(self):
        enroll_date = self.cleaned_data['enroll_date']
        graduate_date = self.cleaned_data['graduate_date']
        if enroll_date > graduate_date:
            raise ValidationError('Enroll date coudnt be greater than graduate date!')


class StudentCreateForm(StudentBaseForm):
    pass


class StudentUpdateForm(StudentBaseForm):
    age = IntegerField()

    class Meta(StudentBaseForm.Meta):
        fields = [
            'first_name',
            'last_name',
            'birthdate',
            # 'age',
            'enroll_date',
            'graduate_date',
            'phone_number',
        ]

    def __init__(self, *args, **kwargs):
        self.base_fields['age'].initial = kwargs.get('instance').age()
        self.base_fields['age'].widget.attrs['readonly'] = True
        super().__init__(*args, **kwargs)
