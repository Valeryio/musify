
miliseconds = 223352 / 1000
minutes = str(miliseconds / 60)
time_track = []

seconds = int(minutes.split('.')[1][:2])
minutes = int(minutes.split('.')[0])

if seconds > 60:
    minutes += 1
    seconds -= 60

time_track.append(str(minutes))
time_track.append(str(seconds))
track_time = ':'.join(time_track)

