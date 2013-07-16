from django.shortcuts import render_to_response
from django.http import HttpResponse

def search_form(request):
	return render_to_response('search_form.html')


def search(request):
	if 'q' in request.GET:
		message = 'You searched for: %r' % request.GET['q'] 
	else:
		message = 'You submitted an empty form.' 
	return HttpResponse(message)

def display_meta(request):
	values = request.META.items() 
	values.sort()
	html = []
	for k, v in values:
		html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v)) 
	return HttpResponse('<table>%s</table>' % '\n'.join(html))