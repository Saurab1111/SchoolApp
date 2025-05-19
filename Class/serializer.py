from rest_framework import serializers
from Class.models import Schools,Classes

class SchoolSerilalizer(serializers.ModelSerializer):
        # classes= serializers.PrimaryKeyRelatedField(queryset=Classes.objects.all(),many=True)
        
        class Meta:
            model=Schools
            fields='__all__'

        
class ClassSerializer(serializers.ModelSerializer):
    school=serializers.SlugRelatedField(
         queryset=Schools.objects.all(),
         slug_field='name'
    )
    class Meta:
        model=Classes
        fields='__all__'
    
    # def create(self,validated_data):
    #      validated_data['school']=