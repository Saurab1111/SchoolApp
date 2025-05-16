from django.urls import path
from Class.views import ClassList,ClassDetails
urlpatterns = [
    path('list/',ClassList.as_view()),
    path('details/<int:pk>/',ClassDetails.as_view())
]
