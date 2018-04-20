
"use strict";

let DigitalRead = require('./DigitalRead.js')
let DigitalWrite = require('./DigitalWrite.js')
let AnalogWrite = require('./AnalogWrite.js')
let AnalogRead = require('./AnalogRead.js')
let DigitalSetDirection = require('./DigitalSetDirection.js')
let ServoWrite = require('./ServoWrite.js')
let ServoRead = require('./ServoRead.js')

module.exports = {
  DigitalRead: DigitalRead,
  DigitalWrite: DigitalWrite,
  AnalogWrite: AnalogWrite,
  AnalogRead: AnalogRead,
  DigitalSetDirection: DigitalSetDirection,
  ServoWrite: ServoWrite,
  ServoRead: ServoRead,
};
