from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from hashlib import md5
from os import system 
from string import Template

def command_line(engine, fingerprint):
	if engine == 'dot':
		return Template('$eng -Tpng -O static/data/$fp.$eng >static/data/$fp.$eng.txt 2>&1').substitute(eng=engine, fp=fingerprint)
	elif engine == 'mscgen':
		return Template('$eng -T png -i static/data/$fp.$eng -o static/data/$fp.$eng.png >static/data/$fp.$eng.txt 2>&1').substitute(eng=engine, fp=fingerprint)
	else:
		return None

def api(request):
	engine = request.GET.get('engine')
	code = request.GET.get('code').encode('utf-8')
	action = request.GET.get('action')
	if engine == '' or engine is None or code == '' or code is None:
		return HttpResponse('Invalid parameters')

	fingerprint = md5(code).hexdigest()
	try:
		f = open('static/data/%s.%s' % (fingerprint, engine), 'w')
		f.write(code)
		f.close()
	except:
		return HttpResponse('Generate graph failed')

	cmd = command_line(engine, fingerprint)
	ret = system(cmd)
		
	if action == "geterrormsg":
		return HttpResponseRedirect('/static/data/%s.%s.txt' % (fingerprint, engine))
	else:
		# return HttpResponse('/static/data/%s.%s.png' % (fingerprint, engine))
		return HttpResponseRedirect('/static/data/%s.%s.png' % (fingerprint, engine))
		

def examples(request):
	t = get_template('examples.html')
	html = t.render(Context({'HTTP_HOST': request.META['HTTP_HOST']}))
	return HttpResponse(html)

def examples_js(request):
	t = get_template('examples.js')
	html = t.render(Context({'HTTP_HOST': request.META['HTTP_HOST']}))
	return HttpResponse(html)

def playground(request):
	t = get_template('playground.html')
	html = t.render(Context({'HTTP_HOST': request.META['HTTP_HOST']}))
	return HttpResponse(html)

