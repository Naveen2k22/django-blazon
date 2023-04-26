from django import forms
from .models import User

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Field, Div, Submit, Button

class UserCreate(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        
        self.helper.layout = Layout(
            Div(
                Field('f_name'),
                Field('m_name'),
                Field('l_name'),
                Field('gender'),
                Field('address'),
                Field('email'),
                Field('phone'),
                css_class="grid gap-x-6 gap-y-0 mb-6 grid-cols-1 grid-rows-2 md:grid-cols-2 md:grid-rows-2 font-['Poppins'] sm:grid-cols-1 sm:grid-rows-7 lg:grid-cols-3 "
            ),
            Div(
                Submit(name="submit", value="Save", css_class="py-2 px-6 bg-[var(--success)] rounded text-white font-bold font-['Poppins'] cursor-pointer"),
                Button(name="button", value="Cancel", css_class="py-2 px-6 bg-[var(--warning)] rounded text-white font-bold font-['Poppins'] cursor-pointer", css_id="cancel-btn"),
                css_class="flex justify-center items-center gap-2"
            )
        )
        