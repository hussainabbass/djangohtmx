from django.urls import path
from . import views
from htmx.views import index
app_name = 'htmx'
urlpatterns = [
    path('',views.index,name='index'),
    path('add',views.adduser,name='adduser'),
    path('delete/<event_id>/',views.delete_event,name='delete-event'),
    path('edit/<event_id>/',views.edit_event,name='edit-event'),

]
