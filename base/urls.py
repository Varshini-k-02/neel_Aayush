from django.urls import path
from . import views
urlpatterns =[
    path('',views.home,name="home"),
    path('login/',views.loginPage,name="login"),
    path('register/',views.registerPage,name="register"),
  
    path('complaint/',views.complaint,name="complaint"),
    path('empdashboard/',views.empdashboard,name="empdash"),
    path('empcategory/',views.empcategory,name="empcat"),
    path('empallcomp/',views.empallcomp,name="empallcomp"),
    path('assign/<str:pk>',views.assignment,name="assign"),
    path('comment/<str:pk>',views.comment,name="comment"),
    path('userdash/',views.userdashboard,name="userdash"),
    path('usercomplaint/',views.usercreatecomp,name="usercomp"),
    path('usercompstatus/',views.usercompstatus,name="usercompstatus"),
    path('userprofile/',views.userprofile,name="userprofile"),
    path('table',views.table,name="table"),
    
    path('progress/<str:pk>',views.progress,name="progress"),
   
    path('support/',views.support,name="support"),
    path('privacy/',views.privacy,name="privacy"),
    path('about/',views.about,name="about"),
    path('tandc/',views.tandc,name="tandc"),
    path('emppending/',views.emppending,name="emppending"),


]

