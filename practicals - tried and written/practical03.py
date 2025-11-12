'''
In a company, employee salaries are stored in a list as floating-point numbers. Write a
Python program that sorts the employee salaries in ascending order using the following two
algorithms:
• Selection Sort: Sort the salaries using the selection sort algorithm.
• Bubble Sort: Sort the salaries using the bubble sort algorithm.
After sorting the salaries, the program should display top five highest salaries in the company

'''
salaries = [55000.50 , 42000.75 , 60000.00 , 75000.25 , 58000.10 , 82000.00 , 47000.90 , 91000.30 , 50000.45]

class sorting:
    def selectionsort(self , list):
        for i in range(0 , len(list)-1):
            for j in range(i+1 , len(list)):
                if(list[i] > list[j]):
                    # print(f"swapped {list[i]} and {list[j]}")
                    list[i],list[j] = list[j],list[i] # swap
        print("selection sorted = ", list)
        return list
    
    def bubblesort(self , list):
        for i in range (0 , len(list)):
            for j in range(0 , len(list)-i-1):
                if(list[j] > list[j+1]):
                    list[j],list[j+1] = list[j+1],list[j]

        print("Bubble sorted = " , list)
        return list

    
s = sorting()

selectionsorted = s.selectionsort(salaries.copy())
# print(selectionsorted)

bubblesorted = s.bubblesort(salaries.copy())
# print(bubblesorted)
top5 = bubblesorted[-5::]
print("Top 5 salaries =",top5[::-1])