Flask App to control home heating. 

  

The app requires a mosquitto DB to be running as that is how it will speak with,  

monitor and control IoT devices in a home (For this project I'm using Arduino  

devices).  

  

Eventually the app should be able to get data from a website so that temperatures  

within the home can be monitored. (Using Home Assistant for example.) 

  

The goal of this project is to incorporate a machine learning algorithm into the  

system in order to improve overall energy efficiency for the house. 

  

The flask application can currently be run from the app.py file. It is necessary  

to manually enter the mosquitto DB location and user info in order to connect the  

application.  

  

Currently working on getting current temperature data from a webpage while I wait 

for an Arduino device with the ability to get updates over the air/over WiFi. 

