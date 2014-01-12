# Import modul webiopi
import webiopi

# Memanggil library GPIO
GPIO = webiopi.GPIO

# -------------------------------------------------- #
# Mendefinisikan GPIO                                #
# -------------------------------------------------- #

# GPIO untuk Motor Kiri
L1=22 # H-Bridge Input Pin 1
L2=23 # H-Bridge Input Pin 2


# GPIO untuk Motor Kanan
R1=24 # H-Bridge Input Pin 3
R2=25 # H-Bridge Input Pin 4


# -------------------------------------------------- #
# Membuat Fungsi Motor Kiri                          #
# -------------------------------------------------- #

def left_stop():
    GPIO.output(L1, GPIO.LOW)
    GPIO.output(L2, GPIO.LOW)

def left_forward():
    GPIO.output(L1, GPIO.HIGH)
    GPIO.output(L2, GPIO.LOW)

def left_backward():
    GPIO.output(L1, GPIO.LOW)
    GPIO.output(L2, GPIO.HIGH)

# -------------------------------------------------- #
# Membuat Fungsi Motor Kanan                         #
# -------------------------------------------------- #
def right_stop():
    GPIO.output(R1, GPIO.LOW)
    GPIO.output(R2, GPIO.LOW)

def right_forward():
    GPIO.output(R1, GPIO.HIGH)
    GPIO.output(R2, GPIO.LOW)

def right_backward():
    GPIO.output(R1, GPIO.LOW)
    GPIO.output(R2, GPIO.HIGH)

# -------------------------------------------------- #
# Definisi Macro untuk JavaScript                    #
# -------------------------------------------------- #

def go_forward():
    left_forward()
    right_forward()

def go_backward():
    left_backward()
    right_backward()

def turn_left():
    left_forward()
    right_backward()

def turn_right():
    left_backward()
    right_forward()

def stop():
    left_stop()
    right_stop()
    
# -------------------------------------------------- #
# Inisialisasi                                       #
# -------------------------------------------------- #

# Setup GPIO

GPIO.setFunction(L1, GPIO.OUT)
GPIO.setFunction(L2, GPIO.OUT)

GPIO.setFunction(R1, GPIO.OUT)
GPIO.setFunction(R2, GPIO.OUT)



# -------------------------------------------------- #
# Membuat Web Server                                 #
# -------------------------------------------------- #


# Menempatkan web server pada port 8000, dan membuat ID dan password
server = webiopi.Server(port=8000, login="cambot", password="cambot")

# Mendaftarkan Macro untuk dipanggil pada javascript di HTML

server.addMacro(go_forward)
server.addMacro(go_backward)
server.addMacro(turn_left)
server.addMacro(turn_right)
server.addMacro(stop)

# -------------------------------------------------- #
# Me-Loop Program Web Server                         #
# -------------------------------------------------- #

# Menjalankan Loop sampai CTRL+C ditekan atau Raspberry direstart
webiopi.runLoop()

# -------------------------------------------------- #
# Mematikan Program Web Server                                   #
# -------------------------------------------------- #

# Stop Web server
server.stop()

# Mengatur Ulang fungsi GPIO
GPIO.setFunction(L1, GPIO.IN)
GPIO.setFunction(L2, GPIO.IN)

GPIO.setFunction(R1, GPIO.IN)
GPIO.setFunction(R2, GPIO.IN)


