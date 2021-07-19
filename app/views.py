from django.shortcuts import render
from .models import Person
from .forms import PersonForm
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django import forms
from .forms import UserRegistrationForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from mysite.settings import EMAIL_HOST_USER

from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from .serializers import PersonSerializer
from rest_framework import permissions
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response



# Create your views here.
def person_list(request):
	persons = Person.objects.all()
	return render(request, 'app/person_list.html', {'persons':persons})
@login_required
def person_new(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save(commit=False)
            person.save()
            return redirect('person_list')
    else:
        form = PersonForm()
    return render(request, 'app/person_edit.html', {'form': form})
@login_required
def person_edit(request,pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == "POST":
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            person = form.save(commit=False)
            person.save()
            return redirect('person_list')
    else:
        form = PersonForm(instance=person)
    return render(request, 'app/person_edit.html', {'form': form})
@login_required
def person_delete(request, pk):
    data_to_be_deleted = get_object_or_404(Person, pk = pk)
    if request.method == 'POST':
        data_to_be_deleted.delete()
        return redirect('person_list')

    return render(request, 'app/person_delete.html', {'data_to_be_deleted': data_to_be_deleted})
@login_required
def person_detail(request, pk):
    data = get_object_or_404(Person, pk = pk)

    return render(request, 'app/person_detail.html', {'data': data})



def home(request):
    return render(request, 'registration/home.html')
    
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                login(request, user)
                return redirect('person_list')    
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')
                
    else:
        form = UserRegistrationForm()
        
    return render(request, 'registration/register.html', {'form' : form})







def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "app/templates/registration/password_reset_email.txt"
                    c = {
                    "email":user.email,
                    'domain':'127.0.0.1:8000',
                    'site_name': '',
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "user": user,
                    'token': default_token_generator.make_token(user),
                    'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'shilpagupta841287@gmail.com' , [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect ("/password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="app/registration/password_reset.html", context={"password_reset_form":password_reset_form})


# def password_reset_form(request):
#     sub = forms.PasswordResetForm()
#     if request.method == 'POST':
#         sub = forms.PasswordResetForm(request.POST)
        
#         recepient = str(sub['Email'].value())

#         send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
#        # return render(request, 'app/registration/success.html', {'recepient': recepient})
#     return render(request, 'app/registration/index.html', {'form':sub})



class PersonListAPI(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'app/person_list.html'

    def get(self, request):
        queryset = Person.objects.all()
        return Response({'persons' : queryset})
    



class PersonCreateAPI(CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'app/person_edit.html'
    
    def post(self, request):
        queryset = Person.objects.all()
        return Response({'persons' : queryset})
    



class PersonUpdateAPI(UpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'app/person_edit.html'
    
    def put(self, request, pk):
        queryset = Person.objects.all()
        return Response({'persons' : queryset})
    


class PersonDestroyAPI(DestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'app/person_delete.html'
    
    def delete(self, request, pk):
        queryset = Person.objects.all()
        return Response({'persons' : queryset})
    