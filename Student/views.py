from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from Student.models import Student,Notes
from Student.serializers import StudentSerializer,NotesSerializer
from rest_framework.permissions import BasePermission
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from django.db.models import Q
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

# Create your views here.

        

class StudentList(ListCreateAPIView):
    queryset= Student.objects.all()
    serializer_class=StudentSerializer

class StudentDetail(RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        pk= self.kwargs.get('pk')
        return Student.objects.filter(pk=pk)
    
    def retrieve(self,request,*args,**kwargs):
        pk=kwargs.get('pk')
        # print("Called retrieve")
        serializer=Student.objects.get(pk=pk)
        serializer=StudentSerializer(serializer)
        return Response(serializer.data)

        pass
    serializer_class=StudentSerializer


# class NotesInfo(APIView):

#     def get(self,request):
#         print(request.user)
#         note= Notes.objects.all()
#         serializer=NotesSerializer(note)
#         return Response(serializer.data)
        

#     def post(self,request):
#         pass

#     def put(self,request):
#         pass

#     def delete(self,request):
#         pass

@api_view(['GET','POST'])
def NotesInfo(request):
    print(request.user)
    # limit= int(request.query_params.get('limit'))
    # offset=int(request.query_params.get('offset'))
    if request.method=='GET':
        if isinstance(request.user,User) :
            note= Notes.objects.filter(student_id=request.user.student.id)
            serializer=NotesSerializer(note,many=True,context={'request':request})
            return Response(serializer.data)
        else:
            return Response({'data':"Anonymous user, Please Login!"})
        
    if request.method=='POST':
        if isinstance(request.user,User) :
            serializer= NotesSerializer(data=request.data,context={'request':request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=HTTP_200_OK)
            else:
                return Response({'Error':'Please enter the valid data. Thanks!'})
        else:
            return Response({'data':"Anonymous user, Please Login!"})
        
def authorize(request,obj):
    if isinstance(request.user,User):
        if request.user.student.id== obj.student_id:
            return True
    return False



@api_view(['GET','PUT','DELETE','PATCH'])
def NotesDetail(request,pk):
    try:
        serializer=Notes.objects.get(pk=pk)
        if not serializer:
            raise Exception("No such data")
    except Exception as e:
        return Response({'Error':'No such data'})
    
    serializer=Notes.objects.get(pk=pk)
    if authorize(request,serializer):
        if request.method=='GET':
            serializer=NotesSerializer(serializer)
            return Response(serializer.data)
        if request.method=='PUT' or request.method=='PATCH':
            if request.method=='PUT':
                serializer= NotesSerializer(serializer,data=request.data,context={'request':request})
            else:
                serializer= NotesSerializer(serializer,data=request.data,context={'request':request},partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response({'error':'Enter valid data'})

        if request.method=='DELETE':
            serializer.delete()
            return Response('Deleted Successfully!!',status=HTTP_200_OK)
    else:
        return Response({'error':'Not authorized'})