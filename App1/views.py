
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from App1.models import Sick,Docktur,Diseases,Recommender
from App1.serializers import Sickserializer,Dockturserializer,Disserializer,Recsserializer
from sklearn.externals import joblip


# Create your views here.
@csrf_exempt
def sickApi(request,id=0):
    if request.method=='GET':
        s=Sick.objects.all()
        sick_serializer=Sickserializer(s,many=True)
        mj=joblib.load('DecisionTree')
        print(mj(['abdominal_pain','sinus_pressure','runny_nose','unsteadiness','weakness_of_one_body_side','loss_of_smell',
              'bladder_discomfort']))
        return JsonResponse(sick_serializer.data,safe=False)
    elif request.method=='POST':
        s2=JSONParser().parse(request)
        sick_serializer1=Sickserializer(data=s2)
        if sick_serializer1.is_valid():
          sick_serializer1.save()
          return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to add",safe=False)
    elif request.method=='PUT': 
          sick_data1=JSONParser().parse(request)
          sick1=Sick.objects.get(sickId=sick_data1['sickId'])
          sick_serializer1=Sickserializer(sick1,data=sick_data1)
          if sick_serializer1.is_valid():
             sick_serializer1.save()
             return JsonResponse("Update Successfully",safe=False)
          return JsonResponse("Failed to update",safe=False)
    elif request.method=='DELETE':
         sick2=Sick.objects.get(sickId=id)
         sick2.delete()
         return JsonResponse("deleted Successfully",safe=False)



         
def DocApi(request,id=0):
    if request.method=='GET':
        d=Docktur.objects.all()
        doc_serializer=Dockturserializer(d,many=True)
        return JsonResponse(doc_serializer.data,safe=False)
    elif request.method=='POST':
        d2=JSONParser().parse(request)
        doc_serializer1=Dockturserializer(data=d2)
        if doc_serializer1.is_valid():
          doc_serializer1.save()
          return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to add",safe=False)
    elif request.method=='PUT': 
          doc_data1=JSONParser().parse(request)
          doc1=Docktur.objects.get(DocId=doc_data1['DocId'])
          doc_serializer1=Dockturserializer(Doc1,data=doc_data1)
          if doc_serializer1.is_valid():
             doc_serializer1.save()
             return JsonResponse("Update Successfully",safe=False)
          return JsonResponse("Failed to update",safe=False)
    elif request.method=='DELETE':
         doc2=Docktur.objects.get(DocId=id)
         doc2.delete()
         return JsonResponse("deleted Successfully",safe=False)


def DisApi(request,id=0):
    if request.method=='GET':
        i=Diseases.objects.all()
        dis_serializer=Disserializer(i,many=True)
        return JsonResponse(dis_serializer.data,safe=False)
   
   
    elif request.method=='POST':
        i2=JSONParser().parse(request)
        dis_serializer1=Disserializer(data=i2)
        if dis_serializer1.is_valid():
          dis_serializer1.save()
          return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to add",safe=False)
    elif request.method=='PUT': 
          dis_data1=JSONParser().parse(request)
          dis1=Diseases.objects.get(DisId=dis_data1['DisId'])
          dis_serializer1=Disserializer(dis1,data=dis_data1)
          if dis_serializer1.is_valid():
             dis_serializer1.save()
             return JsonResponse("Update Successfully",safe=False)
          return JsonResponse("Failed to update",safe=False)
    elif request.method=='DELETE':
         dis2=Diseases.objects.get(DisId=id)
         dis2.delete()
         return JsonResponse("deleted Successfully",safe=False)



def RecommenderAPI(request,id=0):
     if request.method=='GET':
        i=Recommender.objects.all()
        dis_serializer=Recsserializer(i,many=True)
        return JsonResponse(dis_serializer.data,safe=False)
     elif request.method=='POST' :
        i2=JSONParser().parse(request)
        dis_serializer1=Recsserializer(data=i2)
        if dis_serializer1.is_valid():
          dis_serializer1.save()
          return JsonResponse("Added Successfully",safe=False)
   



# model=joblib.load(DecisionTree.Joblib)
# def predict(request):
#     return render(request,model)
