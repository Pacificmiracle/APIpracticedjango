
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import EntrySerializer
from Home.models import Entry
from django.shortcuts import get_object_or_404
# Create your views here.
def home (request):
    return render(request,"home.html")

class EntryViews(APIView):
    def post(self, request):
        serializer = EntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
 
class EntryViews(APIView):
    def get(self, request, id=None):
        if id:
            item = Entry.objects.get(id=id)
            serializer = EntrySerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Entry.objects.all()
        serializer = EntrySerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
 
class EntryViews(APIView):
 
    def patch(self, request, id=None):
        item = Entry.objects.get(id=id)
        serializer = EntrySerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

class Entryviews(APIView):
    
    def delete(self, request, id=None):
        item = get_object_or_404(Entry, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})    
       
def show (request):
    data = Entry.objects.all()
    return render(request,"show.html",{'data': data })

def send (request):
    if request.method == 'POST':
        ID = request.POST['id']
        name = request.POST['Name']
        number =request.POST['Number']
        Entry(ID = ID, Name = name, Number = number).save()
        msg = "Data Saved Successfully" 
        return render(request,"home.html",{'msg':msg})
    else:
        return HttpResponse("<h1> NOT Found 404</h1>")
    
def delete(request):
    ID = request.GET['id']
    Entry.objects.filter(ID = ID).delete()
    return HttpResponseRedirect("show")

def edit(request):
    ID = request.GET['id']
    name = number = "NOT_AVAILABLE"
    for data in Entry.objects.filter( ID = ID ):
        name = data.name
        number = data.number  
    return render(request,"edit.html",{'ID':ID,'name':name, 'number':number})

def RecordEdited(request):
    if request.method == 'POST':
        ID = request.POST['id']
        name = request.POST['name']
        number = request.POST['number'] 
        Entry.object.filter(ID = ID).update(name = name, number = number)
        return HttpResponseRedirect("show")
    else:
        return HttpResponse("<h1> 404 NOT Found </h1>")
    
        


    