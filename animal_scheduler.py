import datetime

our_open_time = datetime.time(8, 0)  # Pet shelter open time
our_close_time = datetime.time(18, 0)  # Pet shelter close time


# make a list of possible book times in with gap of 15 minutes
def generate_booking_times(open_time, close_time, day):
    available_times = []
    current_time = datetime.datetime.combine(day, open_time)
    while current_time.time() < close_time:
        available_times.append(current_time)
        current_time = current_time + datetime.timedelta(minutes=15)
    return available_times


class Animal:
    def __init__(self, name):
        self.name = name
        self.available_schedule_today = generate_booking_times(our_open_time, our_close_time,
                                                               datetime.datetime.today())

    # check which available times meet user's requirements
    def available_booking_times(self, preferable_times: list, booking_duration: int):
        times_list = []
        for available_time in self.available_schedule_today:
            end_time = available_time + datetime.timedelta(minutes=booking_duration)
            if (end_time.time() <= our_close_time and
                    available_time >= preferable_times[0] and
                    end_time <= preferable_times[1]):
                times_list.append(available_time.strftime("%H:%M"))
        return times_list


# create animal object
dog1 = Animal("Bobik")

# user defines his/her free time
from_time = datetime.datetime.combine(datetime.date.today(), datetime.time(12))
to_time = datetime.datetime.combine(datetime.date.today(), datetime.time(15))
time_range = [from_time, to_time]

print(dog1.available_booking_times(time_range, 120))
