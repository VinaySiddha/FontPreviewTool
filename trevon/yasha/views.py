# views.py

from django.shortcuts import render, redirect
from django.http import JsonResponse
from .services.compiler_api import compile_code
from .services.problem_api import get_problems, get_problem
from .services.container_api import create_container, get_container

def compile_view(request):
    if request.method == 'POST':
        source_code = request.POST.get('source_code')
        language = request.POST.get('language')
        try:
            result = compile_code(source_code, language)
            return JsonResponse(result)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return render(request, 'compile.html')

def problems_view(request):
    try:
        problems = get_problems()
        return render(request, 'problems.html', {'problems': problems})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def problem_detail_view(request, problem_id):
    try:
        problem = get_problem(problem_id)
        return render(request, 'problem_detail.html', {'problem': problem})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def create_container_view(request):
    if request.method == 'POST':
        image = request.POST.get('image')
        try:
            container = create_container(image)
            return JsonResponse(container)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return render(request, 'create_container.html')

def container_detail_view(request, container_id):
    try:
        container = get_container(container_id)
        return render(request, 'container_detail.html', {'container': container})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

