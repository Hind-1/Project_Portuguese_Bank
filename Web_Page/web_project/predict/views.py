from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
# from .models import PredResults

def predict(request):
    return render(request,'predict.html')

def predict_chances(request):
    if request.POST.get('action') == 'post':
        # Receive data from client
        age = float(request.POST.get('age'))
        duration = float(request.POST.get('duration'))
        campaign = float(request.POST.get('campaign'))
        pdays = float(request.POST.get('pdays'))
        previous = float(request.POST.get('previous'))
        model = pd.read_pickle('/Users/hindsalem/Desktop/Project_Portuguese_Bank/Data/Dataset/model.pickle')
        # # Make prediction
        result = model.predict([[age, duration, campaign, pdays, previous]])
        classification=result[0]
        # PredResults.objects.create(age=age, duration=duration, campaign=campaign,
                                #    pdays=pdays,previous=previous ,classification=classification)
        return JsonResponse({'result':classification,'age':age, 'duration':duration, 'campaign':campaign, 'pdays':pdays, 'previous':previous},
        safe=False)