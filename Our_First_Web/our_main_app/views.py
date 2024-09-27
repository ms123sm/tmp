from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#these 2 functions gives an example of how to write into the page. This requires the HttpResponse
# def our_main_app(request):
# 	return HttpResponse('Hello World')

# def app2(request):
# 	return HttpResponse(2*11)

#to run templates, use Render

def app1(request):
	y = {'name2':'real is me not you', 'age':'100', 'major':'history', 'huge':"3456465645675"}
	# return render(request, 'app1/index.html', {'name1':'game', 'age':'33', 'major':'physics'})
	# you can get data through variables, folders, or any data resource in your system
	return render(request, 'app1/index.html', y)

def about(request):
	return render(request, 'app1/about.html')
