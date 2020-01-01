#Write a program that uses a for loop to "count mississippily" to five. Having counted to five, the program should print to the screen the final message "Ready or not, here I come!"
import time

for second in range(1, 6):
    print(second, "Mississippi")
    time.sleep(1)
	
print("Ready or not, here I come!")