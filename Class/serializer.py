from rest_framework import serializers
from Class.models import Schools,Classes

class SchoolSerilalizer(serializers.ModelSerializer):
        classes= serializers.PrimaryKeyRelatedField(queryset=Schools.objects.all(),many=True)
        
        class Meta:
            model=Schools
            fields='__all__'

        
class ClassSerializer(serializers.ModelSerializer):
    school= serializers.StringRelatedField()
    class Meta:
        model=Classes
        fields='__all__'
    
    