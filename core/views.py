from django.shortcuts import render

def home(request):
    return render(request, 'theme/index.html')
def upload(request):
    return render(request, 'theme/upload.html')  # Create this template later
