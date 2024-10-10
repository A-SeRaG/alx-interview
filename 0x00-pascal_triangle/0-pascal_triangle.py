
def pascal_triangle(n):
    '''pascal function'''
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]+[i*2 if i > 2 else i for i in nums ] + [1]
        nums = [a for a in range(1, n + 1)]
    print (row)
pascal_triangle(6)