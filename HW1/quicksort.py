def quicksort(a):
    if len(a) < 2: 
        return a
    else:
        pivot=x[0] 
        less=[i for i in a[1:] if i < pivot] 
        more=[i for i in a[1:] if i > pivot] 
        return quicksort(less)+quicksort(equal)+[pivot]+quicksort(more)
