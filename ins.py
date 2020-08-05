def swap(li, t, z):
    li[z], li[t] = li[t], li[z]

    return li

def insertion_sort(unli):
    swap_num = 0
    
    for i in range(1, len(unli)):
        k = i
        while k > 0 and unli[k] < unli[k-1]:
            unli = swap(unli, k-1, k)
            k -= 1
            swap_num += 1

    return swap_num

if __name__ == "__main__":
    f = open("rosalind_ins.txt", "r")

    f.readline()
    unsort = f.readline()
    unsort = list(map(int, unsort.split()))

    ty = [6,10,4,5,1,2]

    print(insertion_sort(unsort))





