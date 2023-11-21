# import libraries
from flask import Flask, render_template, request
from gpiozero import OutputDevice, PWMOutputDevice
from gpiozero.pins.pigpio import PiGPIOFactory
from prometheus_flask_exporter import PrometheusMetrics

# Define our app
app = Flask(__name__)

# Define the metrics
metrics = PrometheusMetrics(app)
metrics.register_default(
    metrics.counter(
        'by_path_counter', 'Request count by request paths',
        labels={'path': lambda: request.path}
    )
)

# Add an endpoint counter
endpoint_counter = metrics.counter(
    'endpoint_counter', 'Request count by endpoints',
    labels={'endpoint': lambda: request.endpoint}
)

# Define factory
factory = PiGPIOFactory(host='')

#Define the motor pins and PWM pins
en_1 = PWMOutputDevice(12, pin_factory=factory)
en_2 = PWMOutputDevice(26, pin_factory=factory)
motor_in1 = OutputDevice(13,  pin_factory = factory)
motor_in2 = OutputDevice(21,  pin_factory = factory)
motor_in3 = OutputDevice(17,  pin_factory = factory)
motor_in4 = OutputDevice(27,  pin_factory = factory)

#Define the main home route
#This will print Robot app to the browser
@app.route("/")
@endpoint_counter
def index():
    return render_template("index.html")

## Directions for the robot
@app.route("/forward")
@endpoint_counter
def forward():
    motor_in1.on()
    motor_in2.off()
    motor_in3.on()
    motor_in4.off()
    return render_template("index.html")

@app.route("/backward")
@endpoint_counter
def backward():
    motor_in1.off()
    motor_in2.on()
    motor_in3.off()
    motor_in4.on()
    return render_template("index.html")

@app.route("/left")
@endpoint_counter
def left():
    motor_in1.off()
    motor_in2.on()
    motor_in3.on()
    motor_in4.off()
    return render_template("index.html")

@app.route("/right")
@endpoint_counter
def right():
    motor_in1.on()
    motor_in2.off()
    motor_in3.off()
    motor_in4.on()
    return render_template("index.html")

@app.route("/stop")
@endpoint_counter
def stop():
    motor_in1.off()
    motor_in2.off()
    motor_in3.off()
    motor_in4.off()
    return render_template("index.html")

## Add PWM Control
@app.route('/motorpwm', methods=['POST'])
@endpoint_counter
def motorpwm():
    slider = request.form["speed"]
    en_1.value = int(slider) / 10
    en_2.value = int(slider) / 10
    return render_template('index.html')

# add an errorhandler
@app.errorhandler(404)
@endpoint_counter
def page_not_found(e):
    return render_template('404.html'), 404

# it looks for name and then runs the app
if __name__ == "__main__":
    app.run(host="0.0.0.0")
