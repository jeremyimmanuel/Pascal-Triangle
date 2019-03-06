'''
Created by Jeremy Tandjung
03/05/2019
'''

'''
INPUT: The number of rows of the pascal triangle
RETURNS: A 2D array representation of a pascal triangle
'''
def createPascal(numRows):
    #Return values for 1 row and 2 rows
    if numRows == 1:    
        return [[1]]
    elif numRows == 2:
        return [[1],[1,1]]

    #If input is more than 2 rows
    pascal = [[1],[1,1]]
    while(len(pascal) < numRows):   
        row = [1]   #The edge of each row will always be one

        #Calculate values of row based on previous row's values
        prev = pascal[len(pascal)-1]
        for i in range(1, len(prev)):
            row.append(prev[i] + prev[i-1])
        row.append(1)
        pascal.append(row)

    return pascal

'''
Recursive version of the creation of pascal's triangle
INPUT: Number of rows
RETURNS: A 2D array representation of pascal's triangle
'''
def createPascalR(numRows):
    if(numRows == 1):
        return [[1]]

    def helper(numRows, p):
            if(numRows == 2):
                p.append([1,1])
                return [1,1]
        
            prev = helper(numRows-1, p) #get previous pascal row
            
            ans = [1]
            for i in range(1, len(prev)):
                ans.append((prev[i] + prev[i-1]))
            ans.append(1)
            p.append(ans)
            return ans
    
    pascal = [[1]]
    helper(numRows, pascal)
    return pascal
