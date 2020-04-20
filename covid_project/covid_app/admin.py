from django.contrib import admin
from covid_app.models import covid_ind, covid_data_anal, data_base, Feedback_Enquiry, MyReply

# Register your models here.
admin.site.register(covid_ind)
admin.site.register(covid_data_anal)
admin.site.register(data_base)
admin.site.register(Feedback_Enquiry)
admin.site.register(MyReply)
