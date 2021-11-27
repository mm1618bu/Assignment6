class Location:
    def __init__(self,row=0,column=0,maxValue=0):
        self.row = row
        self.column = column
        self.maxValue = maxValue

    def __str__(self):
        return "(Row : "+str(self.row)+" Column : "+str(self.column)+" Value : "+str(self.maxValue)+")";


def locateLargest(a):
    r=0
    c=0
    m=-1
    for i in range(len(a)):
        for j in range(len(a[0])):
#update maximum
            if a[i][j]>a[r][c]:
                r = i
                c = j
    return Location(r,c,a[r][c])
  
print('Enter the number of rows and columns in the list: ',end='');
data = input().strip().split(',')
rows = int(data[0].strip())
cols = int(data[1].strip())

ans = list()
for i in range(rows):
    print('Enter row '+str(i)+': ',end='')
    data = input().strip().split()
    l = []
    for x in data:
        l.append(float(x))
    ans.append(l)

loc = locateLargest(ans)
print('The location of the largest element is at ('+str(loc.row)+', '+str(loc.column)+')')
