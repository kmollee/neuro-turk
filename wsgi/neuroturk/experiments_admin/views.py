from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render

#from polls.models import Poll
from experiments_admin.models import Assignment


def index(request):
    return render(request, 'experiments_admin/index.html')


def assignments(request):
    assignments_list = Assignment.objects.all()
    context = {'assignments_list': assignments_list}
    return render(request, 'experiments_admin/assignments.html', context)


def experiments(request):
    pass


def subjects(request):
    pass


def recruitment_environments(request):
    pass
