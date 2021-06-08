

def file_joining():

    with open('one.txt', 'r') as f1:
        firstfile= frozenset(f1.readlines())
        print(firstfile)
    with open ('two.txt', 'r') as f2:
        secondfile = frozenset(f2.readlines())
        print (secondfile)

    def file_union(firstfile,secondfile):
        thirdfile= (firstfile | secondfile)
        #print(thirdfile)
        return thirdfile

    def file_intersection(firstfile,secondfile):
        thirdfile= (firstfile & secondfile)
        return thirdfile

    def file_difference(firstfile,secondfile):
        thirdfile= ( firstfile - secondfile)
        return thirdfile

    def file_symmetric_difference(firstfile,secondfile):
        thirdfile= (firstfile ^ secondfile)
        return thirdfile 

   
    thirdfile=file_union(firstfile , secondfile)

  
     
    with open ('third.txt', 'w') as f3:
        if thirdfile:
            f3.writelines(sorted(thirdfile))
        else:
            f3.write("\n No new content")


if __name__ =='__main__':
    file_joining()