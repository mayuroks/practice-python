#lint:enable
#lint:disable
#! /usr/bin/python3.3
import math
#data = [5, 8, 13, 27, 14]
#data = [10,10]
#data = [3,1,1]
#data = [12, 30, 30, 32, 42, 49]
#data = [5, 5, 6, 5]
data = [33,38,25,5,40,46,7,27]



l1, l2 = [], []

data.sort()
data = data[::-1]
threshhold = sum(data) // 2
print('THRESH : ',threshhold, "\n")
sum1,sum2,sum3 = 0,0,0

print("DATA : ", data)
res = []
l1 = list(data)

answer = []
def knap_sack(list, thresh, start = 0):
        new_start = 0
        if thresh  >= min(list):
           print('FINISH','THRESH : ',thresh)
            #return 0
        if sum(res) > thresh:
            print('TRAP : ', res,start)
            return
        res.append(start)
        list.remove(start)


        # find new start point :: new_start = i
        for i in list:
                if i <= (thresh - start):
        	           print('RECURSE',' THRESH : ',thresh," REMOVED : ",start," new_start : ",i," list1 : ",list)
        	           new_start = i
        	           new_thresh = thresh - new_start
        	           knap_sack(list, new_thresh, new_start)
        	           print("ANSWER : ", sum(res))
#print('KNAP : ',knap_sack(l1, threshhold), "RESULT : ",res)


for i in data:
        l1 = list(data)
        res=[]
        l2.append(i)
        print('KNAP =========================== : ',l2,knap_sack(l1, threshhold, i), "RESULT : ",sum(res),"\n\n")
        answer.append(sum(res))
        print('FINAL ANSWER : ', math.fabs(sum(data) - 2*max(answer)))
#print(sum(data) - 2*max(answer))
#print("LIST : ", l2)

#print(min(math.fabs((sum1 - sum3 + sum1)),math.fabs((sum2 - sum3 + sum2))))
