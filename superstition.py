# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="karlo"
__date__ ="$Nov 1, 2011 8:45:24 PM$"

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
    nums = [11,13,17,19,23,29,31,37,41,43]
    print superstition(nums)
    nums = [3,5,7,11,13,17,19,23,29,31]
    print superstition(nums)
