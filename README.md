Steps:
1) open the project.
2) open file in cd meetng_room
3) command install pip install-r requirements.txt .
4) make migrations the database in command python manage.py makemigrations.
5) after migrate the models in comman python manage.py migrate.
6) Then run the server in command python manage.py runserver.
7) open the Api url in POSTMAN for create meeting rooms http://localhost:8000/api/create-meeting-room/
8) check the meeting room http://localhost:8000/api/meeting-rooms/
9) For booking  http://localhost:8000/api/bookings/
10) for check the available meeting rooms http://localhost:8000/api/available-meeting-rooms/
   
