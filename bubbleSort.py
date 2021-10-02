def bubbleSort(arrayOfNumbers):
    for i in range(len(arrayOfNumbers) - 1):
        for j in range(len(arrayOfNumbers) - 1 - i):
            if arrayOfNumbers[j] > arrayOfNumbers[j + 1]:
                arrayOfNumbers[j], arrayOfNumbers[j + 1] = arrayOfNumbers[j + 1], arrayOfNumbers[j]
    return arrayOfNumbers

numCount = int(input("Enter how many numbers will be in array : "))

numbersToSort = list(map(int,input("\nEnter the numbers one line, delimiting them with space : ").strip().split()))[:numCount] 

print(bubbleSort(numbersToSort))
