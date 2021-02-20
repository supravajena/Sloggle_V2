from django.shortcuts import render


def home(request):
    return render(request, 'SloggleUI/home.html')


def find_jobs(request):
    return render(request, 'SloggleUI/find_jobs.html')


def hire_freelancer(request):
    return render(request, 'SloggleUI/hire_freelancer.html')


def post_project(request):
    language_list = ["C", "C++", "Python"]
    return render(request, 'SloggleUI/post_project.html', {"language_list": language_list})


def about(request):
    return render(request, 'SloggleUI/about.html')


def contact(request):
    return render(request, 'SloggleUI/contact.html')


def post_project_details(request):
    return render(request, 'SloggleUI/post_project_details.html')
