// Export the pigpio variable, express variable, define the app and port number, and prometheus

const pigpio = require('pigpio-client').pigpio({host: ''});
const express = require('express')
const app = express()
const port = 3000
const host = '0.0.0.0'
const path = require('path');
const promMid = require('express-prometheus-middleware');

// Connect to the Pi
const ready = new Promise((resolve, reject) => {
  pigpio.once('connected', resolve);
  pigpio.once('error', reject);
});

// Define prometheus Metrics
app.use(promMid({
   metricsPath: '/metrics',
  collectDefaultMetrics: true,
  requestDurationBuckets: [0.1, 0.5, 1, 1.5],
  requestLengthBuckets: [512, 1024, 5120, 10240, 51200, 102400],
  responseLengthBuckets: [512, 1024, 5120, 10240, 51200, 102400],
}));

// Add the static directory
app.use(express.static(__dirname +"/static"));

// create the main home route
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname+'/index.html'));
})


ready.then(async (info) => {
  // Define the pins
  const en1 = pigpio.gpio(12);
  const en2 = pigpio.gpio(26);
  const in1 = pigpio.gpio(13);
  const in2 = pigpio.gpio(21);
  const in3 = pigpio.gpio(17);
  const in4 = pigpio.gpio(27);
// Define our directions for the robot
  app.get('/forward', (req, res) => {
  in1.write(1);
  in2.write(0);
  in3.write(1);
  in4.write(0)
  res.sendFile(path.join(__dirname+'/index.html'));
});

  app.get('/backward', (req, res) => {
   in1.write(0);
   in2.write(1);
   in3.write(0);
   in4.write(1);
  res.sendFile(path.join(__dirname+'/index.html'));
});

  app.get('/left', (req, res) => {
     in1.write(0);
     in2.write(1);
     in3.write(1);
     in4.write(0);
  res.sendFile(path.join(__dirname+'/index.html'));
});

  app.get('/right', (req, res) => {
     in1.write(1);
     in2.write(0);
     in3.write(0);
     in4.write(1);
  res.sendFile(path.join(__dirname+'/index.html'));
});

  app.get('/stop', (req, res) => {
     in1.write(0);
     in2.write(0);
     in3.write(0);
     in4.write(0);
  res.sendFile(path.join(__dirname+'/index.html'));
});

// Routes for our speed control 
  app.get('/half', (req, res) => {
  en1.analogWrite(128);
  en2.analogWrite(128);
  res.sendFile(path.join(__dirname+'/index.html'));
});

  app.get('/full', (req, res) => {
   en1.analogWrite(255);
    en2.analogWrite(255);
  res.sendFile(path.join(__dirname+'/index.html'));
});



}).catch(console.error);

// create the main home route
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname+'/index.html'));
})

// Have the app listen to the port defined
app.listen(port, host, () => {
  console.log(`Example app listening on port ${port} and host ${host}`)
})





