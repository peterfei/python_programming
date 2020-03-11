#coding utf-8

def pascalRow(n):
    if n==0:
        return [1]
    else:
        N = pascalRow(n-1)
        return [1] +[N[i] + N[i+1] for i in range(n-1)]+ [1]
def pascalTriangle(n):
    triangle = []
    for i in range(n):
        triangle.append(pascalRow(i))
    return triangle
if __name__== "__main__":
    for i in pascalTriangle(7):
        print(i)
