from django.forms import ModelForm, inlineformset_factory
from django import forms
from .models import Task, Tag, Tagmap
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description']

    name = forms.CharField(max_length=100)
    description = forms.CharField()
    
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Save'))
        super(TaskForm, self).__init__(*args, **kwargs)
        
class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
 
    name = forms.CharField(max_length=100, widget=forms.Textarea())
    
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Save'))
        super(TagForm, self).__init__(*args, **kwargs)

TaskFormSet = inlineformset_factory(Task, Task.tags.through, fields='__all__')