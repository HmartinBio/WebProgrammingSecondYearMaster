from django import forms
from MicroscopyQuizz.models import User
from MicroscopyQuizz.models import AnswerToTheQuizz
from MicroscopyQuizz.models import Answers
from MicroscopyQuizz.models import Images

''' Class: UserFormSignUp
This class allows to initialise formular to signUp'''

class UserFormSignUp(forms.ModelForm):
    class Meta: 
        model = User
        fields = ('name', 'surname', 
            'username', 'mailAddress', 
            'password',)


''' Class: QuizzFormMicroscopy
This class allows to initialise formular to Answer to the 
questions concerning Microscopy'''

class QuizzFormMicroscopy(forms.Form):
    choices = []
    answer = Answers.objects.filter(questionId = 1)
    
    for i in answer.all(): 
        choices.append((i.answer, i.answer))
    
    firstQuestion = forms.ChoiceField(choices = choices, widget = forms.RadioSelect)
    secondQuestion = forms.ChoiceField(choices = choices, widget = forms.RadioSelect)
    thirdQuestion = forms.ChoiceField(choices = choices, widget = forms.RadioSelect)
    fourthQuestion = forms.ChoiceField(choices = choices, widget = forms.RadioSelect)


''' Class: QuizzFormComponent
This class allows to initialise formular to Answer to the 
questions concerning Cellular Component'''


class QuizzFormComponent(forms.Form):
    choices = []
    answer = Answers.objects.filter(questionId = 2)
    
    for j in answer.all():
        choices.append((j.answer, j.answer))

    firstQuestion = forms.ChoiceField(choices = choices, widget = forms.RadioSelect)
    secondQuestion = forms.ChoiceField(choices = choices, widget = forms.RadioSelect)
    thirdQuestion = forms.ChoiceField(choices = choices, widget = forms.RadioSelect)
    fourthQuestion = forms.ChoiceField(choices = choices, widget = forms.RadioSelect)


''' Class: ImageSearchBar
This class allows to initialise the search bar in the aim to 
search pictures in the pictures gallery '''


class ImageSearchBar(forms.Form):
    searchBar = forms.CharField(max_length=200)



''' Class: ListBoxSearchBar
This class allows to initialise the list box next to the search bar
in the aim to select the item to autocomplete the search bar '''


class ListBoxSearchBar(forms.Form):
    columnNames = [field.name for field in Images._meta.get_fields()]
    choices = []
    choices.append(("", ""))
    for i in columnNames:
        choices.append((i, i))
    
    listbox = forms.CharField(widget = forms.Select(choices = choices))
