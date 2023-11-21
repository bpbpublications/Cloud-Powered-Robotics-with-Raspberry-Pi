# import libraries
from flask import Flask, render_template, request
from gpiozero import OutputDevice, PWMOutputDevice
from gpiozero.pins.pigpio import PiGPIOFactory

# Define our app
app = Flask(__name__)

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
def index():
    return render_template("index.html")

## Directions for the robot
@app.route("/forward")
def forward():
    motor_in1.on()
    motor_in2.off()
    motor_in3.on()
    motor_in4.off()
    return render_template("index.html")

@app.route("/backward")
def backward():
    motor_in1.off()
    motor_in2.on()
    motor_in3.off()
    motor_in4.on()
    return render_template("index.html")

@app.route("/left")
def left():
    motor_in1.off()
    motor_in2.on()
    motor_in3.on()
    motor_in4.off()
    return render_template("index.html")

@app.route("/right")
def right():
    motor_in1.on()
    motor_in2.off()
    motor_in3.off()
    motor_in4.on()
    return render_template("index.html")

@app.route("/stop")
def stop():
    motor_in1.off()
    motor_in2.off()
    motor_in3.off()
    motor_in4.off()
    return render_template("index.html")

## Add PWM Control
@app.route('/motorpwm', methods=['POST'])
def motorpwm():
    slider = request.form["speed"]
    en_1.value = int(slider) / 10
    en_2.value = int(slider) / 10
    return render_template('index.html')


# it looks for name and then runs the app
if __name__ == "__main__":
    app.run(host="0.0.0.0")
