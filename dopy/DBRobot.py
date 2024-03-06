import socket
import time



__author__ = "Chanwool Kim Lunalabs in Republic of Korea"
__copyright__ = "Copyright 2024. Chanwool Kim(Lunalabs). All rights reserved"
__license__ = "LGPLv3"


class RobotException(Exception):
    pass
    
class DBRobot:
    def __init__(self, host=192.168.5.1, port=29999):
        self.host = host
        self.port = port
        self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.soc.connect((self.host, self.port))

    def send_command(self, cmd):
        print(f"Sending command: {cmd}")
        self.soc.sendall(cmd.encode())
        
        # wait robot response
        data = self.soc.recv(1024)
        print(f"Received: {data.decode()}")

    def PowerOn(self, wait=10):
        self.send_command('PowerOn()')
        time.sleep(wait)  # wait robot power on

    def EnableRobot(self):
        self.send_command('EnableRobot()')

    def DisableRobot(self):
        self.send_command('DisableRobot()')

    def ClearError(self):
        self.send_command('ClearError()')
        
    def MovJ(self, pose):
        self.send_command(f'MovJ({pose})')
        
    def MovL(self, pose):
        self.send_command(f'MovL({pose})')
        
    def StartDrag(self):
        self.send_command('StartDrag()')
        
    def StopDrag(self):
        self.send_command('StopDrag()')