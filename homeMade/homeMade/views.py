from django.http import HttpResponse, Http404
# from django.template import Template, Context
# from django.template.loader import get_template 
# from django.template import Context
from django.shortcuts import render_to_response
import datetime

def hello(request):
	return HttpResponse("Hello world")

def current_datetime(request):
	# now = datetime.datetime.now()
	# html = "<html><body>It is now %s.</body></html>" % now 
	# return HttpResponse(html)
	
	now = datetime.datetime.now()
	
	# t = Template("<html><body>It is now {{ current_date }}.</body></html>") 
	
	# fp = open('/Users/zhengqin/Documents/WorkSpace/WebSite/Dev/HomeMadeFoodSharing/homeMade/templates/time.html')
	# t = Template(fp.read())
	# fp.close()

	# t = get_template('time.html')
	# html = t.render(Context({'current_date': now}))
	# return HttpResponse(html)

	return render_to_response('time.html', {'current_date': now})

def hours_ahead(request, offset): 
	try:
		offset = int(offset) 
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	# html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt) 
	# return HttpResponse(html)
	return render_to_response('hours_ahead.html', {'hour_offset':offset,'next_time':dt})