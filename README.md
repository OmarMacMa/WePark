# WePark

WePark is an Internet of Things project developed by a team of students at the Tecnologico de Monterrey university. The project uses sensors and an ESP8266 board to automatically monitor the occupancy of our campus parking lot in real time. The sensor data is processed and sent to an Azure PostgreSQL database, which is then displayed on our website for easy access by students and staff. By using WePark, you can quickly check which segments of the parking lot are available, saving you time and hassle when looking for a spot.

Our website features two pages: one displaying the current occupancy of the parking lot in real time, and another that provides historical statistics on the occupancy of the parking lot by hour and segment. This allows you to see not only where the available spots are at the moment, but also how the occupancy has changed over time and which segments tend to be the busiest.

Here is the main page:

Here is the stadictics page:

This web page was developed in Python 3.8 using the Django web framework. The required modules can be found in the `requirements.txt` file.

You can take a look at the web page in [HERE](http://ec2-54-167-62-67.compute-1.amazonaws.com:8000/index)
