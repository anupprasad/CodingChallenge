__author__ = 'Anup'

numberOfLines=int(raw_input("Please Inter First Line "))
inputMatrix=[]
for i in range(numberOfLines):
    line=raw_input("Please Inter "+str(i) +"row ")
    values=line.split(" ")
    tempMatrix=[]
    for j in values:
        tempMatrix.append(int(j))
    inputMatrix.append(tempMatrix)

kIndices=int(raw_input("please inter indices "))

def calManhattan(x1,y1,x2,y2):
  dist= abs(x2-x1)+abs(y2-y1)
  return dist

def checkForDuplicate():

    totalRow=len(inputMatrix)
    col=0
    if totalRow==0:
	  print "NO"
	  return
    notFound=False
    found=False
    for i in range(totalRow):
        if found:
            break
        for col in range(totalRow):
         notFound=False

         if found:
                break;
         for k in range(i,totalRow):
            if notFound:
                notFound=False;
                break
            if found:
                break;
            colLen=len(inputMatrix[i])

            for j in range(colLen):

               dist=calManhattan(i,col,k,j)
               """
               if dist>kIndices:
                   notFound=True
                   break
               """
               if dist!=0 and inputMatrix[i][col]==inputMatrix[k][j]:
                   print "YES"
                   found=True;
                   break;

    if not found:
        print "NO"


checkForDuplicate()




