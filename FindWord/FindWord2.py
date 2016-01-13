__author__ = 'Anup'

wordMatrix = [
    ['A', 'C', 'C', 'F', 'F', 'F'],
    ['H', 'A', 'I', 'I', 'I', 'D'],
    ['N', 'S', 'T', 'X', 'T', 'R'],
    ['U', 'T', 'P', 'U', 'U', 'Y'],
    ['S', 'P', 'I', 'N', 'T', 'K']
]

wordMatrix2 = [
    ['A', 'A', 'C'],
    ['H', 'A', 'I'],
    ['N', 'S', 'T'],
    ['U', 'T', 'P'],
    ['S', 'U', 'P']
]

findMatrix = ["RUN","FIX","CITY", "PUN", "SUN","PINT"]


# print findMatrix[1]
# print wordMatrix[0][1]
# print "row "+str(len(wordMatrix))
# print "col"+str(len(wordMatrix[0]))


def filterSomething(param):
    if param < len(wordMatrix):
        return True
    else:
        return False


def travLeftToright(target):
    length = len(wordMatrix[0])
    height = len(wordMatrix)
    heightCount = 0
    targetLength = len(target)
    posCount = 0
    row = -1
    pos = []

    if targetLength > length:
        return
    else:
        for j in range(len(wordMatrix)):
            row = j
            # for letterIndex in range(target):
            count = 0
            posCount=0
            for i in wordMatrix[j]:
                if length - posCount < targetLength-count:
                    break
                count += 1
                posCount += 1
                if i != target[count - 1]:
                    count = 0
                    pos[:] = []
                    continue
                else:
                    pos.append(posCount)
                    # pos[posCount]=count

                if count == targetLength:
                    print "row " + str(row+1) + " Col " + str(pos)+" word "+target+" Direction L-R"
                    return True



def travTopToDown(target):

    length = len(wordMatrix[0])
    height = len(wordMatrix)
    heightCount = 0
    targetLength = len(target)
    posCount = 0
    col = -1
    pos = []
    if targetLength > height:
        return
    else:
        for j in range(len(wordMatrix[0])):
            col = j
            # for letterIndex in range(target):
            count = 0
            posCount=0
            for i in range(len(wordMatrix)):
                if height - posCount < targetLength-count:
                    break
                count += 1
                posCount += 1
                if wordMatrix[i][j] != target[count - 1]:
                    count = 0
                    pos[:] = []
                    continue
                else:
                    pos.append(posCount)
                    # pos[posCount]=count

                if count == targetLength:
                    print "Col " + str(col+1) + " Row " + str(pos)+" word "+target+" Direction T-B"
                    return True


def travRightDignal(target):
    length = len(wordMatrix[0])
    height = len(wordMatrix)
    heightCount = 0
    targetLength = len(target)
    posCount = 0
    temprow = -1
    digCount=0
    pos = []
    if targetLength > height:
        return
    else:
     for row in range(len(wordMatrix)):
        temprow = row
            # for letterIndex in range(target):
        count = 0
        posCount=0
        digCount=0
        matchCount=0
        col=0
        while col < len(wordMatrix[0]):
            if length - col < targetLength-count or height-row <targetLength-count:
                    break
            if count==0:
              if wordMatrix[row][col]==target[count]:
                  pos.append(str(row+1)+" "+str(col+1))
                  count+=1
                  matchCount+=1
              else :
                   pos[:] = []


            else:
                if wordMatrix[row+count][col]==target[count] :
                    pos.append(str(row+count+1)+" "+str(col+1))
                    count+=1
                else:
                    col=col-count
                    count=0
                    pos[:] = []
                    # pos[posCount]=count
            col+=1
            if count == targetLength:
                    print str(pos)+ " word "+target +" Direction R-D"
                    return True



def travBottToTop(target):
    length = len(wordMatrix[0])
    height = len(wordMatrix)
    heightCount = 0
    targetLength = len(target)
    posCount = 0
    tempcol = -1
    digCount=0
    actrowcount=targetLength
    pos = []
    if targetLength > height:
        return
    else:
     for it in range((len(wordMatrix)-len(target))+1):
        for col in range(len(wordMatrix[0])):

          tempcol = col
            # for letterIndex in range(target):
          count = 0
          posCount=0
          digCount=0
          row=0

          while row < len(wordMatrix):
            if count==0:
              if row+1<actrowcount:
               row+=1
               continue

            if wordMatrix[row][col]==target[count]:
                  pos.append(str(row+1))
                  count+=1
                  row-=1

            else :
                   pos[:] = []
                   count=0
                   break
          #row+=1
            if count == targetLength:
                    print "Col "+str(tempcol+1)+" "+str(pos)+ " word "+target+" Direction B-T"
                    return True

        actrowcount+=1


def travLeftDignal(target):
    length = len(wordMatrix[0])
    height = len(wordMatrix)
    heightCount = 0
    targetLength = len(target)
    posCount = 0
    temprow = -1
    digCount=0
    actCol=0
    pos = []
    if targetLength > height:
        return
    else:
     for row in range(len(wordMatrix)):
       temprow = row
            # for letterIndex in range(target):
       count = 0
       posCount=0
       digCount=0
       matchCount=0
       col=0
       actCol=0
       if height-row<targetLength :
        return
       while col < len(wordMatrix[0]):
            #if count==0:
            if row+count > len(wordMatrix)-1:
               break
            if count==0:
              if  col < targetLength-1:
                  actCol+=1
                  col+=1
                  continue

            if count==0:
              if wordMatrix[row][col]==target[count]:
                  pos.append(str(row+1)+" "+str(col+1))
                  count+=1
                  matchCount+=1
              else :
                   pos[:] = []


            else:
                if wordMatrix[row+count][col]==target[count] :
                    pos.append(str(row+count+1)+" "+str(col+1))
                    count+=1
                else:
                    col=actCol
                    count=0
                    pos[:] = []
                    # pos[posCount]=count
            if count!=0:
              col-=1
            else :
              col+=1
              actCol+=1
            if count == targetLength:
                    print str(pos)+ " word "+target+" Direction L-D"
                    return True






#print travLeftToright(findMatrix[3])
#print travTopToDown(findMatrix[0])
#print travLeftDignal(findMatrix[1])
#print travBottToTop(findMatrix[4])
#print travRightDignal(findMatrix[0])
# travLeftToright(findMatrix[0])

def findWords():

    for word in findMatrix:
        if travLeftToright(word):
            print
        elif  travTopToDown(word) :
            print
        elif travBottToTop(word):
            print
        elif travLeftDignal(word):
            print
        else:
            travRightDignal(word)



findWords()


