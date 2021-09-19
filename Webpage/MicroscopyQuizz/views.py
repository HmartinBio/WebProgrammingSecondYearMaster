from django.shortcuts import render
from django.shortcuts import redirect
from MicroscopyQuizz.forms import UserFormSignUp
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from MicroscopyQuizz.models import Question, Images, AnswerToTheQuizz, Answers
from MicroscopyQuizz.models import User as UserDatabase
import random
from django.test import Client
from MicroscopyQuizz.forms import QuizzFormMicroscopy, QuizzFormComponent
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth import logout
from django.views import View
from MicroscopyQuizz.forms import ImageSearchBar
from MicroscopyQuizz.forms import ListBoxSearchBar
from django.http import JsonResponse

# Create your views here.

''' Method: home
    This method is used to give the homepage View'''

def home(request,):
    return render(request, "home/home.html")



''' Method: homeSignin
    This method is used to give the homepage view when the user 
    is connected to the website '''

@login_required
def homeSignin(request):
    score = UserDatabase.objects.get(username=request.user.username)
    score = score.score
    
    if (score == None): 
        score = 0
        
    return render(request, "home/homeSignedIn.html", {'score': score})



''' Method: choiceQuizz
    This method is used to give the view of the page 
    displaying the choice of questions type'''

def choiceQuizz(request,):
    score = UserDatabase.objects.get(username=request.user.username)
    score = score.score
    
    if (score == None):
        score = 0
    
    return render(request, "quizzTemplate/quizzChoicesTemplate.html", {'score': score})




''' Class: MicroscopyQuizzView
    This class is used to give the view of the page 
    displaying the questions concerning Microscopy'''



class MicroscopyQuizzView(View):
    form = QuizzFormMicroscopy

    def get(self, request):
    
        score = UserDatabase.objects.get(username=request.user.username)
        score = score.score
    
        if (score == None): 
            score = 0

        ## We increment the active game number of the user
        username = "{}".format(request.user.username)
        user = UserDatabase.objects.get(username = username)
    

        userGameActive = user.gameActive + 1
        user.gameActive = user.gameActive + 1
        user.save()
        request.session['userGameActive'] = userGameActive
    

        ## We extract the question concerning the microscopy

        question = Question.objects.get(category= 'microscopy')

        ## For each quizz, we ask to the user 10 questions
        ## So we creat a list with the number of questions

        listItems = range(0,4)
        
        ## Creations a dictionnary to store the URLs per 
        ## question
        
        dictionnaryURL = {}
        
        ## For each question

        for iterator in listItems:

            ## Initializing the list of URLs 
            ## For each question

            dictionnaryURL[iterator] = []

            microscopy = Answers.objects.filter(questionId=1)
            microscopy = microscopy.all()
            random_microscopy = random.choice(microscopy)
            microscopy = random_microscopy.answer

            answer = Answers.objects.get(answer= microscopy)
            userId = "{}_{}_{}".format(request.user.username, request.session['userGameActive'], iterator)
            userAnswer = AnswerToTheQuizz(usernamePlusQuestion = userId, goodAnswerId = answer.answerId)
            userAnswer.save()
            
            ## Creating a dictionnary to store the images
            ## And a list to store already used images

            dictionnary_images = {}
            used_images = []

            ## For the four pictures

            for iterator2 in range(0, 2):

                ## If the dictionnary of images is empty

                if (dictionnary_images == {}):

                    ## We take images whose the microscopy type
                    ## corresponds to our microscopy answer

                    images = Images.objects.filter(microscopy = microscopy)
                    images = images.all()

                    ## We choose a picture randomly in the database
                    ## And we add it to the dictionnary_images and 
                    ## to the used images 

                    random_choice = random.choice(images)
                    dictionnary_images[iterator2] = random_choice.url
                    used_images.append(random_choice.image_name)

                else:

                    ## If the dictionnary of images is not empty
                    ## We take images whose the microscopy type
                    ## corresponds to our microscopy answer
                    ## We choose a picture randomly in the database

                    images = Images.objects.filter(microscopy = microscopy)
                    images = images.all()
                    random_choice = random.choice(images)
                    
                    ## If the random picture corresponds to a already 
                    ## used picture, so, While the picture corresponds 
                    ## to a already used picture, we choose another p
                    ## picture

                    while(random_choice.image_name in used_images):
                        random_choice = random.choice(images)

                    ## And then, we add it to the dictionnary of images 
                    ## and to the used images

                    dictionnary_images[iterator2] = random_choice.url
                    used_images.append(random_choice.image_name)

            
            ## For all the elements in the dictionnary of pictures

            for iterator3 in dictionnary_images:

                ## We replace all the spaces by plus sign to get the URL of the picture
                ## And we append the URL to the URL dictionnary

                dictionnaryURL[iterator].append(dictionnary_images[iterator3]) 


        
        request.session['choiceQuestion'] = question.category
        request.session['question'] = question.question
        request.session['dictionnaryURL'] = dictionnaryURL


        return render(request, "quizzTemplate/quizzTemplateMicroscopy.html", {'choiceQuestion': request.session.get('choiceQuestion'),
            'question': request.session.get('question'), 'form': MicroscopyQuizzView.form, 'dictionnaryURL': request.session.get('dictionnaryURL'), 
            'score': score} )


    def post(self, request):

        score = UserDatabase.objects.get(username=request.user.username)
        score = score.score
    
        if (score == None): 
            score = 0

        form = MicroscopyQuizzView.form(request.POST)         

        if (form.is_valid()):
            
            list_answers = [form.cleaned_data['firstQuestion'],
            form.cleaned_data['secondQuestion'], 
            form.cleaned_data['thirdQuestion'], 
            form.cleaned_data['fourthQuestion']
            ]


            request.session['list_answers'] = list_answers

            list_answer_to_answer = []
            list_description_answer = []

            gainedScore = 0

            for iterator4 in range(0, 4):
                user = UserDatabase.objects.get(username = "{}".format(request.user.username))

                usernameComposed = request.user.username + "_{}".format(request.session['userGameActive']) + "_{}".format(iterator4)
                userAnswer = AnswerToTheQuizz.objects.get(usernamePlusQuestion = usernameComposed)

                answers = Answers.objects.get(answerId = userAnswer.goodAnswerId)

                score = Question.objects.get(question_id = 1)

                if (list_answers[iterator4] == answers.answer):
                    list_answer_to_answer.append("TrueQuestion")
                    gainedScore += score.points
                    
                
                else:
                    list_answer_to_answer.append("FalseQuestion")

                list_description_answer.append(answers.definition)
            
            user.score += gainedScore
            user.save()
            request.session['gainedScore'] = gainedScore

            request.session['list_answer_to_answer'] = list_answer_to_answer
            request.session['list_description_answer'] = list_description_answer 

            return redirect('QuizzMicroscopyCorrection')
            
        
        else:
            print(form.errors)



