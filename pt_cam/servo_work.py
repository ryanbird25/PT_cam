import machine
from machine import Pin, PWM
from utime import sleep

"""
SG90 Servo Control

PWM freuquency: 50Hz (20ms period)
Pulse Widths : Rotation Angle

1MS (1000us) : 0 degree
2MS (2000us) : 45 degree
3MS (3000us) : 90 degree
4MS (4000us) : 180 degree

"""
TILT_SERVO_PIN = 17
PAN_SERVO_PIN = 16

CAM_D0 = 6
CAM_D1 = 7
CAM_D2 = 8
CAM_D3 = 9
CAM_D4 = 10
CAM_D5 = 11
CAM_D6 = 12
CAM_D7 = 13

CAM_SCL = 3
CAM_SDA = 2

CAM_DCLK = 14
CAM_VSYNC = 4
CAM_HRFF = 5

CAM_PWDN = 18
CAM_RST = 15

tilt_pwm = PWM(Pin(TILT_SERVO_PIN, Pin.OUT))
pan_pwm = PWM(Pin(PAN_SERVO_PIN, Pin.OUT))

tilt_pwm.freq(50)
pan_pwm.freq(50)

def set_servo_angle(pwm_pin: PWM, angle: float):
    # Convert angle (0-180) to pulse width and then to duty cycle
    min_us = 500
    max_us = 2500
    pulse_us = int(min_us + (max_us - min_us) * angle // 180)
    pwm_pin.duty_ns(pulse_us * 1000) # Use duty_ns with nanoseconds

current_pan_angle = 90
increasing = True

while True:
    try:
        print(f"Setting angle: {current_pan_angle}")
        set_servo_angle(pan_pwm, current_pan_angle)
        if increasing:
            current_pan_angle += 5
            if current_pan_angle >= 170:
                increasing = False
        else:
            current_pan_angle -= 5
            if current_pan_angle <= 10:
                increasing = True
        current_pan_angle = (current_pan_angle) % 180
        sleep(1) # sleep 1sec
    except KeyboardInterrupt:
        break
print("Finished.")