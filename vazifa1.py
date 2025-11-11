cars = {
    "Malibu": 35000,
    "Spark": 12000,
    "Cobalt": 18000,
    "Tracker": 28000
}

eng_qimmat = max(cars, key=cars.get)
eng_arzon = min(cars, key=cars.get)
ortalacha = sum(cars.values()) / len(cars)

print("Eng qimmat:", eng_qimmat)
print("Eng arzon:", eng_arzon)
print("O'rtacha qiymat:", ortalacha)
