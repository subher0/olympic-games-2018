from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import loader
from ..models.project import Project


def project_view(request, projectId):
    project = get_object_or_404(Project, pk=projectId)
    context = {
        'project': project
    }
    template = loader.get_template('main/project.html')
    return HttpResponse(template.render(context, request))
