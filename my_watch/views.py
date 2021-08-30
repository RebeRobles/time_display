from django.shortcuts import render
from time import gmtime, strftime, localtime



# Create your views here.

def index(request):
    context =  {
      #'time': strftime('%Y-%m-%d %H:%M %p', gmtime()),
      'timelocal': strftime("%b-%d, %Y", localtime()),
      'timelocal1': strftime("%H:%M %p", localtime()),
    }
    return render(request, 'index.html', context)