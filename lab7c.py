#!/usr/bin/env python3
# Student ID: ateimouri1
class Time:
    """Simple object type for time of the day.
    data attributes: hour, minute, second
    """
    def __init__(self,hour=12,minute=0,second=0):
        """constructor for time object""" 
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'


# def sum_times(t1, t2):
#     """Add two time objests and return the sum."""
#     sum = Time(0,0,0)
#     sum.hour = t1.hour + t2.hour
#     sum.minute = t1.minute + t2.minute
#     sum.second = t1.second + t2.second
#     if sum.second >= 60: #check if the second are 60 or more
#         sum.second -= 60 #if subtract 60 frim seconds and add 1 to minutes
#         sum.minute += 1
#     #check if the minutes are 60 or more
#     if sum.minute >= 60: #if subtract 60 from mintuses and add 1 to hours
#         sum.minute -= 60
#         sum.hour += 1
#     return sum #return the adjust time


def sum_times(t1, t2):
    """Add two time objects and return the sum."""
    t1_seconds = time_to_sec(t1)
    t2_seconds = time_to_sec(t2)
    sum_sec = t1_seconds + t2_seconds
    return sec_to_time(sum_sec)




# def change_time(time, seconds):
#     time.second += seconds #add the given seconds to the time
#     if valid_time(time) != True: #check if the time invalid

#             #adjust the time if second are 60 or more
#             while time.second >= 60:
#                 time.second -= 60
#                 time.minute +=1

#             #adjusy the time if minutes are 60 or more
#             while time.minute >= 60:
#                 time.minute -= 60
#                 time.hour += 1

#             #adjust the time if minutes are negative
#             while time.second < 0: 
#                 time.minute -= 1 
#                 time.second += 60 

#             #adjust the time if minutes are negative
#             while time.minute < 0: 
#                 time.hour -= 1 
#                 time.minute += 60
 
#     return None

def change_time(time, seconds):
    sum_sec_change = time_to_sec(time) + seconds
    new_time = sec_to_time(sum_sec_change)
    time.hour = new_time.hour
    time.minute = new_time.minute
    time.second = new_time.second
    return None

def time_to_sec(time):
    """Convert a time object to a single integer representing the number of seconds from mid-night"""
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def sec_to_time(seconds):
    """Convert a given number of seconds to a time object in hour, minute, second format"""
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


def valid_time(t):
    """check for the validity of the time object attributes:
        24 > hour > 0, 60 > minute > 0, 60 > second > 0 """
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True
