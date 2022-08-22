from rest_framework import serializers
from App1.models import Sick,Docktur,Diseases,Recommender

class Sickserializer(serializers.ModelSerializer):
    class Meta:
        model=Sick
        fields=('sickId',
                'sickName',
                'sickEmail')



class Dockturserializer(serializers.ModelSerializer):
    class Meta:
        model=Docktur
        fields=('DocId',
                'DocName',
                'Docspecialty',
                'docEmail'
                )                  

class Disserializer(serializers.ModelSerializer):
    class Meta:
        model=Diseases
        fields=('DisId','DisName','DisDescribe','specialty') 
class Recsserializer(serializers.ModelSerializer):
    class Meta:
        model=Recommender
        fields=('DisId','DisName','Recomend')         