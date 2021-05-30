from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import redirect_to_login
from django.shortcuts import redirect, render

from account.models import Profile
from account.forms import (UserRegisterForm,
                           ProfileRegisterForm)


class LogoutWithMessage(auth_views.LogoutView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.INFO, 'Ви успішно вийшли зі свого облікового запису!')
        return response


def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        profile_form = ProfileRegisterForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            # create new user, but do not save to db
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password1'])
            # save user in db.
            new_user.save()
            # creation profile
            new_profile = Profile.objects.create(user=new_user)
            # add type_user, phone number in Profile
            edit_profile = Profile.objects.get(user=new_user)
            edit_profile.phone_number = request.POST.get('phone_number')
            edit_profile.type_user = 'guest'
            edit_profile.save()
            # message
            messages.success(request, 'Чудово! Тепер Ви маєте свій обліковий запис!')
            if 'next_url' in request.session:
                return redirect_to_login(request.session['next_url'])
            else:
                return redirect('login')
    else:
        user_form = UserRegisterForm()
        profile_form = ProfileRegisterForm()
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'account/register.html', context=context)
