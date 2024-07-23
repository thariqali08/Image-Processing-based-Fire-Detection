import urequests
import time
import machine
import network

ssid = "ECE Dept Wi-Fi 1"
password = "Wifi-1@Ece"

# Connect to Wi-Fi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

while not wlan.isconnected():
    time.sleep(1)
    print("Connecting to Wi-Fi...")

print("Connected to Wi-Fi")
print('network config:', wlan.ifconfig())
# Define GPIO pins for LED and Buzzer
led_pin = machine.Pin(1, machine.Pin.OUT)  # Use built-in LED pin
buzzer_pin = machine.Pin(0, machine.Pin.OUT)  # Adjust as needed

def check_fire_status():
    # Send HTTP GET request to the Flask server
    response = urequests.get("http://192.169.74.202:5000/check_fire")
    data = response.json()  # Get the JSON data from the response
    response.close()  # Close the response
   
    # Check the status from the server
    status = data.get("status", "No fire detected")
   
    if status == "Fire detected":
        # Turn on the LED and Buzzer
        print("Fire Detected")
        led_pin.on()
        buzzer_pin.on()
    else:
        print("No Fire Detected")
        # Turn off the LED and Buzzer
        led_pin.off()
        buzzer_pin.off()

while True:
    # Check fire status and act accordingly
    check_fire_status()
    time.sleep(2)  # Check every 2 seconds
