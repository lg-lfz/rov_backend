from time import sleep
import pigpio
import RPi.GPIO as GPIO
import atexit

# Set up BCM GPIO numbering
GPIO.setmode(GPIO.BCM)

# Connect to pigpio
pi = pigpio.pi() 

def close_connections():
    pi.stop() # Disconnect pigpio.
    print("Closed gpio connections")

atexit.register(close_connections)

class motor_GPIO:
    def __init__(self):
        # ESC_PIN
        self.ESC_GPIO = 18
        atexit.register(self.stop_motor)

    def setSpeed(self, speed: int) -> None:
        print("Set speed")
        pi.set_servo_pulsewidth(self.ESC_GPIO, self.convert_speed(float(speed), 0.8))
        print("Speed is set to: ", speed)

    def convert_speed(self, input_value: float, limitation: float = 1.0) -> int:
        # Ensure the input_value is within the expected range
        if input_value < -10.0 or input_value > 10.0:
            raise ValueError("Input value must be in the range of -10.0 to +10.0")
        
        # Ensure the limitation is within the expected range
        if limitation > 1.0 or limitation <= 0.0:
            raise ValueError("Input value must be in the range of 0.0 to 1.0")
        
        # Map the input range [-10.0, +10.0] to output range [1000, 2000]
        output_value = 1500 + ((input_value * 50) * limitation)
        print("Outputvalue = ", output_value)
        return int(output_value)
    
    def stop_motor(self):
        pi.set_servo_pulsewidth(self.ESC_GPIO, 0) # Stop servo pulses.
        print("Stoped motor at pin ", self.ESC_GPIO)
