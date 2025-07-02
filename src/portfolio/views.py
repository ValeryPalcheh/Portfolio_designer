from django.shortcuts import render, get_object_or_404
from .models import Project, Category
from django.utils import timezone

def index(request):
    category_id = request.GET.get('category')
    if category_id:
        projects = Project.objects.filter(category__id=category_id)
    else:
        projects = Project.objects.all()
    categories = Category.objects.all()
    return render(request, 'portfolio/index.html', {
        'projects': projects,
        'categories': categories,
        'now': timezone.now()
    })

def about(request):
    return render(request, 'portfolio/about.html', {'now': timezone.now()})

def contact(request):
    return render(request, 'portfolio/contact.html', {'now': timezone.now()})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'portfolio/project_detail.html', {'project': project, 'now': timezone.now()})

