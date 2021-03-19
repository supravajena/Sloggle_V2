from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import authenticate, login, logout

from .models import UserInfo

UserModel = get_user_model()
from .forms import SignUpForm


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return render(
            request,
            'SloggleUI/activation_confirmation_notice.html',
            {"message": "Thank you for your email confirmation. Now you can log in to your account."})
    else:
        return render(
            request,
            'SloggleUI/activation_confirmation_notice.html',
            {"message": "Activation link is not valid."})


def home(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        # TODO: delete this after debugging
        print(form.errors.as_data())
        
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return render(request, 'SloggleUI/makeYourChoice.html')
    else:
        form = SignUpForm()
    return render(request, 'SloggleUI/home.html', {'form': form})
    

def find_jobs(request):
    return render(request, 'SloggleUI/find_jobs.html')


def hire_freelancer(request):
    userInfos = UserInfo.objects.all()
    return render(request, 'SloggleUI/hire_freelancer.html', {"userInfos": userInfos})


def post_project(request):
    language_list = ["C", "C++", "Python"]
    return render(request, 'SloggleUI/post_project.html', {"language_list": language_list})


def about(request):
    return render(request, 'SloggleUI/about.html')


def contact(request):
    return render(request, 'SloggleUI/contact.html')


def post_project_details(request):
    return render(request, 'SloggleUI/post_project_details.html')


def register(request):
    if request.method == "POST":
        title = request.POST["title"]
        category = request.POST["category"]
        skills = request.POST["skills"]
        expertiseRadio = request.POST["expertiseRadio"]
        company = request.POST["company"]
        location = request.POST["location"]
        state = request.POST["state"]
        zip = request.POST["zip"]
        designation = request.POST["designation"]

        userInfo = UserInfo(title=title, category=category, skills=skills, expertiseRadio=expertiseRadio, company=company, location=location, state=state, zip=zip, designation=designation)
        userInfo.save()
    return render(request, 'SloggleUI/register.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=str(username), password=str(password))
        if user is None:
            return HttpResponse("Unauthorized")
        else:
            if user.is_active:
                login(request, user)
                return redirect("dashboard")
            else:
                return HttpResponse("Your username is : " + username)
    return render(request, 'SloggleUI/login.html')


def dashboard(request):
    if not request.user.is_authenticated:
        print(request.user)
        print(request.user.is_authenticated)
        return HttpResponse("Unauthorized User.")
    return render(request, "SloggleUI/dashboard.html")


def logout_user(request):
    logout(request)
    return redirect("home")