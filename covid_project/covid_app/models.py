from django.db import models

# Create your models here.

class covid_ind(models.Model):
      confirmed = models.IntegerField(null = True, db_index = True, blank = True)
      day_increment_confirmed = models.IntegerField(null = True, db_index = True, blank = True)
      active = models.IntegerField(null = True, db_index = True, blank = True)
      day_increment_active = models.IntegerField(null = True, db_index = True, blank = True)
      recovered = models.IntegerField(null = True, db_index = True, blank = True)
      day_increment_recovered = models.IntegerField(null = True, db_index = True, blank = True)
      deaths = models.IntegerField(null = True, db_index = True, blank = True)
      day_increment_deaths = models.IntegerField(null = True, db_index = True, blank = True)
      date_updated = models.DateTimeField(null = True, db_index = True, blank = True)


class covid_data_anal(models.Model):

      daily_confirm = models.ImageField(upload_to = 'graphs', blank = True)
      monthly_confirm = models.ImageField(upload_to = 'graphs', blank = True)
      recov_daily_plot = models.ImageField(upload_to = 'graphs', blank = True)
      decease_daily_plot = models.ImageField(upload_to = 'graphs', blank = True)
      daily_hospitalize = models.ImageField(upload_to = 'graphs', blank = True)
      age_distribution = models.ImageField(upload_to = 'graphs', blank = True)
      heat_map = models.ImageField(upload_to = 'graphs', blank = True)
      conf_cum_plot = models.ImageField(upload_to = 'graphs', blank = True)
      pair_plot = models.ImageField(upload_to = 'graphs', blank = True)
      dailyconf_dist_15mar = models.ImageField(upload_to = 'graphs', blank = True)
      recovered_cum_plot = models.ImageField(upload_to = 'graphs', blank = True)
      deceased_cum_plot = models.ImageField(upload_to = 'graphs', blank = True)
      States_Conf_plot = models.ImageField(upload_to = 'graphs', blank = True)


class data_base(models.Model):
      age_group_data = models.FileField(upload_to = 'File', blank = True)
      statewise_test_details = models.FileField(upload_to = 'File', blank = True)
      individual_data = models.FileField(upload_to = 'File', blank = True)

class Feedback_Enquiry(models.Model):
      name_mandatory = models.CharField(max_length = 1000, null = True, db_index = True)
      suggestions_not_mandatory = models.CharField(max_length = 2000, blank = True, null = True, db_index = True, default = 'Hey')
      feedback_not_mandatory = models.CharField(max_length = 2000, blank = True, null = True, db_index = True)
      my_reply = models.CharField(max_length = 2000, blank = True, null = True, db_index = True)
      Enquiry_not_madatory = models.CharField(max_length = 2000, blank = True, null = True, db_index = True)
      time = models.DateTimeField(null = True, db_index = True, blank = True)
#      image = models.ImageField(upload_to = 'userposts', blank = True)
      
      def __str__(self):
            return self.name_mandatory
      
#      date_time = models.DateTimeField(null = True, db_index = True, blank = True)
      
class MyReply(models.Model):
      setfeedback = models.ForeignKey('Feedback_Enquiry', on_delete=models.CASCADE, max_length = 2000, blank = True, null = True, db_index = True)
      my_reply = models.CharField(max_length = 2000, blank = True, null = True, db_index = True)
      time = models.DateTimeField(null = True, db_index = True, blank = True)
      
      def __str__(self):
            return self.my_reply
