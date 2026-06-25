import math 
print("="*25)
print("Orbital Trajectory Simulator")
print("="*25) 


print("\n Select Environment")
print("Mercury-1")
print("Venus-2")
print("Earth-3")
print("Mars -4")
print("Jupiter-5")
print("Saturn-6")
print("Uranus-7")
print("Neptune-8")
print("Sun-0")

planet=input("Choose Celestial no: ")
speed = float(input("Speed (m/s): "))
angle = float(input("Launch angle (degrees): "))






if planet =="1":
    g= 3.70
elif planet == "2":
    g=8.87
elif planet == "3":
    g=9.81
elif planet == "4":
    g=3.71
elif planet == "5":
    g=24.79
elif planet == "6":
    g=10.44
elif planet == "7":
    g=8.69
elif planet == "8":
    g=11.15
else:
    g= 274


angle_rad = math.radians(angle)
vx = speed * math.cos(angle_rad)
vy = speed * math.sin(angle_rad)

time = (2 * vy) / g
range_distance = vx * time
max_height = (vy ** 2) / (2 * g)

print("\nRESULTS")

print(f"Planet: {planet}")
print(f"Horizontal Velocity: {vx:.2f} m/s")
print(f"Vertical Velocity: {vy:.2f} m/s")
print(f"Time of flight: {time:.2f}s")
print(f"Max Height: {max_height:.2f}m")
print(f"Range: {range_distance:.2f} m")




