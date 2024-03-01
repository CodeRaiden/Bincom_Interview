from django import forms
from .models import AnnouncedPuResults, PollingUnit, PollUnitResult
from django.db import connection

# class AddPartyForm (forms.ModelForm):
#  # now we discribe our member form through a Meta class
#  class Meta:
#   # define model type
#   model = PollingUnit

#   # cursor = connection.cursor()
#   # cursor.execute("select Announced_Pu_Results.polling_unit_uniqueid,Announced_Pu_Results.party_Abbreviation,Announced_Pu_Results.party_score,Polling_Unit.polling_unit_name from Announced_Pu_Results join Polling_Unit on Announced_Pu_Results.polling_unit_uniqueid=Polling_Unit.uniqueid")
#   # model = cursor.fetchall()
#   model = AnnouncedPuResults

#   fields = ['party_Abbreviation', 'polling_unit_uniqueid', 'party_score']

#  class Meta:

#   model = PollingUnit
#   fields = ['polling_unit_name']






class PollUnitResultForm (forms.ModelForm):
 # now we discribe our member form through a Meta class
 class Meta:
  model = PollUnitResult

  fields = ['polling_unit_uniqueid', 'party_abbreviation', 'party_score', 'polling_unit_name']