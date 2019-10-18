from django import forms
from test_app.models import TestModel

class TestModelForm(forms.ModelForm):
    class Meta:
        model = TestModel
        fields = '__all__'
