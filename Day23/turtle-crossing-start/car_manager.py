from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class CarManager:
    def __init__(self):
        self.all_cars = []  # List untuk menyimpan semua mobil
        self.car_speed = STARTING_MOVE_DISTANCE  # Kecepatan awal mobil

    def create_car(self):
        """Membuat mobil baru dengan posisi y yang acak."""
        random_chance = random.randint(1, 6)
        if random_chance == 1:  # Membuat mobil dengan probabilitas rendah agar tidak terlalu banyak
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)  # 20px x 40px
            random_y = random.randint(-250, 250)  # Tidak ada mobil dalam 50px teratas dan bawah
            new_car.goto(300, random_y)  # Semua mobil mulai dari sisi kanan layar
            self.all_cars.append(new_car)

    def move_cars(self):
        """Menggerakkan semua mobil ke kiri."""
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        """Meningkatkan kecepatan mobil setelah level naik."""
        self.car_speed += MOVE_INCREMENT
