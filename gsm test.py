import serial
import time

def send_at_command(command, expected_response, timeout=2):
    ser.write((command + "\r\n").encode())
    time.sleep(timeout)
    response = ser.read_all()
    try:
        response_text = response.decode('utf-8')
    except UnicodeDecodeError:
        response_text = response.decode('latin1')
    print(f"Response: {response_text}")

    if expected_response in response_text:
        return True, response_text
    return False, response_text


ser = serial.Serial('/dev/ttyS3', 19200, timeout=1)
time.sleep(2)


success, response = send_at_command('AT+CSQ', "OK")
print("Signal Quality:", response)


success, response = send_at_command('AT+CGREG?', "OK")
print("Network Registration Status:", response)


success, response = send_at_command('AT+SAPBR=0,1', "OK")
print("Delete Bearer Profile:", response)


success, response = send_at_command('AT+SAPBR=3,1,"CONTYPE","GPRS"', "OK")
print("Set Bearer Profile Type:", response)

success, response = send_at_command('AT+SAPBR=3,1,"APN","internet"', "OK")
print("Set APN:", response)

success, response = send_at_command('AT+SAPBR=3,1,"USER",""', "OK")
print("Set APN User:", response)

success, response = send_at_command('AT+SAPBR=3,1,"PWD",""', "OK")
print("Set APN Password:", response)


success, response = send_at_command('AT+SAPBR=1,1', "OK", 10)
print("Open GPRS connection:", response)


success, response = send_at_command('AT+SAPBR=2,1', "OK")
print("GPRS Bearer Status:", response)


success, response = send_at_command('AT', "OK")
print("Module Status:", response)


ser.close()
