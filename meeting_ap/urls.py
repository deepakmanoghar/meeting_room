from django.urls import path
from .views import MeetingRoomListView,MeetingRoomCreateView, BookingCreateAPIView, AvailableMeetingRoomListAPIView

urlpatterns = [
    path('meeting-rooms/', MeetingRoomListView.as_view(), name='meeting-room-list'),
    path('create-meeting-room/', MeetingRoomCreateView.as_view(), name='create-meeting-room'),
    path('bookings/', BookingCreateAPIView.as_view(), name='booking-create'),
    path('available-meeting-rooms/', AvailableMeetingRoomListAPIView.as_view(), name='available-meeting-room-list'),
]