from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView

from .models import Vendor, User
from .form import UserCreate

class UserListView(ListView):
    model = User
    template_name = 'user/index.html'
    
    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        return super().get_context_data(**kwargs)


def index(request):
    context = {
        "message": "Welcome to CloudBerry360 :)"
    }
    return HttpResponse(render(request, "index.html", context))

def vendor(request):
    latest_vendor_list = Vendor.objects.order_by("-created_at")[:5]
    context = { "vendor_list": latest_vendor_list }
    return HttpResponse(render(request, "vendor.html", context))

def vendor_detail(request, vendor_id):
    return HttpResponse("You're looking at vendor %s." % vendor_id)

def create_user(request):
    form = UserCreate(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("vendor:user"))
    context = { "form":form }    
    return HttpResponse(render(request, 'user/create.html', context))


def update_user(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return HttpResponseRedirect(reverse("vendor:user"))
    form = UserCreate(request.POST or None, instance = user)
    
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
