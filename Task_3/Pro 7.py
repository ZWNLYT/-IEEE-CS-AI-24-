def knapSack(*args):
    W, n = args[0], args[1]
    wt, val = args[2], args[3]

    if W == 0 or n == 0:
        return 0
    
    if wt[n-1] > W:
        return knapSack(W, wt[:n-1], val[:n-1])

    else:
        return max(val[n-1] + knapSack(W - wt[n-1], wt[:n-1], val[:n-1]),
                   knapSack(W, wt[:n-1], val[:n-1]))

n = int(input("Enter the number of items: "))
W = int(input("Enter the maximum weight of the knapsack: "))

wt = []
val = []

print("Enter the weights and values of the items:")
for i in range(n):
    wt.append(int(input("Weight of item {}: ".format(i+1))))
    val.append(int(input("Value of item {}: ".format(i+1))))
print("Maximum possible sum of values of items that can be taken home: "
      , knapSack(W, n, wt, val))