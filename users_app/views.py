from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
# from .foms import  UserUpdateForm, ProfileUpdateForm


# django have different messages
# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.error

# Create your views here.


def register(request):
  if request.method == 'POST':
    form = UserRegisterForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      messages.success(request, f'Yor account have been created! you can now login.')
      return redirect('login')
  else:
    form = UserRegisterForm()
  return render(request, 'users_app/register.html',{'form' : form})

# @login_required
# def user_profile(request):
#   if request.method == "POST":
#     user_update_form = UserUpdateForm(request.POST, instance=request.user)
#     profile_update_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
    
#     if user_update_form.is_valid() and profile_update_form.is_valid():
#       user_update_form.save()
#       profile_update_form.save()
#       messages.success(request, f'Your profile has been updated!')
#       return redirect('user_profile')
  
#   else:
#     user_update_form = UserUpdateForm(instance=request.user)
#     profile_update_form = ProfileUpdateForm(instance=request.user.profile)

#   context = {
#     "user_update_form" : user_update_form,
#     "profile_update_form" : profile_update_form
#   }

#   return render(request,'users_app/user_profile.html',context=context)


