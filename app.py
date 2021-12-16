from flask import Flask, render_template, request
from flask_mqtt import Mqtt

# Manually enter the mosquitto DB location and user info
app = Flask(__name__)
app.config['MQTT_BROKER_URL'] = '192.168.101.117'
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_USERNAME'] = 'pi'
app.config['MQTT_PASSWORD'] = 'raspberry'
app.config['MQTT_KEEPALIVE'] = 5
app.config['MQTT_TLS_ENABLED'] = False

mqtt = Mqtt(app)

# Publishing does work, currently the button only says hello world.
# Currently working on trying to allow user to subscribe to mqtt messages (not working)
@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        message = request.form['publish']
        mqtt.publish('topic', str(message))
        message = None
        return render_template('home.html')

    if request.method == 'GET':
        subscribe = request.form['subscribe']
        data = mqtt.subscribe(subscribe)

        return '''<h1>{}</h1>'''.format(data)

# App runs in debug to allow for changes to occur without having to restart the Application

if __name__ == '__main__':
    app.run(debug=True)