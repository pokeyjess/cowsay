from django.shortcuts import render
from cowsay_app.models import Input
from cowsay_app.forms import InputForm
import subprocess

# I mainly used this source to figure out subprocess: 
# https://linuxhint.com/execute_shell_python_subprocess_run_method/
# I also used Stackoverflow and Python docs

def index(request):
    if request.method == "POST":
        new_input = InputForm()
        form = InputForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Input.objects.create(
                input=data.get('input')
            )
            cow = subprocess.run(
                ['cowsay', data['input']], capture_output=True
            ).stdout.decode("utf-8")
            return render(request, "index.html", {'form': new_input, 'cow': cow})
                  
    form = InputForm()
    return render(request, "index.html", {"title": "Welcome to Cowsay", "form": form})
    
    


