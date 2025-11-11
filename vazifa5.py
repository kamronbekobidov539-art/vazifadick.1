car_count = {
    "Chevrolet": 120,
    "Toyota": 95,
    "BMW": 60,
    "Kia": 75
}

eng_kop = max(car_count, key=car_count.get)
eng_kam = min(car_count, key=car_count.get)

print("Eng ko'p sotilgan:", eng_kop)
print("Eng kam sotilgan:", eng_kam)
