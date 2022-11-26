def nameRank(names, marks, updates, n):
     
    # Array of students
    b = [[0 for j in range(3)] for i in range(n)]
    for i in range(n):
         
        # name of the student
        b[i][0] = names[i]
         
        # Update marks of the student
        b[i][1]= marks[i] + updates[i]
         
        # current rank of the student
        b[i][2] = i + 1
         
    high= b[0]
    for j in range(1, n):
        if (b[j][1] >= high[1]):
            high=b[j]
             
    # Printing the name and jump in rank
    print("Name: ", high[0], ", Jump: ",
            abs(high[2]-1),sep="")
 
# Names of the students
names=["Aniket","Shahnawaz","Ayush"]
 
# Marks of the students
marks = [75,80,70]
 
# Updates that are to be done
updates=[1,2,3]
 
a=len(marks)
 
nameRank(names,marks,updates,a)

# This code is contributed by Aniket kumar(12215523),Madhukar Rai(12215018),N V K Jaswanth Srighakollapu(12215170)
 
