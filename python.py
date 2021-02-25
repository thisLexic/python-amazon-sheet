# list - maximum, minimum, length, list comprehension, all/any, sort
max([1,2,3]) # error when list is empty
min([1,2,3]) # error when list is empty
len([1,2,3])

[x for x in fruits if "a" in x]

all([True, True, False]) # all items in a list are true
any([True, True, False]) # any of the items in a list are true
not any([True, True, False]) # all items in a list are false

[1,2,3].sort()
intervals.sort(key = lambda x: x[0]) # sort a list of lists



# parenthesis

class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        o = ["[", "(", "{"]
        c = ["]", ")", "}"]
        for p in s:
            if p in o:
                l.append(p)
            else:
                if len(l) == 0:
                    return False
                
                left = l.pop()
                if left == "(" and p == ")":
                    continue
                elif left == "{" and p == "}":
                    continue
                elif left == "[" and p == "]":
                    continue
                else:
                    return False
        if len(l) == 0:
            return True
        else:
            return False



# palindromes (inefficient)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        sLen = len(s)        
        longest = ""
        for i1 in range(sLen):
            for i2 in range(sLen, i1, -1):
                testPal = s[i1:i2]
                if testPal == testPal[::-1]:
                    if len(testPal) > len(longest):
                        longest = testPal
        return longest

# sudoku checker
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row check
        for row in board:
            used = []
            for item in row:
                if item in used and item != ".":
                    return False
                else:
                    used.append(item)
                    
        # column check
        for iCol in range(9):
            used = []
            for iItem in range(9):
                item = board[iItem][iCol]
                if item in used and item != ".":
                    return False
                else:
                    used.append(item)
                    
        # box check
        for row in range(0, 9, 3):
            for column in range(0, 9, 3):
                used = []
                for x in range(3):
                    for y in range(3):
                        item = board[row+x][column+y]
                        if item in used and item != ".":
                            return False
                        else:
                            used.append(item)
            
                    
        return True


# validate binary tree node
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return validate(self, root, None, None)
    
    def validate(self, root: TreeNode, maxi: int, mini: int) -> bool:
        if root == None:
            return True
        elif (maxi != None and maxi <= root.val) or (mini != None and mini >= root.val):
            return False
        else:
            return Solution.validate(self, root.left, root.val, mini) and Solution.validate(self, root.right, maxi, root.val)

# combination sum

class Solution(object):
    def combinationSum(self, candidates, target):
        table = [[] for _ in range(target + 1)]
        
        for c in candidates:
            for t in range(target+1):
                if c > t:
                    continue
                elif c == t:
                    table[t].append([c])
                else:
                    for sList in table[t-c]:
                        table[t].append(sList + [c])
        
        return table[t]

# permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        self.getPermute(answer, [], nums)
        return answer
    
    def getPermute(self, answer, current, left):
        if len(left) == 0:
            answer.append(current)
            return
        else:
            for last in left:
                leftLess = left[:]
                leftLess.remove(last)
                self.getPermute(answer, current + [last], leftLess)

# sort lists within a list, merge intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        output = []
        start = intervals[0][0]
        end = intervals[0][1]
        for interval in intervals[1:]:
            iStart = interval[0]
            iEnd = interval[1]
            if iStart >= start and iStart <= end:
                if iEnd > end:
                    end = iEnd
            elif iStart < start and iEnd >= end:
                start = iStart
                end = iEnd
            else:
                output.append([start, end])
                start = iStart
                end = iEnd
        output.append([start, end])
        return output



