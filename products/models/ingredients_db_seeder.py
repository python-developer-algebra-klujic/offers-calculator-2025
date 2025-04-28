
import csv

from .ingredients import Ingredient


CSV_TEXT = """\
1,Plastic Resin,PLR-001,High-density polyethylene,2.5,1.02,2.55
2,Aluminum Sheet,ALS-002,2mm thickness aluminum sheet,3.75,1.05,3.938
3,Stainless Steel Screws,SSS-003,M3 x 10mm screws,0.1,1.01,0.101
4,Lithium Battery,LBT-004,3.7V 1000mAh battery,4,1.08,4.32
5,Copper Wire,CWR-005,1mm diameter copper wire,0.2,1.03,0.206
6,LED Display,LED-006,16x2 character LCD display,2,1.1,2.2
7,Microcontroller,MCU-007,ATmega328P microcontroller,5,1.07,5.35
8,GPS Module,GPS-008,U-blox NEO-6M GPS module,12,1.15,13.8
9,PCB Board,PCB-009,Double-sided PCB board,1.5,1.02,1.53
10,Soldering Wire,SOW-010,0.8mm lead-free solder wire,0.05,1.01,0.051
11,Heat Shrink Tubing,HST-011,2:1 ratio heat shrink tubing,0.1,1.02,0.102
12,Ferrite Bead,FBD-012,EMI suppression ferrite bead,0.02,1.01,0.02
13,Ceramic Capacitor,CCA-013,100nF ceramic capacitor,0.01,1,0.01
14,Resistor,RES-014,10k ohm resistor,0.01,1,0.01
15,Voltage Regulator,VRG-015,LM7805 voltage regulator,0.5,1.04,0.52
16,Diode,DIO-016,1N4007 rectifier diode,0.02,1,0.02
17,Thermal Paste,THP-017,High-performance thermal paste,1,1.05,1.05
18,Enclosure,ENC-018,ABS plastic enclosure,3,1.1,3.3
19,Ribbon Cable,RBC-019,10-wire ribbon cable,0.5,1.02,0.51
20,Push Button,PBM-020,Momentary push button,0.15,1.02,0.153
21,Transistor,TRN-021,NPN transistor,0.02,1,0.02
22,Connector,CON-022,2-pin JST connector,0.1,1.02,0.102
23,Heat Sink,HSK-023,Aluminum heat sink,0.25,1.03,0.258
24,Crystal Oscillator,CRO-024,16 MHz crystal oscillator,0.05,1.02,0.051
25,Relay,RLY-025,5 V relay module,1,1.05,1.05
26,Potentiometer,POT-026,10 kΩ potentiometer,0.2,1.02,0.204
27,Tactile Switch,TSW-027,6 mm tactile switch,0.02,1.01,0.02
28,Inductor,IND-028,10 µH inductor,0.03,1.01,0.03
29,MOSFET,MOS-029,N-channel MOSFET,0.5,1.04,0.52
30,Ethernet Module,ETH-030,ENC28J60 Ethernet module,7,1.1,7.7
31,Thermistor,THM-031,10 kΩ thermistor,0.1,1.01,0.101
32,Optocoupler,OPC-032,4N35 optocoupler,0.2,1.02,0.204
33,Piezo Buzzer,PBZ-033,5 V piezo buzzer,0.5,1.03,0.515
34,DC Motor,DCM-034,6 V DC motor,3,1.1,3.3
35,Motor Driver,MDR-035,L298N motor driver,4,1.08,4.32
36,Light Sensor,LSR-036,Photodiode light sensor,0.3,1.02,0.306
37,Speaker,SPK-037,8 Ω speaker,2,1.05,2.1
38,Temperature Sensor,TMP-038,DS18B20 temperature sensor,1.5,1.05,1.575
39,Humidity Sensor,HMS-039,DHT22 humidity sensor,3,1.1,3.3
40,Pressure Sensor,PRS-040,BMP280 pressure sensor,4,1.08,4.32
41,Proximity Sensor,PRX-041,IR proximity sensor,1,1.05,1.05
42,Gyroscope,GYR-042,MPU6050 gyroscope module,3.5,1.1,3.85
43,Accelerometer,ACC-043,ADXL345 accelerometer,2.5,1.08,2.7
44,Ultrasonic Sensor,ULS-044,HC-SR04 ultrasonic sensor,2,1.07,2.14
45,Hall Effect Sensor,HLS-045,A3144 Hall effect sensor,0.5,1.03,0.515
46,Vibration Motor,VBM-046,3 V vibration motor,1.5,1.05,1.575
47,Light Emitting Diode,LED-047,5 mm red LED,0.02,1.01,0.02
48,Capacitive Touch Sensor,CTS-048,TTP223 touch sensor,1,1.05,1.05
49,RFID Module,RFID-049,RC522 RFID module,5,1.07,5.35
50,OLED Display,OLE-050,0.96-inch OLED display,6,1.1,6.6
"""

def ingredients_db_seed(request):
    csv_reader = csv.reader(CSV_TEXT.strip().splitlines())
    ingredients_list = []

    for (_,
         name,
         code,
         description,
         base_price,
         price_mod,
         final_price
    ) in csv_reader:
        ingredients_list.append(
            Ingredient(
                name=name,
                code=code,
                description=description,
                base_price=base_price,
                price_mod=price_mod,
                final_price=final_price
            )
        )
    Ingredient.objects.bulk_create(ingredients_list)
