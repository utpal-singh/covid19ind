# -*- coding: utf-8 -*-
from django import forms
from covid_app.models import Feedback_Enquiry

class NewUserForm(forms.ModelForm):
      class Meta:
            model = Feedback_Enquiry
            exclude = ["my_reply", "time"]
