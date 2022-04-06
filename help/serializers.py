from rest_framework import serializers
from .models import Help


class HelpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Help
        fields = ['full_name', 'email', 'phone', 'subject', 'description', 'address']
