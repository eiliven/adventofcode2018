import re
import numpy as np
from collections import defaultdict

records_test = """[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up"""
records = records_test.split('\n')

with open('input.txt') as f:
    records = f.readlines()


def half_parse(rec):
    dt, rest = rec.split(']')
    date_year, time = dt.split(' ')
    date = date_year[-5:]
    minutes = time[-2:]

    return date, int(minutes), rest


guard_sleep_time = {}
for r in sorted(records):
    date, minutes, rest = half_parse(r)
    if rest.find('Guard') != -1:
        guard = re.findall(r'\d+', rest)[0]
    if rest.find('falls asleep') != -1:
        asleep = minutes
    if rest.find('wakes up') != -1:
        if guard not in guard_sleep_time:
            guard_sleep_time[guard] = np.zeros(65)
        for m in range(asleep, minutes):
            guard_sleep_time[guard][m] += 1

max_time = 0
max_min = 0
guard = None
for gid, dsm in guard_sleep_time.items():
    guard_max = np.max(dsm)
    if guard_max > max_time:
        max_min = np.argmax(dsm)
        max_time = guard_max
        guard = gid

print(int(guard) * max_min)
