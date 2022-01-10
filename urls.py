from django.urls import path
from Home import views
from .views import EntryViews

urlpatterns = [
    path('', views.home),
    path('show',views.show),
    path('send',views.send),
    path('delete',views.delete),
    path('edit',views.edit),
    path('RecordEdited',views.RecordEdited),
    path('Entry/', EntryViews.as_view()),
    path('Entry/<int:id>', EntryViews.as_view())
]

