""""User views"""

from django.contrib.auth import authenticate, login
from django.shortcuts import render

def login_view(request):

    return render(request, 'users/login.html')