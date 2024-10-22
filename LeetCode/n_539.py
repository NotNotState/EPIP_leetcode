

"""def findMinTimeDif_failed(timePoints: list[str]) -> int:
    timePoints = sorted(timePoints)
    print(timePoints)
    start = timePoints[0].split(":")
    end = timePoints[1].split(":")

    end_hours = int(end[0]) * 60 if int(end[0]) != 0 else 24 * 60
    end_minutes= int(end[1]) if int(end[1]) != 0 else 0
    end_total = end_hours + end_minutes

    start_hours = int(start[0]) * 60 if int(start[0]) != 0 else 24 * 60
    start_minutes = int(start[1]) if int(start[1]) != 0 else 0
    start_total = start_hours + start_minutes

    res = abs(end_total - start_total) % (24 * 60)

    print(res)

    return res"""

def return_minutes(time: str) -> int:
    hours, minutes = time.split(":")
    modulus = 24 * 60

    hours = int(hours) * 60 if int(hours) != 0 else modulus
    minutes = int(minutes) if int(minutes) != 0 else 0

    if hours == 24 * 60 and minutes != 0:
        #return (hours + minutes) % (modulus)
        return minutes

    return (hours + minutes)

def findMinTimeDiff(time_points: list[str]) -> int:
    minutes = [int(time[:2]) * 60 + int(time[3:]) for time in time_points]
    minutes.sort()
    sol = min(minutes[i + 1] - minutes[i] for i in range(len(minutes) - 1))
    
    return min(sol, 24*60 - (minutes[-1] - minutes[0])) # the arithmetic accounts for the circular nature of the clock

if __name__ == "__main__":
    #timePoints = ["23:59", "00:00"]
    #timePoints = ["00:00","00:00"]
    #timePoints = ["01:01","02:01","03:00"]
    timePoints = ["12:12","00:13"]

    print(findMinTimeDiff(timePoints))
