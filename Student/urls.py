from django.urls import path
from Student.views import StudentDetail,StudentList,NotesInfo,NotesDetail
urlpatterns = [
    path('list/',StudentList.as_view()),
    path('details/<int:pk>/',StudentDetail.as_view()),
    path('notes',NotesInfo),
    path('notes/<int:pk>',NotesDetail)
]
