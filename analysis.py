import random, time
from code import selection_sort, insertion_sort, bubble_sort

def create_rand_list(size, max_val):
    rand = random.randint(1,max_val)
    rand_list= [] 

    for number in range(size):
        rand=random.randint(1,max_val)
        rand_list.append(rand)
    return rand_list

# size = int(input("What sixe list do you want to create? "))
# max = int(input("What is the max value of the range? "))
# print(type(size), type(max))


arr = create_rand_list(100,100)

def analyze_time(func_name,arr ):
    toc = time.time()
    func_name(arr)
    tic = time.time()
    seconds = tic - toc
    print(f"{func_name} elapsed time is ---> {seconds}")


analyze_time(selection_sort,arr)
analyze_time(insertion_sort,arr)
analyze_time(bubble_sort,arr)
