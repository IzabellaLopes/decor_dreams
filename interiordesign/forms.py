from django import forms
from products.widgets import CustomClearableFileInput
from .models import Design


class DesignForm(forms.ModelForm):

    class Meta:
        model = Design
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-green rounded'