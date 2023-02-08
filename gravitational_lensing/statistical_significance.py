import numpy as np

def count_between_stddev(arr1, arr2, multiplier=1):
    # combine the arrays into one array
    combined = np.concatenate([arr1, arr2])
    # find the standard deviation of the combined array
    stddev = np.std(combined)
    # find the mean of the combined array
    mean = np.mean(combined)
    # find the lower and upper bounds
    lower = mean - multiplier * stddev
    upper = mean + multiplier * stddev
    # count the number of elements between the lower and upper bounds
    count = len(np.where((combined >= lower) & (combined <= upper))[0])
    return count, stddev, lower, upper

def report_statistical_significance(count, total, stddev, multiplier):
    # calculate the percentage of elements within the bounds
    percentage = count / total * 100
    # report the statistical significance
    if multiplier == 1:
        print(f"{count} elements ({percentage:.2f}%) fall within 1 standard deviation of the mean.")
    elif multiplier == 2:
        print(f"{count} elements ({percentage:.2f}%) fall within 2 standard deviations of the mean.")
    elif multiplier == 3:
        print(f"{count} elements ({percentage:.2f}%) fall within 3 standard deviations of the mean.")
    else:
        print(f"{count} elements ({percentage:.2f}%) fall within {multiplier} standard deviations of the mean.")
    print(f"The standard deviation is {stddev:.2f}.")

# example arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])

# count the number of elements between 1 standard deviation of the mean
count, stddev, lower, upper = count_between_stddev(arr1, arr2, multiplier=1)
total = len(arr1) + len(arr2)
report_statistical_significance(count, total, stddev, multiplier=1)

# count the number of elements between 2 standard deviations of the mean
count, stddev, lower, upper = count_between_stddev(arr1, arr2, multiplier=2)
report_statistical_significance(count, total, stddev, multiplier=2)

# count the number of elements between 3 standard deviations of the mean
count, stddev, lower, upper = count_between_stddev(arr1, arr2, multiplier=3)
report_statistical_significance(count, total, stddev, multiplier=3)