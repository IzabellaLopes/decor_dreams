from django import forms
from .models import PreviousProject
from products.widgets import CustomClearableFileInput


class AddProjectImageForm(forms.ModelForm):
    class Meta:
        model = PreviousProject
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=True, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-green rounded'