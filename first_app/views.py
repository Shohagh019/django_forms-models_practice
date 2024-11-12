from django.shortcuts import render
from .forms import PracticeModel
# Create your views here.
def home(request):
    form = PracticeModel()
    return render(request, 'index.html', {'form': form})