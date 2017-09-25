velocity= 0
speed_limit = 60
time = int(input("Time Spent on The Road"))
acceleration = int(input("Acceleration"))
distance = int(input("Distance"))
traveled = velocity * time + 0.5 * acceleration * time**2
limit = time  + 1
for x in range (0, limit):
    reached = velocity * x + 0.5 * acceleration * x**2
    print("Duration :" + str(x) +  "distance :"+int(reached/10)*"*")

if acceleration >= speed_limit:
    print("max speed was " +int(acceleration)+"m/s")
else:
    print("max speed was " +str(acceleration)+"m/s")


if traveled >= distance:
    print("reached "+int(distance)+"m")
else:
    print("reached "+str(distance)+"m")