''' Method: MicroscopyQuizzView
    This method is used to redirect the user on the page 
    displaying the answers of the questions concerning 
    Microscopy'''


def MicroscopyQuizzPageCorrection(request):

    score = UserDatabase.objects.get(username=request.user.username)
    score = score.score

    return render(request, "quizzTemplate/quizzTemplateAnswers.html", 
        {'dictionnaryURL': request.session.get('dictionnaryURL'), 
        'list_answer_to_answer': request.session.get('list_answer_to_answer'), 
         'list_description_answer': request.session.get('list_description_answer'), 
         'list_choices': [('fluorescence microscopy', 0),  ('scanning electron microscopy (SEM)', 1), 
          ('transmission electron microscopy (TEM)', 2), ('phase contrast microscopy', 3)], 
          'list_answers': request.session.get('list_answers'), 'gained_score': request.session.get('gainedScore'), 
          'score': score})




''' Class: CellularComponentQuizzView
    This class is used to give the view of the page 
    displaying the questions concerning Cellular Component'''


class CellularComponentQuizzView(View):
    form = QuizzFormComponent

    def get(self,request):
    
        score = UserDatabase.objects.get(username=request.user.username)
        score = score.score

        ## We increment the active game number of the user
        username = "{}".format(request.user.username)
        user = UserDatabase.objects.get(username = username)
    

        userGameActive = user.gameActive + 1
        user.gameActive = user.gameActive + 1
        user.save()
        request.session['userGameActive'] = userGameActive
    

        ## We extract the question concerning the microscopy

        question = Question.objects.get(category= 'component')

        ## For each quizz, we ask to the user 10 questions
        ## So we creat a list with the number of questions

        listItems = range(0,4)
        
        ## Creations a dictionnary to store the URLs per 
        ## question
        
        dictionnaryURL = {}
        
        ## For each question

        for iterator in listItems:

            ## Initializing the list of URLs 
            ## For each question

            dictionnaryURL[iterator] = []

            component = Answers.objects.filter(questionId=2)
            component = component.all()
            random_component = random.choice(component)
            component = random_component.answer

            answer = Answers.objects.get(answer=component)
            userId = "{}_{}_{}".format(request.user.username, request.session['userGameActive'], iterator)
            userAnswer = AnswerToTheQuizz(usernamePlusQuestion = userId, goodAnswerId = answer.answerId)
            userAnswer.save()
            
            ## Creating a dictionnary to store the images
            ## And a list to store already used images

            dictionnary_images = {}
            used_images = []

            ## For the four pictures

            for iterator2 in range(0, 2):

                ## If the dictionnary of images is empty

                if (dictionnary_images == {}):

                    ## We take images whose the microscopy type
                    ## corresponds to our microscopy answer

                    images = Images.objects.filter(component = component)
                    images = images.all()

                    ## We choose a picture randomly in the database
                    ## And we add it to the dictionnary_images and 
                    ## to the used images 

                    random_choice = random.choice(images)
                    dictionnary_images[iterator2] = random_choice.url
                    used_images.append(random_choice.image_name)

                else:

                    ## If the dictionnary of images is not empty
                    ## We take images whose the microscopy type
                    ## corresponds to our microscopy answer
                    ## We choose a picture randomly in the database

                    images = Images.objects.filter(component = component)
                    images = images.all()
                    random_choice = random.choice(images)
                    
                    ## If the random picture corresponds to a already 
                    ## used picture, so, While the picture corresponds 
                    ## to a already used picture, we choose another p
                    ## picture

                    while(random_choice.image_name in used_images):
                        random_choice = random.choice(images)

                    ## And then, we add it to the dictionnary of images 
                    ## and to the used images

                    dictionnary_images[iterator2] = random_choice.url
                    used_images.append(random_choice.image_name)

            
            ## For all the elements in the dictionnary of pictures

            for iterator3 in dictionnary_images:

                ## We replace all the spaces by plus sign to get the URL of the picture
                ## And we append the URL to the URL dictionnary

                dictionnaryURL[iterator].append(dictionnary_images[iterator3]) 


    
        
        request.session['choiceQuestion'] = question.category
        request.session['question'] = question.question
        request.session['dictionnaryURL'] = dictionnaryURL

        return render(request, "quizzTemplate/quizzTemplateComponent.html", {'choiceQuestion': request.session.get('choiceQuestion'),
        'question': request.session.get('question'), 'form': CellularComponentQuizzView.form, 'dictionnaryURL': request.session.get('dictionnaryURL'), 
        'score': score} )


    def post(self, request):

        score = UserDatabase.objects.get(username=request.user.username)
        score = score.score

        form = CellularComponentQuizzView.form(request.POST)

        if (form.is_valid()):
            
            list_answers = [form.cleaned_data['firstQuestion'],
                form.cleaned_data['secondQuestion'], 
                form.cleaned_data['thirdQuestion'], 
                form.cleaned_data['fourthQuestion']
            ]


            request.session['list_answers'] = list_answers

            list_answer_to_answer = []
            list_description_answer = []

            gainedScore = 0

            for iterator4 in range(0, 4):
                user = UserDatabase.objects.get(username = "{}".format(request.user.username))

                usernameComposed = request.user.username + "_{}".format(request.session['userGameActive']) + "_{}".format(iterator4)
                userAnswer = AnswerToTheQuizz.objects.get(usernamePlusQuestion = usernameComposed)

                answers = Answers.objects.get(answerId = userAnswer.goodAnswerId)

                score = Question.objects.get(question_id = 2)

                if (list_answers[iterator4] == answers.answer):
                    list_answer_to_answer.append("TrueQuestion")
                    gainedScore += score.points
                    
                
                else:
                    list_answer_to_answer.append("FalseQuestion")

                list_description_answer.append(answers.definition)
            
            user.score += gainedScore
            user.save()
            request.session['gainedScore'] = gainedScore

            request.session['list_answer_to_answer'] = list_answer_to_answer
            request.session['list_description_answer'] = list_description_answer 

            return redirect('QuizzComponentCorrection')
            
        
        else:
            print(form.errors)


