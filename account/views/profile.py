from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from account.forms import ProfileForm
from account.models import CustomUser


@login_required
def profile(request):
    user = request.user
    return render(request, 'account/profile.html', {'user': user} )

@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('account:profile')
    else:
        form = ProfileForm(instance=user)
    return render(request, 'account/edit_profile.html', {'form': form})

