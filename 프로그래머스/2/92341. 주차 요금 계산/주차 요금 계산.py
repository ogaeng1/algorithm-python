from collections import defaultdict

def solution(fees, records):
    answer = []
    parking_time = defaultdict(int)
    in_out_info = defaultdict(int)
    
    for i in records:
        time, car_number, in_out = i.split(' ')
        
        h = int(time[:2])
        m = int(time[3:])
        convert_time = h * 60 + m
        
        if in_out == 'IN':
            in_out_info[car_number] = convert_time
        else:
            parking_time[car_number] += convert_time - in_out_info[car_number]
            del in_out_info[car_number]
    
    max_time = 23 * 60 + 59
    
    for i, j in in_out_info.items():
        parking_time[i] += max_time - j
        
    for i, j in sorted(parking_time.items()):
        fee = 0
        
        if j <= fees[0]:
            fee = fees[1]
        else:
            fee = fees[1] + ((j - fees[0] - 1) // fees[2] + 1) * fees[3]
            
        answer.append(fee)
    
    return answer