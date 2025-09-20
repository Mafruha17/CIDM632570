from django.shortcuts import render, redirect
from .models import CodeSnippet
from .forms import CodeSnippetForm

def create_snippet(request):
    if request.method == 'POST':
        form = CodeSnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_snippets')
    else:
        form = CodeSnippetForm()
    return render(request, 'hallucination_app/create_snippet.html', {'form': form})

def list_snippets(request):
    snippets = CodeSnippet.objects.all().order_by('-created_at')
    return render(request, 'hallucination_app/list_snippets.html', {'snippets': snippets})
