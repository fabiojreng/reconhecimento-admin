from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.users.models import User


@login_required(login_url="login")
def home(request):
    last_users = User.objects.all().order_by("-created_at")[:3]
    return render(request, "home.html", {"users": last_users})
