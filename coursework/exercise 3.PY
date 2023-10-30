# write a procedual python program that calculates average of numbers between 1 and 50 and dipslays the results. rewrite the program and convert it into an object oriented program.
# PROCEDUAL APPROACH

total=0
count=0

for num in range(1,51  ):
    total+=num
    count+=1

average=total/count
print("average of numbers between 1 and 50 using procdural approach is :",average)

# OBJECT ORIENTED APPROACH
class Average:
    def __init__(self, start, end):
        self.start=start
        self.end=end

    def cal_average(self):
        total=sum(range(self.start,self.end +1))
        count=self.end-self.start+1
        return total/count
    
calculator=Average(1,50)
average=calculator.cal_average()

print("the average of the numbers between 1 and 50 using the object oriented approach is: ",average)