''' Method: ComponentPageCorrection
    This method is used to give the view of the answers
    to the questions concerning Cellular Component'''



def ComponentPageCorrection(request):
    
    score = UserDatabase.objects.get(username=request.user.username)
    score = score.score

    return render(request, "quizzTemplate/quizzTemplateAnswers.html", 
        {'dictionnaryURL': request.session.get('dictionnaryURL'), 
        'list_answer_to_answer': request.session.get('list_answer_to_answer'), 
         'list_description_answer': request.session.get('list_description_answer'), 
         'list_choices': [('pollen wall', 0), ('dendrite', 1),  ('synaptic vesicle', 2), 
          ('microtubule cytoskeleton', 3), ('desmosome', 4), ('axoneme', 5), ('endoplasmic reticulum', 6), 
          ('mitochondrion', 7)], 'list_answers': request.session.get('list_answers'), 'gained_score': request.session['gainedScore'], 
          'score': score})



''' Method: classment
    This method is used to give the view of the classment page'''


def classment(request,):
    score = UserDatabase.objects.get(username=request.user.username)
    score = score.score
    
    if (score == None):
        score = 0

    classmentDictionnary = {}
    user = UserDatabase.objects.order_by('score').reverse()

    for i in user.all():
        classmentDictionnary[i.username] = i.score

    return render(request, "Classment/classmentTemplate.html", {'classmentDictionnary': classmentDictionnary,
        'score': score})


