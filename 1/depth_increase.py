
def depth_increase(fn)-> int:
    """ Count the number of immeadiate increases in depth. """
    acc_increase = 0
    lines_read = 0
    last_depth = 0
    lines_read = 0

    input = open(fn, "r")
    for depth in input:
        lines_read += 1
        if (lines_read == 1):
            last_depth = depth
            continue
        if int(depth) > int(last_depth):
            acc_increase += 1
        last_depth = depth   

    print(f"""Number of measurements taken: {lines_read}.
        Total increase of depth: {acc_increase}""")
    return acc_increase

def sum_increase(fn)-> int:
    """ Counts the number of immedieate increases of sums of 3 depths. """
    sum_1 = 0
    sum_2 = 0
    sum_3 = 0
    lines_read = 0
    increased = 0
    input = open(fn, "r")
    #read the first measurement 'manually'
    #will make the loop prettier
    sum_1 = int(input.readline())
    lines_read += 1
    sum_2 = int(input.readline())
    lines_read += 1
    sum_1 += sum_2
    sum_3 = int(input.readline())
    lines_read += 1
    sum_1 += sum_3
    sum_2 += sum_3

    #Then, iterate over the rest
    for depth in input:
        mbsl = int(depth)
        sum_1 += mbsl
        sum_2 += mbsl
        sum_3 += mbsl
        iter = lines_read % 3
        print("Iter: ",iter)
        #print(f"Sum_1: {sum_1}, sum_2: {sum_2} , sum_3: {sum_3} & lines_read: {lines_read}")
        if iter == 0: 
            if (sum_2 - mbsl) > (sum_1):
                increased += 1
            sum_2 = 0
            #sum_3 = 0
        elif iter == 1:
            #print("ITER == 1")
            if (sum_3 - mbsl) > sum_2:
                increased += 1
            sum_3 = 0
        else:
            #print("ITER == 2")
            if (sum_1 - mbsl) > (sum_3):
                increased += 1
            sum_1 = 0
        lines_read += 1
        return 0


    print(f"""Total increase of depth when noise is taken into account: {increased}.""")
    return increased

normal_increase = depth_increase("input")
noise_adjusted = sum_increase("input")

difference = (noise_adjusted - normal_increase)

print(f"""After adjusting for noise, {difference}
    immeadiate increases are found.""")
