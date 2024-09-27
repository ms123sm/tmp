from django.shortcuts import render

# Create your views here.
from .models import User, Player

def user(request):
	return render(request, 'users/user.html', {'activeusers':Player.objects.get(id=1)})

def users(request):
	return render(request, 'users/users.html', {'allusers':User.objects.all()})


# def users(request):
# 	allusers = User.objects.all()
# 	filtered_users = User.objects.all()
# 	filtered_users = {'allusers': allusers.filter(score__range=[5,10])}
# 	# filtered_users = {'allusers': allusers.filter(score__in=[5,6,7,8,9,10])}
# 	# filtered_users = {'allusers': allusers.filter(username__contains='5')}
# 	# filtered_users = {'allusers': allusers.exclude(score=5)}
# 	# filtered_users = {'allusers': allusers.filter(score=5)}
# 	# allusers = User.objects.filter()
# 	return render(request, 'users/users.html', filtered_users)