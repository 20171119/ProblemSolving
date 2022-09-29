import math
from collections import defaultdict

def solution(fees, records):
    answer = []
    num2time = defaultdict(list)
    
    for record in records:
        time, number, c = record.split()
        hour, minute = map(int, time.split(":"))
        time = hour*60 + minute
        num2time[number].append(time)
    
    for key, val in sorted(num2time.items()):
        total_time = 0
        if len(val) % 2:
            num2time[key].append(23*60 + 59)
        for i in range(0, len(val), 2):
            total_time += val[i+1] - val[i]
        if total_time < fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil(float(total_time - fees[0]) / fees[2]) * fees[3])
            
    return answer

# 다른사람 풀이
from collections import defaultdict
from math import ceil

class Parking:
    def __init__(self, fees):
        self.fees = fees
        self.in_flag = False
        self.in_time = 0
        self.total = 0

    def update(self, t, inout):
        self.in_flag = True if inout=='IN' else False
        if self.in_flag:  self.in_time = str2int(t)
        else:             self.total  += (str2int(t)-self.in_time)

    def calc_fee(self):
        if self.in_flag: self.update('23:59', 'out')
        add_t = self.total - self.fees[0]
        return self.fees[1] + ceil(add_t/self.fees[2]) * self.fees[3] if add_t >= 0 else self.fees[1]

def str2int(string):
    return int(string[:2])*60 + int(string[3:])

def solution(fees, records):
    recordsDict = defaultdict(lambda:Parking(fees))
    for rcd in records:
        t, car, inout = rcd.split()
        recordsDict[car].update(t, inout)
    return [v.calc_fee() for k, v in sorted(recordsDict.items())]