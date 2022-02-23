from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from restaurants.models import Restaurant, Ticket
from .serializers import RestaurantSerializer, TicketSerializer, UserSerializer
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

@api_view(['GET'])
def getRestaurants(request):
    restaurants = Restaurant.objects.all()
    serializer = RestaurantSerializer(restaurants, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getRestaurant(request, pk):
    try:
        restaurant = Restaurant.objects.get(id=pk)
        serializer = RestaurantSerializer(restaurant, many=False)
        return Response(serializer.data)
    except Restaurant.DoesNotExist:
        return Response(status=404)
    except ValidationError:
        return Response(ValidationError.error_dict, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createTicket(request):
    serializer = TicketSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response(serializer.error_messages, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def manageTicket(request, pk):
    try:
        ticket = Ticket.objects.get(id=pk)
    except Ticket.DoesNotExist:
        return Response(status=404)
    except ValidationError:
        return Response(ValidationError.error_dict, status=400)
    
    if request.method == 'GET':
        serializer = TicketSerializer(ticket, many=False)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = TicketSerializer(ticket, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    if request.method == 'DELETE':
        ticket.delete()
        return Response(status=204)

@api_view(['GET', 'POST'])
def purchaseTicket(request, pk):
    try:
        ticket = Ticket.objects.get(id=pk)
    except Ticket.DoesNotExist:
        return Response(status=404)
    except ValidationError:
        return Response(ValidationError.error_dict, status=400)
    
    if request.method == 'GET':
        restaurant = ticket.restaurant
        serializer = RestaurantSerializer(restaurant, many=False)
        return Response(serializer.data)
    
    if request.method == 'POST':
        if ticket.available:
            ticket.available = False
            ticket.save()
            return Response(status=200)
        else:
            return Response({'error': f'Sorry, the ticket "{ticket.name}" was already purchased'}, status=403)

@api_view(['POST'])
def registerUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = User.objects.create(username=serializer.validated_data['username'].lower())
        user.set_password(serializer.validated_data['password'])
        user.save()
        return Response({'message': 'User account was created'}, status=201)
    else:
        return Response(serializer.error_messages, status=400)