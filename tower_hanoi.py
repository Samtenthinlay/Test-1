def tower_hanoi(n,a,b,c):
    if n==1:
        print("move 1st disk from ",a,"to",c)
        return
    tower_hanoi(n-1,a,c,b)
    print("move",n, "th disk from",a ,"to",c)
    tower_hanoi(n-1,b,a,c)

#num=int(input("numner of disk you want:"))
tower_hanoi(3,"rod1","rod2","rod3")
print(tower_hanoi)