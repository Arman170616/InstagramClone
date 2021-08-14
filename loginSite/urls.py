from django.urls import path
from loginSite import views

App_name = 'loginSite'


urlpatterns = [
    path('signup/', views.sign_up, name='sign_up'),

]
