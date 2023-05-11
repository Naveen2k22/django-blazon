from typing import Any, Dict
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from django.contrib import messages

from .models import Vendor, User, Desig
from .form import UserForm, DesigForm, DesigGradeFormSet

class UserListView(ListView):
    model = User
    template_name = 'user/index.html'
    
    def get_context_data(self, **kwargs: any) -> Dict[str, any]:
        context = super().get_context_data(**kwargs)
        context.update({
            "table_headers" :["Firstname", "Lastname", "Address", "Email", "Phone"],
            "data_keys":["f_name", "l_name", "address", "email", "phone"]
        })
        return context

class DesigListView(ListView):
    model = Desig
    template_name = 'desig/index.html'
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update({
            "table_headers" :["Title", "Description"],
            "data_keys":["title", "description"]
        })
        return context

def index(request):
    context = {
        "message": "Welcome to CloudBerry360"
    }
    messages.info(request, "Greetings !!!")
    return HttpResponse(render(request, "index.html", context))

def vendor(request):
    latest_vendor_list = Vendor.objects.order_by("-created_at")[:5]
    context = { "vendor_list": latest_vendor_list }
    return HttpResponse(render(request, "vendor.html", context))

def vendor_detail(request, vendor_id):
    return HttpResponse("You're looking at vendor %s." % vendor_id)

def create_user(request):
    form = UserForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("vendor:user"))
    context = { "form":form }    
    return HttpResponse(render(request, 'user/create.html', context))

def create_desig(request):
    form = DesigForm(request.POST or None)
    formset = DesigGradeFormSet(request.POST or None, prefix="desig")
    if request.method == 'POST' and form.is_valid() and formset.is_valid():
        desig = form.save()
        grades = formset.save(commit=False)
        for grade in grades:
            grade.desig = desig
            grade.save()
        return HttpResponseRedirect(reverse("vendor:desig"))
    context = { "form":form, "formset":formset }
    return HttpResponse(render(request, 'desig/create.html', context))

def update_desig(request, desig_id):
    try:
        desig = Desig.objects.get(pk=desig_id)
    except Desig.DoesNotExist:
        return HttpResponseRedirect(reverse("vendor:desig"))
    
    desig_form = DesigForm(request.POST or None, instance = desig)
    grades_formset = DesigGradeFormSet(request.POST or None, instance=desig, prefix="desig")
    if request.method == 'POST':
        if desig_form.is_valid() and grades_formset.is_valid():
            desig_form.save()
            grades_formset.save(commit=False)
            print(grades_formset.deleted_objects, grades_formset.changed_objects, grades_formset.new_objects, grades_formset.cleaned_data)
            for deleted_grade in grades_formset.deleted_objects:
                deleted_grade.delete()
            for changed_grade in grades_formset.changed_objects:
                changed_grade[0].save()
            for new_grade in grades_formset.new_objects:
                new_grade.desig = desig
                new_grade.save()
            return HttpResponseRedirect(reverse("vendor:desig"))
    context = { "desig_form":desig_form, "grades_formset": grades_formset, "desig_id": desig_id}
    return HttpResponse(render(request, 'desig/update.html', context))

def delete_desig(request, desig_id):
    try:
        desig = Desig.objects.get(pk=desig_id)
    except Desig.DoesNotExist:
        return HttpResponseRedirect(reverse("vendor:desig"))
    desig.delete()
    return HttpResponseRedirect(reverse("vendor:desig"))

def update_user(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return HttpResponseRedirect(reverse("vendor:user"))
    form = UserForm(request.POST or None, instance = user)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("vendor:user"))
    else:
        context = { "form": form, "user_id": user_id }
        return render(request, "user/update.html", context)

def delete_user(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return HttpResponseRedirect(reverse("vendor:user"))
    user.delete()
    return HttpResponseRedirect(reverse("vendor:user"))
