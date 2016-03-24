from django.forms import ModelForm
from django import forms
from .models import Task
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'tags']

    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper = FormHelper()
        self.helper.form_id = 'id-task'
        self.helper.form_class = 'task'
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.add_input(Submit('submit', 'Save'))
        super(TaskForm, self).__init__(*args, **kwargs)
