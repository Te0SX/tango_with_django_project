from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	# Construct a dictionary to pass to the template engine as its context.
	# Note the key boldmessage matches to {{ boldmessage }} in the template! 
	context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}

	# Return a rendered response to send to the client.
	return render(request, 'rango/index.html', context=context_dict)

def about(request):
	# Construct a dictionary to pass to the template engine as its context.
	# Note the key boldmessage matches to {{ boldmessage }} in the template! 
	context_dict = {'boldmessage': 'This tutorial has been put together by Theodoros Vrakas'}

	# Return a rendered response to send to the client.
	return render(request, 'rango/about.html', context=context_dict)
	


# def index(request):
# 	return HttpResponse("Rango says hey there partner! " + "<a href='/rango/about/'>About</a>")

# # Part of the Exercise 3
# def about(request):
# 	return HttpResponse("Rango says here is the about page. " + "<a href='/rango/'>Index</a>")
