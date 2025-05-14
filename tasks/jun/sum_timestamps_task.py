

def sum_timestamps(sequence):
    if len(sequence) == 1:
        for timestamp in sequence:
            if len(timestamp.split(":")) == 3:
                hours, minutes, seconds = timestamp.split(":")
                return f"{int(hours)}:{int(minutes):02d}:{int(seconds):02d}"
            elif len(timestamp.split(":")) == 2:
                minutes, seconds = timestamp.split(":")
                return f"{int(minutes)}:{int(seconds):02d}"

    hours_l = []
    minutes_l = []
    seconds_l = []
    for timestamp in sequence:
        if len(timestamp.split(":")) == 2:
            minutes, seconds = timestamp.split(":")
            minutes_l.append(int(minutes))
            seconds_l.append(int(seconds))

        elif len(timestamp.split(":")) == 3:
            hours, minutes, seconds = timestamp.split(":")
            hours_l.append(int(hours))
            minutes_l.append(int(minutes))
            seconds_l.append(int(seconds))
    
    result_seconds = sum(seconds_l)
    if result_seconds >= 60:
        minutes_l.append(result_seconds // 60)
        result_seconds = result_seconds - (result_seconds // 60 * 60)

    result_minutes = sum(minutes_l)
    if result_minutes >= 60:
        hours_l.append(result_minutes // 60)
        result_minutes = result_minutes - (result_minutes // 60 * 60)

    if hours_l:
        return f"{sum(hours_l)}:{result_minutes:02d}:{result_seconds:02d}"
        
    return f"{result_minutes}:{result_seconds:02d}"


# '10:20'
# print(sum_timestamps(['02:32', '04:48']))
# print(sum_timestamps(['05:02']))
# print(sum_timestamps(['15:32', '45:48']))
print(sum_timestamps(['02:01', '04:05'])) # 6:06


# sequence = ['6:35:32', '2:45:48', '40:10']
# def result(sequence):
#     for i in sequence:
#         if len(i.split(":")) == 3:
#             print("hour")
#         elif len(i.split(":")) == 2:
#             print("minute")


print(sum_timestamps(['6:35:32', '2:45:48', '40:10']))