from django.forms import ModelForm
from django import forms
from .models import Task
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'tags']

    name = forms.CharField(max_length=100)
    description = forms.CharField()
    tags = forms.CharField()
    
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Save'))
        super(TaskForm, self).__init__(*args, **kwargs)