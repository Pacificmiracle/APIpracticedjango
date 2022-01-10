from rest_framework import serializers
from .models import Entry

class EntrySerializer(serializers.ModelSerializer):
    ID = serializers.CharField(max_length=10,primary_key=True)
    Name = serializers.CharField(max_length=50)
    Number = serializers.CharField(max_length=50)

    class Meta:
        model = Entry
        fields = ('__all__')