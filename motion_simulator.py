print("="*35)
print("Motion Simulator")
print("="*35)

u= float(input("Iitial velocity (m/s): "))
a= float(input("Acceleration (m/s^2): "))
t= float(input("Time (s): "))
               
v= u + a*t     
s= u*t + 0.5*a*t**2
Av= (u + v)/2
print("\nSimulation Complete")
print("----------------")
print(f"Final Velocity: {v:.2f} m/s")
print(f"Distance: {s:.2f} m")
print(f"Average Velocity: {Av:.2f} m/s")

      