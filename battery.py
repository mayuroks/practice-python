#! /usr/bin/python3.3
import math
#data = [5, 8, 13, 27, 14]
#data = [10,10]
#data = [3,1]
#data = [12, 30, 30, 32, 42, 49]
#data = [5, 5, 6, 5]
data = [33,38,25,5,40,46,7,27]



l1, l2 = [], []

data.sort()
data = data[::-1]
threshhold = sum(data) / 2
#print('THRESH : ',threshhold, "\n")
sum1,sum2,sum3 = 0,0,0

#print("DATA : ", data)
res = []
l1 = list(data)

def knap_sack(list, thresh, start = 0):
        new_start = 0
        if thresh  < min(list):
        #       print('FINISH','AVG : ',thresh)
                return 0

        res.append(start)
        list.remove(start)

        # find new start point :: new_start = i
        for i in list:
                if i <= (thresh - start) :
        #               print('RECURSE',' THRESH : ',thresh," REMOVED : ",start," new_start : ",i," list1 : ",list)
                        new_start = i
                        break
        return start + knap_sack(list, thresh - start, new_start)

#print('KNAP : ',knap_sack(l1, threshhold), "RESULT : ",res)

answer = []
for i in data:
        l1 = list(data)
        res=[]
        l2.append(i)
        #print('KNAP : ',knap_sack(l1, threshhold, i), "RESULT : ",res,"\n\n")
        answer.append(knap_sack(l1, threshhold, i))
print(sum(data) - 2*max(answer))
#print("LIST : ", l2)

#print(min(math.fabs((sum1 - sum3 + sum1)),math.fabs((sum2 - sum3 + sum2))))
