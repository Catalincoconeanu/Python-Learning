# While Loops, we must have a False state at some point or the loop will be infinite
c = 0
while c < 5:
    print(c)
    c = c + 1
# While c < 5 then c will be printed, always must add c= c + 1 , to increment, if not c will always be = 0

# Break statement - Sample: While c is 0 and < 5 , but if c == 3 the process ends, after 3. This will print, 0,1,2,3
c = 0
while c < 5:
    print(c)
    if c == 3:
        break
    c = c + 1

# Continue statement - Sample: This will print 1,2,4,5  > and will skip the nr. 3

c = 0
while c < 5:
    c = c + 1
    if c == 3:
        continue
    print(c)
# Pass function -  Sample: This will print 1,2,3,4,5
c = 0
while c < 5:
    c = c + 1
    if c == 3:
        pass
    print(c)
