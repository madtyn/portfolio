from django.shortcuts import render

def hello_recruiter(request):
	return render(request, 'hello_recruiter.html', {})
