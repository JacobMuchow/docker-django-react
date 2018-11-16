from rest_framework import seralizers
from .models import Lead

class LeadSerializer(seralizers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'