from django.http import HttpResponse, Http404
from django.template import Template, Context
import datetime

def hello(request):
	return HttpResponse("Hello world")

def current_datetime(request):
	# now = datetime.datetime.now()
	# html = "<html><body>It is now %s.</body></html>" % now 
	# return HttpResponse(html)
	now = datetime.datetime.now()
	# t = Template("<html><body>It is now {{ current_date }}.</body></html>") 
	fp = open('/Users/zhengqin/Documents/WorkSpace/WebSite/Dev/HomeMadeFoodSharing/homeMade/templates/time.html')
	t = Template(fp.read())
	fp.close()
	html = t.render(Context({'current_date': now}))
	return HttpResponse(html)

def hours_ahead(request, offset): 
	try:
		offset = int(offset) 
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt) 
	return HttpResponse(html)