import timeit



def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, 
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst

numbers = [5, 3, 8, 4, 2]





if __name__ =='__main__':
    numbers = [5, 3, 8, 4, 2,10,12,25,44,65]
    
    t_merge = timeit.timeit(stmt='merge_sort(numbers)', globals=globals(),number=1)
    t_insert = timeit.timeit(stmt='insertion_sort(numbers)', globals=globals(),number=1)
    t_normal = timeit.timeit(stmt='numbers.sort()', globals=globals(),number=1)
    numbers.sort()
    print(f'Time sorting \n numbers = {numbers} \n normal sort= {t_normal} \n Insertion sort = {t_insert} \n merge sort = {t_merge}')