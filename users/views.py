from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.views import View
from .models import author
from django.contrib.auth.hashers import check_password


class author_login(View):
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        #print(username, password)
        author_obj = author.get_auth_by_username(username)
        if(author_obj):
            print(author_obj.username)
            if(check_password(password, author_obj.password) or password == author_obj.password):
                request.session['auth_id'] = author_obj.id
                request.session['Name'] = author_obj.name
                return HttpResponseRedirect('/profile')
        else:
            return render(request, 'login.html', {'error': 'Wrong Username or Password'})
        return render(request, 'login.html')

class author_profile(View):
    def get(self, request):
        return render(request, 'profile.html')
    
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

# def login(request):
#     if request.method == 'POST':
#         form = 
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)