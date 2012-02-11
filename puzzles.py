# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="karlo"
__date__ ="$Nov 1, 2011 8:45:24 PM$"

import itertools

def fillTheDots(n):
    consecutiveNumbers = [n,n+1,n+2,n+3,n+4,n+5,n+6,n+7,n+8,n+9,n+10,n+11]
    exp1 = lambda a: a[0]+a[1]+a[2]-a[3]
    exp2 = lambda a: a[0]-a[1]+a[2]*a[3]
    exp3 = lambda a: a[0]-a[1]+a[2]+a[3]
    exp4 = lambda a: a[0]*a[1]-a[2]
    exp5 = lambda a: a[0]-a[1]+a[2]
    exp6 = lambda a: a[0]/a[1]*a[2]
    exp7 = lambda a: a[0]+a[1]*a[2]
    expressions = lambda a: [exp1(a),exp2(a),exp3(a),exp4(a),exp5(a),exp6(a),exp7(a)]
#    expressions = lambda a: [\
#                a[0]+'+'+a[3]+'+'+a[6]+'-'+a[9],
#                a[1]+'-'+a[4]+'+'+a[7]+'*'+a[10],
#                a[2]+'-'+a[5]+'+'+a[8]+'+'+a[11],
#                a[0]+'*'+a[1]+'-'+a[2],
#                a[3]+'-'+a[4]+'+'+a[5],
#                a[6]+'/'+a[7]+'.*'+a[8],
#                a[9]+'+'+a[10]+'*'+a[11]]    
    results = [23,195,28,161,18,0,301]    
    comb = 0
    reduced = []
    for item in itertools.permutations(consecutiveNumbers,4):
#        if item[6] == 0:
#            break
#        exp = expressions(item)
        acctual = exp1(item)
        if acctual == results[0]:
#            print item
            reduced = [x for x in consecutiveNumbers if x not in item]            
            for item in itertools.permutations(reduced,4):
#                print item
                acctual = exp2(item)
#                print acctual
                if acctual == results[1]:
                    print item
                    reduced = [x for x in reduced if x not in item]
                    for item in itertools.permutations(reduced,4):
                        acctual = exp3(item)
                        if acctual == results[2]:
#                            print item
                            reduced = [x for x in reduced if x not in item]
                            for item in reduced:
                                print item,
                    
#        index = 0
        comb = comb + 1
        if comb%1000000 == 0:
            print comb,
#        for expItem in exp:
#            if expItem != results[index]:
#                break
#            index = index + 1
#        if index == 7:
#            return item    
#    return None

def superstition(nums):
    operands = ['+','-','*','/']
    magicNumber = 2012
    operandsNineCombinations = [(a,b,c,d,e,f,g,h,i) for a in operands for b in operands for c in operands for d in operands for e in operands for f in operands for g in operands for h in operands for i in operands]
    for item in operandsNineCombinations:
        index = 0
        expresionList = [str(nums[0])]
        for operand in item:
            expresionList.append(operand)
            expresionList.append(str(nums[index+1]))
            index = index + 1
        sum = eval(''.join(expresionList))
        if sum == magicNumber:
            return item
    return 'No combination for 2012'
if __name__ == "__main__":
#    nums = [11,13,17,19,23,29,31,37,41,43]
#    print superstition(nums)
#    nums = [3,5,7,11,13,17,19,23,29,31]
#    print superstition(nums)    
        print fillTheDots(-11.0)
