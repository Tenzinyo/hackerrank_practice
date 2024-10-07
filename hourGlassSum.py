def hourGlassSum(arr):
    maxsum = -99
    for i in range(4):
        for j in range(4):
            top = sum(arr[i][j:j+3])
            middle = sum(arr[i+1][j+1])
            end = sum(arr[i+2][j:j+3])
            totalsum = top + middle + end
            maxsum =max(totalsum,maxsum)

    return maxsum
