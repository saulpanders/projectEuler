# @saulpanders
# ex_018.py 
# 
# Q:  Find the maximum total from top to bottom of the triangle

# idea: represent triangle as a binary tree and check sum of max path from root to leaves (can be greedy!)
# idea: can be a bit greedy here I think
# notice that we can use dynamic programming to store sub-paths sums
'''
if we start at the farthest left corner and consider just the subtriangle made up of the leaves and their common node, we can calculate the 
max path of that subtriangle

then, at each new "row" of triangle added, we only need to consider the potential paths from this new row


represent triangle as a triangular array, then we can use binary tree traversal strats!

'''

n=15

triangle_tree = [
[75, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[95, 64, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[17, 47, 82, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[18, 35, 87, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[20, 4, 82, 47, 65, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[19, 1, 23, 75, 3, 34, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[88, 2, 77, 73, 7, 63, 67, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[99, 65, 4, 28, 6, 16, 70, 92, 0, 0, 0, 0, 0, 0, 0, 0],
[41, 41, 26, 56, 83, 40, 80, 70, 33, 0, 0, 0, 0, 0, 0, 0],
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29, 0, 0, 0, 0, 0, 0],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14, 0, 0, 0, 0, 0],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57, 0, 0, 0, 0],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48, 0, 0, 0],
[63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31, 0, 0],
[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23, 0]
]


def max_path_sum(tri,m,n):
  # loop for bottom-up calculation 
    for i in range(m-1, -1, -1): 
        for j in range(i+1): 
  
            # for each element, check both 
            # elements just below the number 
            # and below right to the number 
            # add the maximum of them to it 
            if (tri[i+1][j] > tri[i+1][j+1]): 
                tri[i][j] += tri[i+1][j] 
            else: 
                tri[i][j] += tri[i+1][j+1] 
  
    # return the top element 
    # which stores the maximum sum 
    return tri[0][0] 


def main():
  print(max_path_sum(triangle_tree,14,14))

if __name__ == "__main__":
    main()