import sh1106
from machine import Pin,I2C
import math
import perlin
import urandom
import time



i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=400000)

oled = sh1106.SH1106_I2C(128, 64, i2c, Pin(16), 0x3c)


num = 20
particles = [num]
noiseScale = 100
noiseStrength = .001
tail = 8

# Grilla baja resolución
cols = 16
rows = 8
cell_w = 128 // cols
cell_h = 64 // rows

t = 0.0



while True:
    oled.fill(0)

    for i in range(cols):
        for j in range(rows):
            # Escala las coordenadas
            x = i * 0.8
            y = j * 0.8
            n = perlin.noise(x, y + t)

            # Umbral para blanco o negro
            color = 1 if n > 0.5 else 0
            oled.fill_rect(i * cell_w, j * cell_h, cell_w, cell_h, color)

    oled.show()
    t += 0.02
    time.sleep(0.05)

 
