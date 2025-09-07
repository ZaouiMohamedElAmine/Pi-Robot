from machine import Pin, PWM
import bluetooth
import time

# Définition des broches GPIO pour les moteurs
IN1 = Pin(25, Pin.OUT)  # GPIO pour IN1
IN2 = Pin(33, Pin.OUT)  # GPIO pour IN2
ENA = Pin(26, Pin.OUT)  # GPIO pour ENA (moteur 1)

IN3 = Pin(32, Pin.OUT)  # GPIO pour IN3
IN4 = Pin(13, Pin.OUT)  # GPIO pour IN4
ENB = Pin(12, Pin.OUT)  # GPIO pour ENB (moteur 2)

# Configuration du Bluetooth
device_name = "ESP32-BT"
bt = bluetooth.Bluetooth()

# Fonction de configuration des PWM
PWM_FREQ = 5000
PWM_RESOLUTION = 8

pwm_ena = PWM(ENA, freq=PWM_FREQ, duty=0)  # PWM pour ENA
pwm_enb = PWM(ENB, freq=PWM_FREQ, duty=0)  # PWM pour ENB

# Initialisation du Bluetooth
bt.active(True)
bt.advertise(100, device_name)

def FORWARD():
    pwm_ena.duty(255)  # Vitesse maximale pour moteur 1
    pwm_enb.duty(255)  # Vitesse maximale pour moteur 2
    IN1.value(1)
    IN2.value(0)
    IN3.value(1)
    IN4.value(0)

def BACKWARD():
    pwm_ena.duty(255)  # Vitesse maximale pour moteur 1
    pwm_enb.duty(255)  # Vitesse maximale pour moteur 2
    IN1.value(0)
    IN2.value(1)
    IN3.value(0)
    IN4.value(1)

def LEFT():
    pwm_ena.duty(255)  # Vitesse maximale pour moteur 1
    pwm_enb.duty(255)  # Vitesse maximale pour moteur 2
    IN1.value(0)
    IN2.value(1)
    IN3.value(1)
    IN4.value(0)

def RIGHT():
    pwm_ena.duty(255)  # Vitesse maximale pour moteur 1
    pwm_enb.duty(255)  # Vitesse maximale pour moteur 2
    IN1.value(1)
    IN2.value(0)
    IN3.value(0)
    IN4.value(1)

def STOP():
    pwm_ena.duty(0)  # Arrêter moteur 1
    pwm_enb.duty(0)  # Arrêter moteur 2
    IN1.value(0)
    IN2.value(0)
    IN3.value(0)
    IN4.value(0)

# Boucle principale
while True:
    if bt.any():
        bt_value = bt.read(1)  # Lire une commande Bluetooth
        bt_value = bt_value.decode('utf-8')  # Décoder la commande reçue
        
        print(bt_value)  # Afficher la commande reçue sur le terminal (facultatif pour débogage)
        
        if bt_value == 'F':  # Commande pour avancer
            FORWARD()
        elif bt_value == 'B':  # Commande pour reculer
            BACKWARD()
        elif bt_value == 'L':  # Commande pour tourner à gauche
            LEFT()
        elif bt_value == 'R':  # Commande pour tourner à droite
            RIGHT()
        elif bt_value == 'S':  # Commande pour arrêter
            STOP()
        else:
            STOP()  # Arrêter le robot si la commande est inconnue

    time.sleep(0.1)  # Délai pour éviter la surcharge du processeur
