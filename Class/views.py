from rest_framework.response import Response
from Class.models import Schools,Classes
from Class.serializer import SchoolSerilalizer,ClassSerializer
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_200_OK
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

@api_view(['GET','POST'])
def Schools_list(request):
    if request.method=='GET':
        objects=Schools.objects.all()
        print(objects)
        serializer=SchoolSerilalizer(objects,many=True)
        print(request.user)
        return Response(serializer.data,status=HTTP_200_OK)
    
    if request.method=='POST':
        print(request.data)
        serializer=SchoolSerilalizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_200_OK)
    

@api_view(['GET','PUT','DELETE'])
def School_details(request,pk):
    instance= Schools.objects.get(pk=pk)
    print(instance.classes_set.all()) 
    if request.method=='GET':
        serializer= SchoolSerilalizer(instance)
        return Response(serializer.data,status=HTTP_200_OK)
    
    if request.method=='PUT':
        serializer=SchoolSerilalizer(instance,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_200_OK)
    
    if request.method=='DELETE':
        instance.delete()
        return Response("Deleted successfully!!",status=HTTP_200_OK)

class ClassList(ListCreateAPIView):
    queryset= Classes.objects.all()
    serializer_class=ClassSerializer

class ClassDetails(RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        pk=self.kwargs.get('pk')
        return Classes.objects.filter(pk=pk)

    serializer_class=ClassSerializer

