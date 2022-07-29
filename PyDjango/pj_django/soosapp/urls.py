from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.list, name='list'), #추가
    path('write/', views.write, name='write'), #추가
    path('write/write_ok/', views.write_ok, name='write_ok'), #추가
    path('delete/<int:id>', views.delete, name='delete'), #추가
    path('update/<int:id>', views.update, name='update'), #추가
    path('update/update_ok/<int:id>', views.update_ok, name='update_ok'), #추가
    path('glist/', views.glist, name='glist'),
    path('gwrite/', views.gwrite, name='gwrite'), 
    path('gwrite/gwrite_ok/', views.gwrite_ok, name='gwrite_ok'), 
    path('glist/<int:id>', views.content, name='content'), 
    path('gdelete/<int:id>', views.gdelete, name='gdelete'), 
    path('gupdate/<int:id>', views.gupdate, name='gupdate'),
    path('gupdate/gupdate_ok/<int:id>', views.gupdate_ok, name='gupdate_ok'),
    path('login/', views.login, name='login'),
    path('login/login_ok/', views.login_ok, name='login_ok'),
    path('logout/', views.logout, name='logout'),
]