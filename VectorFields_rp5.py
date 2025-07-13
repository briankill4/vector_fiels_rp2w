import sh1106
from machine import Pin,I2C
import math
from perlinnoise import PerlinNoise
import urandom
import time

noise = PerlinNoise(seed=42)

i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=400000)

oled = sh1106.SH1106_I2C(128, 64, i2c,  Pin(16), 0x3c)

t = 0
num = 15
particles = []

noiseScale = 50
noiseStrenght = 2

#Generate Particles
for i in range(num):
    valX = urandom.randint(0, 128)
    valY = urandom.randint(0, 64)
    orient= 0
    particles.append([valX,valY])
#    print(particles)

while True:
    oled.fill(0)
    for p in particles:
        x = p[0]
        y = p[1]
        xn = noise.noise(x/noiseScale)
        yn = noise.noise(y/noiseScale)
        x = math.sin(xn)
        y = math.cos(yn)
        xn = max(0, min(127, y))
        yn = max(0, min(63, y))
        oled.pixel(math.floor(xn*30+1), math.floor(yn*30), 1)
    oled.show()
    t += 1
    time.sleep(0.3)