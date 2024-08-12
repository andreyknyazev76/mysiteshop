from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms import ValidationError
from django.shortcuts import redirect, render
from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm

from applications.forms import CreateApplicationForm
from applications.models import Application 




@login_required
def create_application(request):
    if request.method == 'POST':
        form = CreateApplicationForm(data=request.POST)
        if form.is_valid():
            
            try:  
                user = request.user
                # Создать заявку
                application = Application.objects.create(
                     user=user,    
                     phone_number=form.cleaned_data['phone_number'],
                     description_address=form.cleaned_data['description_address'],
                    )
                       
                messages.success(request, 'Заявка отправлена!')
                return redirect('main:index')
            except ValidationError as e:
                messages.success(request, str(e))
                return redirect('main:index')
 
    context = {
        'title': 'Home - Отправка заявки',
        'applications': True,
    }
    return render(request, 'applications/create_application.html', context=context)
