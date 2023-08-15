# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
width = int(input())

# Print top part of the pattern
for i in range(1, width+1):
    space = " " * (width - i)
    stars = 'H' * (2 * i - 1)
    print((space+stars))

# Print middle part of the pattern
for i in range(0, ( (2*(width+1)) + ((width+1)//2)) ):
    
    #Top Pillars
    if i in range(0, width+1):
        stars = 'H' * width
        print(stars.center(2 * width, " ") + stars.center(width*6, " "))
        
    #Middle Pillars
    elif i in range(width+1, width+1+((width+1)//2)):
        stars = 'H' * (width * 5)
        print(stars.center(width * 6, " "))

    #Bottom Pillars
    elif i in range(((width+1)//2), ((2*(width+1)) + ((width+1)//2))):
        stars = 'H' * width
        print(stars.center(2 * width, " ") + stars.center(width*6, " "))

# Print bottom part of the pattern
for i in range(width, 0, -1):
    space = ' ' * (width-i)
    stars = 'H' * ((2*i) -1)
    print((space + stars).rjust(width*5+i-1, " "))