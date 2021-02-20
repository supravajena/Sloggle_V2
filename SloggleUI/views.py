from django.shortcuts import render


def home(request):
    return render(request, 'SloggleUI/home.html')


def find_jobs(request):
    return render(request, 'SloggleUI/find_jobs.html')


def hire_freelancer(request):
    return render(request, 'SloggleUI/hire_freelancer.html')


def post_project(request):
    return render(request, 'SloggleUI/post_project.html')
