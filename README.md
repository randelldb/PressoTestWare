# PressoTestWare

Application specific developed for calibrating HVAC pressure switches.

**Design problem**

Create a application that is used to calibrate various types of pressure switches.
User is able to create different **"Calibration Models"**.

The calibration model contains the following data:
- Model name
- Pressure switch Make & Model
- Customer name/information

The Calibration models contains at least 1 **"Sensor Setup"** with a maximum of 2.

A Sensor setup consist of a sensor type and 6 **"Data values"**:

Sensor type e.g.:
- high pressure
- low pressure
- condenser pressure

| Upper range   | Lower range   |
| -----------   | ------------- |
| target value  | target value  |
| tolerance (+) | tolerance (+) |
| tolerance (-) | tolerance (-) |

Data is retrieved via a serial connection.
There are 4 types of data provided:
- Pressure (Bar)
- Room temp (Celsius)
- Relative air moisture rv(%)
- Switching state

The users task is to adjust the pressure switch in a way that the switching state changes
depending on the given range, configured in the Calibration model.



When a calibration is competed the result are outputted in 3 forms:
- Hard-copy (wired printer)
- Pdf (Cloud)
- Sticker (Label writer)

All certificates should have a unique identification number which is generated automatically.
This so called "counter" is stored in a database file. When needed the counter can be altered whitin the
settings of the application (not recommended).

The user is able to see the pressure rise and drop in some sort of graphical fashion e.g.
- chart
- range gauge
- numeric

to successful complete a calibration the proses must meet a set of rules:
- pressure switch adjusted within range
- a upper and a lower pass in a row
- room temp range between 19 and 21 degrees celsius
- relative air moisture range between 30% and 60%

If al these conditions are satisfy then the test will pass and is completing the test possible.
On completion the use can save, print certificate and print the sticker.