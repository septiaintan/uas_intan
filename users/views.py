from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User

from users.models import Biodata

from .forms import UserForms,BiodataForms
# Create your views here.


def is_operator(user):
    if user.groups.filter(name='Operator').exists():
        #request.session['is_operator'] = True
        return True
    else:
        return False

@login_required
@user_passes_test(is_operator)
def users(request):
    template_name = "back/tabel_users.html"
    list_user = User.objects.all()
    context = {
        'title':'tabel users',
        'list_user' : list_user
    }
    return render(request, template_name, context)
    

@login_required
@user_passes_test(is_operator)
def user_lihat(request, id):
    template_name = "back/user_lihat.html"
    try:
        user_info = User.objects.get(id=id)
        biodata = Biodata.objects.get(user=user_info)
    except:
        return redirect(users)
    context = {
        'title':'user lihat',
        'user_info': user_info,
        'biodata' : biodata,
    }
    return render(request, template_name, context)

@login_required
@user_passes_test(is_operator)
def user_edit(request, id):
    template_name = "back/user_edit.html"
    try:
        user_info = User.objects.get(id=id)
        biodata = Biodata.objects.get(user=user_info)
    except:
        return redirect(users)

    if request.method == "POST":
        forms_biodata = BiodataForms(request.POST, instance=biodata)
        forms_user = UserForms(request.POST, instance=user_info)
        if forms_user.is_valid() and forms_biodata.is_valid():
            forms_user.save()
            forms_biodata.save()
            return redirect(users)
    else:
        forms_biodata= BiodataForms(instance=biodata)
        forms_user= UserForms(instance=user_info)
    context = {
        'title' : 'edit user',
        'user_info' : user_info,
        'biodata' : biodata,

        'forms_user' : forms_user,
        'forms_biodata':forms_biodata,
    }
    return render(request, template_name, context)

@login_required
def user_delete(request, id):
    User.objects.get(id=id).delete()
    return redirect(users)
