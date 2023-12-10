from django.shortcuts import render
from rest_framework import generics
from django.utils import timezone 
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status
from rest_framework.views import APIView
from .models import MeetingRoom, Booking
from .serializers import MeetingRoomSerializer, BookingSerializer

class MeetingRoomListView(APIView):
    def get(self, request):
        meeting_rooms = MeetingRoom.objects.all()
        serializer = MeetingRoomSerializer(meeting_rooms, many=True)
        return Response(serializer.data)

class MeetingRoomCreateView(APIView):
    def post(self, request):
        serializer = MeetingRoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookingCreateAPIView(generics.CreateAPIView):
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        room = serializer.validated_data['room']
        start_time = serializer.validated_data['start_time']
        end_time = serializer.validated_data['end_time']

        conflicting_booking = Booking.objects.filter(
            room=room,
            start_time__lt=end_time,
            end_time__gt=start_time
        ).first()

        if conflicting_booking:
            raise ValidationError("The room is already booked for the given time.")

        serializer.save(user=self.request.user)

class AvailableMeetingRoomListAPIView(generics.ListAPIView):
    serializer_class = MeetingRoomSerializer

    def get_queryset(self):
        booked_rooms = Booking.objects.filter(
            start_time__lt=timezone.now(),
            end_time__gt=timezone.now()
        ).values_list('room', flat=True)

        return MeetingRoom.objects.exclude(id__in=booked_rooms)