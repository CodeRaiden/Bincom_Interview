from django.shortcuts import render, redirect
from .models import AnnouncedPuResults, PollingUnit, PollUnitResult
from django.db import connection
from .forms import PollUnitResultForm
from django.contrib import messages

# Create your views here.
def individual_result(request):
 ipu = AnnouncedPuResults.objects.filter(polling_unit_uniqueid = 25)
 context = {
  'pu': ipu
 }

# Note that we can print/view/display the actual sql query used for the "AnnouncedPuResults.objects.all()" by the ORM on the terminal by pulling the query attribute from the ipu variable and printing it below
 print(ipu.query)

 # we can also have a more detailed information of the query by first importing the "connection" library from the django.db class and then down below we can print "connection.query"
 # print(connection.queries)

 return render(request, 'individual.html', context)




def summed_total(request):
 
 if request.method == "POST":

  # here we will check if the request is valid and if it is, we will save it to the database
  if request.POST.get('polling_unit_name'):
   puname= request.POST['polling_unit_name']
   # puId = PollingUnit.objects.all('uniqueid', polling_unit_name = puname)
   # partyAb = AnnouncedPuResults.objects.filter('party_Abbreviation', polling_unit_uniqueid = puId)
   # result = AnnouncedPuResults.objects.filter('party_score', polling_unit_uniqueid = puId)

   cursor = connection.cursor()
   cursor.execute("select Announced_Pu_Results.polling_unit_uniqueid,Announced_Pu_Results.party_Abbreviation,Announced_Pu_Results.party_score,Polling_Unit.polling_unit_name from Announced_Pu_Results join Polling_Unit on Announced_Pu_Results.polling_unit_uniqueid=Polling_Unit.uniqueid")

   joinTable = cursor.fetchall()

   for item in joinTable:
    if item[3] == puname:
     puId = item[0]
     partyAb = item[1]
     partyScore = item[2]
    

   summedT = 0
   
  #  for AResult in AnnouncedPuResults.objects.filter():
  #   summedT = summedT + AResult.party_score
   pu = AnnouncedPuResults.objects.filter(polling_unit_uniqueid = puId)
   
   for ar in AnnouncedPuResults.objects.filter(polling_unit_uniqueid = puId):
    summedT = summedT + ar.party_score
    
   # join = joinTable.index() == puId
    
   
   context = {
    'pu': pu,
    'puId': puId,
    'puname': puname,
    'summedTotal': summedT,
    'partyAbrevation': partyAb,
    'partyScore': partyScore,
    'joinTable': joinTable,
   }
    # to simply redirect the user to a page we can import redirect from django.shortcuts and use it here
    # return redirect('join')
    # or we can redirect the user back to the join view url and also persist the previous user input in the form using render
    
    # using the django inbuilt messaging class we can display a message in the front end
   messages.success(request, ("Request submitted successfully!"))
   return render(request, 'summedresult.html', context)  # now we can go on to reference the context in the frontend join.html page by including each value in the form field values.
  # else:
  #  messages.success(request, ('There was an error submitting your requset. Please try again latter'))
 else:
  allPolls = PollingUnit.objects.all()
  context = {
   'allPolls': allPolls,
  }
  return render(request, 'summed.html', context)
 


def all_results(request):
 
 all_members = PollUnitResult.objects.all()

 if request.method == 'POST':
  all_members = PollUnitResult.objects.filter(polling_unit_uniqueid = request.POST['polling_unit_uniqueid'])
  return render(request, 'allpuresult.html', {'all': all_members})
 
 return render(request, 'pollresults.html', {'all': all_members})
 

def add_party (request):
  if request.method == 'POST':
   form = PollUnitResultForm(request.POST or None)
   
   if form.is_valid:
    form.save()
   else:
    messages.success(request, ('There was an error submitting your requset. Please try again latter'))
  
    puuid = request.POST['polling_unit_uniqueid']
    partyab = request.POST['party_abbreviation']
    result = request.POST['party_score']
    puname = request.POST['polling_unit_name']

    context = {
     'puuid': puuid,
     'partyab': partyab,
     'result': result,
     'puname': puname,
     }

    return render(request, 'addparty.html', context)  # now we can go on to reference the context in the frontend join.html page by including each value in the form field values.
  
    # using the django inbuilt messging class we can display a message in the front end
   messages.success(request, ("Request submitted successfully!"))
   # now we need to go to the base.html page to decide where we want the message displayed in the frontend
   # here we can redirect the user back to the home page
   return redirect('allpuresult')
  else:
   return render(request, 'addparty.html', {})
 