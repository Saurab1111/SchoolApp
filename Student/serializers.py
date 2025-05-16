from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from Student.models import Student,Notes
from Class.models import Classes
from Class.serializer import ClassSerializer
from django.http import JsonResponse

class CustomClassField(serializers.RelatedField):

    def to_internal_value(self, data):
        div=data.split(' ')[1]
        std=data.split(' ')[0]
        id=Classes.objects.get(div=div,std=std)
        return id
        
    
    def to_representation(self, value):
        
        return str(value.std)+" "+str(value.div)

class NotesSerializer(ModelSerializer):
    # student= serializers.SerializerMethodField()
    # def get_student(self,obj):
    #     request=self.context.get('request')
    #     print(request.user)
    #     return request.user.student.id
       
    
    
    def create(self, validated_data):
        print(validated_data)
        request= self.context.get('request')
        validated_data['student']=request.user.student
        return Notes.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        request= self.context.get('request')
        for key,value in validated_data.items():
            setattr(instance,key,value)
        instance.student=request.user.student
        instance.save()
        return instance
        
    class Meta:
        model=Notes
        fields=['id','title','note','student_id']
    
    

class StudentSerializer(ModelSerializer):
    class_in= CustomClassField(queryset=Classes.objects.all())
    # class_in= ClassSerializer()
    
    class Meta:
        model= Student
        fields=['name','roll_no','class_in','user']
    
    # notes= serializers.SerializerMethodField()
    
    # def get_notes(self):
    #     print(self)