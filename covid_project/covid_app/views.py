from django.shortcuts import render
from django.http import HttpResponse
from .models import covid_ind, covid_data_anal, data_base, Feedback_Enquiry
from covid_app.forms import NewUserForm
# Create your views here.

def index(request):
      anal = covid_data_anal.objects.all()
      data = covid_ind.objects.all()
      my_dict = {'anals': anal, 'datas': data}
      return render(request, 'covid_app/index.html', context = my_dict)

def data(request):
      datas = data_base.objects.all()
      my_dict = {'datas': data}
      return render(request, 'covid_app/data.html', context = my_dict)

def user(request):
      feeds = Feedback_Enquiry.objects.all()
#      imgs = Feedback_Enquiry.image.all()
#      reps = MyReply.objects.all()
      form = NewUserForm()
      
      if request.method == 'POST':
            form = NewUserForm(request.POST)
            
            if form.is_valid:
                  form.save(commit = True)
                  return index(request)
            else:
                  print('Error Form Invalid')
                  
      return render(request, 'covid_app/users.html', {'form': form, 'feeds':feeds})
                  