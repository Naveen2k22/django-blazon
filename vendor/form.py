from django import forms
from .models import User,Desig,DesigGrade

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Field, Div, Submit, Button
from djangoformsetjs.utils import formset_media_js

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("f_name", "m_name", "l_name", "gender", "address", "email", "phone")
    
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
                css_class="grid gap-x-6 gap-y-0 mb-6 grid-cols-1 grid-rows-2 md:grid-cols-2 md:grid-rows-2 font-['Poppins'] sm:grid-cols-1 sm:grid-rows-7 lg:grid-cols-3"
            ),
            Div(
                Submit(name="submit", value="Save", css_class="py-2 px-6 bg-[var(--success)] rounded text-white font-bold font-['Poppins'] cursor-pointer"),
                Button(name="button", value="Cancel", css_class="py-2 px-6 bg-[var(--warning)] rounded text-white font-bold font-['Poppins'] cursor-pointer", css_id="cancel-btn"),
                css_class="flex justify-center items-center gap-2"
            )
        )
        

class DesigForm(forms.ModelForm):
    class Meta:
        model = Desig
        fields = ("title", "description")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Div(
                Field('title'),
                Field('description'),
                css_class="grid grid-cols-4 gap-4 font-['Poppins']"
            )
        )
        

class DesigGradeForm(forms.ModelForm):
    class Meta:
        model = DesigGrade
        fields = "__all__"
    
    class Media(object):
        js = formset_media_js
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Div(
                Field('grade', wrapper_class="py-2 !mb-0"),
                Field('from_amt', wrapper_class="py-2 !mb-0"),
                Field('to_amt', wrapper_class="py-2 !mb-0"),
                Field('DELETE', wrapper_class="hidden"),
                css_class="desig-form grid grid-cols-4 justify-center items-start gap-4 bg-white border-b border-l border-r dark:bg-gray-800 dark:border-gray-700 text-base whitespace-wrap px-4 font-['Poppins']",
            )
        )

DesigGradeFormSet = forms.inlineformset_factory(parent_model=Desig, model=DesigGrade, formset=forms.BaseInlineFormSet, form=DesigGradeForm, can_delete=True, extra=1, can_delete_extra=True)
