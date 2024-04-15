def hour_minute_angle(hour, minute):
    angle = minute/60*360
    angle1 = hour/12*360
    if angle1 - angle < 0:
        return (angle1 - angle) + 360
    return angle1 - angle

print(hour_minute_angle(hour=6, minute=30.5))
    
