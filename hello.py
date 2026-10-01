#print("rayan")
#print("CST1510")
#print("=" * 50)
#print(" rayan")
#print("=" * 50)
#print("ID\tSTATUS\nR-004\tOK")
#print("rayan, CST1510")
#student_name = "rayan"
#course_code = "CST1510"
#print(f"{student_name}, {course_code}")

student_name = "rayan"
course_code = "CST1510"
print(student_name, course_code)

print("20" + "20")
print(20 + 20)


x = "srv-01"
y = 87
z = 100
print(x, y, z)

sensor_text = "srv-01"
sensor_value = 87
sensor_reading = 100
print(sensor_text, sensor_value, sensor_reading)


a = 5
b = 10
a = b
b = 3
print(a, b)


a = 5
b = 10
a = b
b = 3
print(a, b)
print("10 3")


total_seconds = 500
minutes = total_seconds // 60
seconds = total_seconds % 60

total_seconds = 9137

hours = total_seconds // 3600
remaining = total_seconds % 3600

minutes = remaining // 60
seconds = remaining % 60

print((10 + 6) / 2)


used_gb = 87
total_gb = 120

percentage_used = (used_gb / total_gb) * 100
remaining_gb = total_gb - used_gb
print(percentage_used)


total = 100
total -=30
total *= 2
print(total)


name = "Rayyan"

print("=" * 30)
print(f"cst1510 - {name}")
print("=" * 30)

label = input("Enter label: ")
part = float(input("Enter part: "))
total = float(input("Enter total: "))

percentage = (part / total) * 100

print(f"{label:<15} : {part:.0f} of {total:.0f} = {percentage:.1f} %")

record_id = input("Enter Record ID: ")
value = float(input("Enter Value: "))
limit = float(input("Enter Limit: "))

difference = value - limit
percentage = (value / limit) * 100

print("Record ID:", record_id)
print("Difference:", difference)
print(f"Percentage of limit: {percentage:.1f}%")