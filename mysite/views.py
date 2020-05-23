import datetime
from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from bookmark.models import Bookmark
# from django.utils import timezone
from django.views import View
from django.views.generic.edit import FormView
from django.utils.dateformat import format
from .forms import ReportForm

def index(request):
	return render(request,'layout.html')

class Report(FormView):
    template_name = 'report.html'
    form_class = ReportForm

    def form_valid(self, form):
        date = form.cleaned_data.get('date')
        year = date.year
        month = format(date, 'm')
        day = format(date, 'd')
        print(str(day)+'/'+str(month)+'/'+str(year))
        return redirect('report_details', year, month, day)

class ReportDetails(View):
    def get(self, request, year, month, day):
        # do your thing here, filter the data etc
        d = Bookmark.objects.filter(date__contains=datetime.date(int(year),int(month),int(day)))
        data={'data':d}
        return render(request, 'report_details.html',data)

	# else:
	 #	now = timezone.now()
	 #	d=Bookmark.objects.filter(date=now).order_by('title')
	 #	data={'data':d}
	 #	return render(request,'showdata.html',data)
	 # data={'bookmark':bookmark}

def postdata(request):
	if request.method=='POST':
		b_title=request.POST.get('title')
		b_url=request.POST.get('url')
		sdata=Bookmark(title=b_title,url=b_url)
		sdata.save()

	return render(request,'postdata.html')
