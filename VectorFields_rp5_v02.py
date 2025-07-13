import sh1106
from machine import Pin,I2C
import math
import perlin
import urandom
import time

i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=400000)

oled = sh1106.SH1106_I2C(128, 64, i2c, Pin(16), 0x3c)

width = 128
height = 64
t = 0
num = 20
particles = []

noiseScale = 100		
noiseStrength = 4
tail = 8

class Particle:
    def __init__(self, x, y, speed):
        self.loc_x = x
        self.loc_y = y
        self.speed = speed
        self.dir_x = 1
        self.dir_y = 0

    def run(self):
        self.move()
        self.check_edges()
        self.update()

    def move(self):
        n = perlin.noise(self.loc_x / noiseScale, self.loc_y / noiseScale,t)
        angle = n * 2 * math.pi * noiseStrength
        self.dir_x = math.cos(angle)
        self.dir_y = math.sin(angle)

        vel_x = self.dir_x * self.speed
        vel_y = self.dir_y * self.speed

        self.prev_x = self.loc_x
        self.prev_y = self.loc_y

        self.loc_x += vel_x
        self.loc_y += vel_y

    def update(self):
        x2 = int(self.loc_x)
        y2 = int(self.loc_y)
        oled.pixel(x2, y2, 1)

        #oled.line(x1, y1, x2, y2, 1)
        
    def check_edges(self):
        if (self.loc_x < 0 or
            self.loc_x > width or
            self.loc_y < 0 or
            self.loc_y > height):

            self.loc_x = urandom.uniform(0, width * 1.2)
            self.loc_y = urandom.uniform(0, height)

        
for i in range(num):
    x = urandom.randint(0, 128)
    y = urandom.randint(0, 64)
    speed = urandom.uniform(.3, 4.0)
    p = Particle(x, y, speed)
    particles.append(p)

while True:
    oled.fill(0)
    for j in range(tail):
        for p in particles:
            p.run()
    oled.show()
    time.sleep(0.06)
