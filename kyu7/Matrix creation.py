"""Create an identity matrix of the specified size( >= 0).

Some examples:

(1)  =>  [[1]]

(2) => [ [1,0],
         [0,1] ]

       [ [1,0,0,0,0],
         [0,1,0,0,0],
(5) =>   [0,0,1,0,0],
         [0,0,0,1,0],
         [0,0,0,0,1] ]   """
def get_matrix(n):
    if n==0: return([])
    else:
        l=[]
        k=[]
        for i in range(n):
            for j in range(n):
                if i==j:
                    l.append(1)
                else:
                    l.append(0)
        m=len(l)//n
        start=0
        for x in range(n):
            end = start + m
            k.append(l[start:end])
            start = end
        return k
