from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from inventory.models import Medicine
from django.http import HttpResponse
from forms import InventoryForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf


# Create your views here.
def add(request):
	if request.POST:
		form = InventoryForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/inventory/all')

	else:
		form = InventoryForm()

	args = {}
	args.update(csrf(request))
	args['form'] = form
	return render_to_response('add_inventory.html', args)	

def all(request):
	args = {}
	args.update(csrf(request))

	args['all'] = Appointment.objects.all()
	return render_to_response('all.html',
		args )


