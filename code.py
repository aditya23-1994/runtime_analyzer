def bubble_sort(arr):
    swap = True
    while swap == True:
        swap = False
        for num in range(len(arr)-1):    
            if arr[num] > arr[num+1]:
                swap = True
                arr[num], arr[num+1] = arr[num+1], arr[num]

    return arr


def selection_sort(arr):
    marker = 0
    while marker < len(arr):
        for num in range(marker, len(arr)):
            if arr[marker] > arr[num]:
                arr[marker], arr[num] = arr[num], arr[marker]
            
        marker += 1
    
    return arr



def insertion_sort(arr):
    marker = 1
    while marker < len(arr):
        for num in range(marker, len(arr)):
            
                if arr[num] < arr[num-1]:
                    arr[num], arr[num-1] = arr[num-1], arr[num]
        marker +=1
    return arr

        
def merge_sort(l1:list,l2:list):
    i = 0
    j = 0
    l = []
    while i < len(l1) and j < len(l2):

        if l1[i] < l2[j]:
            l.append(l1[i])
            i+=1
        else:
            l.append(l2[j])
            j+=1

        print(l)
    while i < len(l1):
        l.append(l1[i])
        i += 1


    while j < len(l1):
        l.append(l1[j])
        j += 1

    print(l)



def merge_arr(arr):
    l1 = [x for x in range(0,arr//2)]
    l2 = []


merge_sort(l1,l2)
