from pyexpat import model
from rest_framework import serializers
from restaurants.models import Restaurant, Ticket
from users.models import Profile
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        
class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

class RestaurantSerializer(serializers.ModelSerializer):
    owner = ProfileSerializer(many=False)
    tickets = serializers.SerializerMethodField()
    
    class Meta:
        model = Restaurant
        fields = '__all__'
        
    def get_tickets(self, obj):
        tickets = obj.ticket_set.all()
        serializer = TicketSerializer(tickets, many=True)
        return serializer.data