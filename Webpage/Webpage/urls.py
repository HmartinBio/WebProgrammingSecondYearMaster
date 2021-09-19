"""Webpage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MicroscopyQuizz.views import home
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from MicroscopyQuizz.views import homeSignin
from MicroscopyQuizz.views import userSignUp
from MicroscopyQuizz.views import choiceQuizz
from MicroscopyQuizz.views import classment
from MicroscopyQuizz.views import MicroscopyQuizzPageCorrection
from django.contrib.auth import logout as django_logout
from MicroscopyQuizz.views import MicroscopyQuizzView
from MicroscopyQuizz.views import CellularComponentQuizzView
from MicroscopyQuizz.views import searchBarImages
from MicroscopyQuizz.views import autocompleteSearchBar
from MicroscopyQuizz.views import searchBarImagesResults
from MicroscopyQuizz.views import ComponentPageCorrection
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('MiniQuizz', home, name='MiniQuizz'),
    path("MiniQuizz/login", LoginView.as_view(), name='login'),
    path("MiniQuizz/SignUp", userSignUp, name= "SignUp"),
    path('MiniQuizz/SignedIn', homeSignin, name = "SignedIn"),
    path('MiniQuizz/QuizzChoice', choiceQuizz , name = "QuizzChoice"),
    path('MiniQuizz/Microscopy', MicroscopyQuizzView.as_view(), name = 'QuizzMicroscopy'), 
    path('MiniQuizz/Microscopy/Correction', MicroscopyQuizzPageCorrection, name = 'QuizzMicroscopyCorrection'),
    path('MiniQuizz/classment', classment, name = 'classment'),
    path('MiniQuizz/Component', CellularComponentQuizzView.as_view(), name='QuizzComponent'),
    path('MiniQuizz/Component/Correction', ComponentPageCorrection, name = 'QuizzComponentCorrection'),
    path('MiniQuizz/logout', LogoutView.as_view(), name='logout'),
    path('MiniQuizz/ImageSearch', searchBarImages, name="searchImages"),
    path('MiniQuizz/SearchImages', autocompleteSearchBar, name = 'autocompleteImageSearchBar'),
    path('MiniQuizz/ImageSearch/Results', searchBarImagesResults, name='searchImagesResults'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




    