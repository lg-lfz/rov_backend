from time import sleep
import pigpio
import RPi.GPIO as GPIO

# Set up BCM GPIO numbering
GPIO.setmode(GPIO.BCM)

# Connect to pigpio
pi = pigpio.pi() 

# ESC_PIN
ESC_GPIO = 18

def setSpeed(speed: int) -> None:
    print("Set speed")
    pi.set_servo_pulsewidth(ESC_GPIO, convert_speed(float(speed), 0.8))
    print("Speed is set to: ", speed)

def convert_speed(input_value: float, limitation: float = 1.0) -> int:
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

def close_connections():
    pi.set_servo_pulsewidth(ESC_GPIO, 0) # Stop servo pulses.
    pi.stop() # Disconnect pigpio.