''' Method: userSignUp
    This method is used to give the view of the SignUp page'''


def userSignUp(request,):
    if (request.method == "POST"):
        form = UserFormSignUp(request.POST)

        if (form.is_valid()):
            formperson = form.save(commit=True)
            user = User.objects.create_user(formperson.username, formperson.mailAddress, 
                formperson.password)
            
            user.surname = formperson.surname
            user.save()

            userdatabase = UserDatabase.objects.get(username=formperson.username)
            userdatabase.gameActive = 0
            userdatabase.score = 0
            userdatabase.save()
        

            user = authenticate(username=formperson.username, password=formperson.password)
            login(request, user)

            return redirect('SignedIn')


    else:
        form = UserFormSignUp()

    return(render(request, 'signUp/formSignUp.html', {'form': form}))



''' Method: searchBarImages
    This method is used to give the view of the Gallery 
    Images Search bar '''


def searchBarImages(request,):
    if (request.method == "POST"):
        form = ImageSearchBar(request.POST)
        formsearchBar = ListBoxSearchBar(request.POST)
        score = UserDatabase.objects.get(username=request.user.username)
        score = score.score
    
        if (score == None): 
            score = 0

        if (form.is_valid()):
            
            request.session['feature'] = form.cleaned_data['searchBar']
            return redirect('searchImagesResults')

    else:
        form = ImageSearchBar
        formsearchBar = ListBoxSearchBar
        score = UserDatabase.objects.get(username=request.user.username)
        score = score.score
    
        if (score == None): 
            score = 0
    
    return render(request, 'ImagesSearchBar/imageSearchBar.html', 
        {'form': form, 'formsearchBar': formsearchBar, 'score': score})





''' Method: searchBarImagesResults
    This method is used to give the view of the results
    of the search with the Gallery Images '''



def searchBarImagesResults(request,):
    
    score = UserDatabase.objects.get(username=request.user.username)
    score = score.score
    
    if (score == None): 
        score = 0
    
    category = request.session['category']
    feature = request.session['feature']

    images = Images.objects.filter(**{category: feature}).all()
    dictionnaryImages = {} 
    counter = 0


    for i in images:
        dictionnaryImages[counter] = []
        dictionnaryImages[counter].append(i.url)
        dictionnaryImages[counter].append(i.description)
        dictionnaryImages[counter].append(i.microscopy)
        dictionnaryImages[counter].append(i.cell_type)
        dictionnaryImages[counter].append(i.component)
        dictionnaryImages[counter].append(i.doi)
        dictionnaryImages[counter].append(i.organism)
        counter += 1


    return render(request, 'ImagesSearchBar/imageSearchBarResults.html', 
        {'dictionnaryImages': dictionnaryImages, 'score': score})




''' Method: autocompleteSearchBar
    This method is used to autocomplete
    the search bar in the Gallery Images view '''



def autocompleteSearchBar(request):
    if (request.is_ajax and request.method == 'POST'):
        category = request.POST['category']
        request.session['category'] = category
        images = Images.objects.values(category)
        images_values = []

        for i in range(0, len(images)):
            images_values.append(str(images[i][category]))

        images_values = list(dict.fromkeys(images_values))

        return JsonResponse(images_values, safe = False)



