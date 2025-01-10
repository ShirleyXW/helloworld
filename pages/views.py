import pickle
import pandas  as pd
import pdb
from django.shortcuts import render, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.views.generic import TemplateView

def homePageView(request):
    return render(request, 'home.html', {
        'mynumbers': [1, 2, 3, 4, 5, 6, ],
        'firstName': 'Xinli',
        'lastName': 'Wang',
    })

def aboutPageView(request):
    return render(request, 'about.html')

def studentPageView(request):
    return render(request, 'xinli.html')


def homePost(request):
    # Create variable to store choice that is recognized through entire function.
    choice = -999
    gmat = -999  # Initialize gmat variable.

    try:
        # Extract value from request object by control name.
        currentChoice = request.POST['choice']
        gmatStr = request.POST['gmat']

        # print("Just before Xinli's breakpoint")
        # pdb.set_trace()
        # breakpoint()
        # print("Just after breakpoint")

        # Crude debugging effort.
        print("*** Years work experience: " + str(currentChoice))
        choice = int(currentChoice)
        gmat = float(gmatStr)
    # Enters 'except' block if integer cannot be created.
    except:
        return render(request, 'home.html', {
            'errorMessage': '*** The choice was missing please try again',
            'mynumbers': [1, 2, 3, 4, 5, 6, ]})
    else:
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('results', args=(choice,gmat)))


def results(request, choice, gmat):
    print("*** Inside reults()")
    # load saved model
    with open('./model_pkl', 'rb') as f:
        loaded_model = pickle.load(f)

    # Create a single prediction
    singleSampleDf = pd.DataFrame(columns=['gmat', 'work_experience'])

    workExperience = float(choice)
    print("*** GMAT Score: " + str(gmat))
    print("*** Years experience: " + str(workExperience))
    singleSampleDf = singleSampleDf._append({'gmat': gmat,
                                             'work_experience': workExperience},
                                            ignore_index=True)

    singlePrediction = loaded_model.predict(singleSampleDf)

    print("Single prediction: " + str(singlePrediction))

    return render(request, 'results.html', {'choice': workExperience, 'gmat': gmat,
                                            'prediction': singlePrediction})
