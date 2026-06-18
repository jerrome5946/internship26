# li=[]
# li.append(1,)
# print(li)
# li.append(2)
# print(li)
# li.append(3)
# print(li)
# li.append(4)
# print(li)
# lit=[16,17]
# li.extend(lit)
# print(li)
# # li.clear()
# # print(li)
# # li.insert(2,"Python")
# # print(li)
# # froot=["apple","orange","grapes","jackfruit"]
# # print(froot)
# # froot.pop(3)
# # print(froot)

# # froot.remove("apple")
# # print(froot)
# # froot.pop()
# # print(froot)
# # froot.pop(3)
# # print(froot)
# li.append(10)
# print(li)
# li.append(10)
# print(li)
# li.append(10)
# print(li)

# print(li.count(10))
# # color=["black","red","white","green","blue","violet"]
# # print(color)
# # i=color.index("blue")
# # print(i)
# no=[1,5,3,8,2,7,]
# # no.sort(reverse=True)
# print(no)
# x=no[:]
# print(x)
# x.append[70]
# print(x)
# 1. Start with an empty list


# 2. Loop 3 times to ask for input
# for i in range(3):
#     # Take input from the user
#     name = input("Enter a student's name: ")
#     # Add that name to our list
#     students.append(name)

# # 3. Print out the final list
# print("\nHere is your list of students:")
# for student in students:
#     print(student)

# print(max(li))
# s={"ananthapandmanapan","aron","aby","sambu"}
# print(s)
# s.add("sreekutty")
# print(s)
# # s.remove("sambu")
# # print(s)
# # print("aron" in s)
# n=s.copy()
# # print(s)
# print(n)
# n.update(["lenso","george"])
# print(n)
# print(len(s))
# print(n.clear())
# s.update(["abikt","jhony"])
# print(s)
# rem=s.pop()
# print(rem)
# com=s.intersection(n)
# print(com)
# print(s.isdisjoint(n))
# l=[1,2,2,2,3,4,5,2,5,7,8,]
# print(l)
# setss=set(l)
# print(setss)

# sentence = "apple banana apple orange banana"

# # .split() breaks the sentence into a list of words
# # set() removes the duplicates
# # len() counts how many are left
# unique_count = len(set(sentence.split()))

# print(f"Number of unique words: {unique_count}")
# # Output: Number of unique words: 3
# d1={1,2,3,4,5}
# d2={2,5,6}
# print(d1.intersection(d2))
# print(d1.symmetric_difference(d2))
# print(d1==d2)
# student={"name":"jerrome","age":"21","course":"cse"}
# print(student)
# # student['place']='kottayam'
# # print(student)
# # student["age"]=22
# # print(student)
# # student.pop("place"
# # print(student)
# # print(student.keys())
# # print(student.values())
# for key,value in student.items():
#  print(f"{key}:{value}")

# print("course" in student)
# student_copy=student.copy()
# print(student_copy)
# student_copy.clear()
# print(student_copy)
# text="haibalu"
# # char_count={}
# for char in text:
#     char_count[char]=char_count.get(char,0)+1
# print(char_count)
# marks={'alice':21,'james':45,'rose':58}
# high=max(marks)

# mergedd=marks|student
# print(mergedd)
# keys=["name ","age","place"]
# values=["jaisy","19","idukki"]
# # combined=dict(zip(keys,values))
# # print(combined)
# # employee={
# #     "emp1":{"name":20,"age":24}
# #     "emp":{"name":23,"age":26}
    
# # }
# # print(employee)
# passed = {subject: score for subject, score in scores.items() if score > 50}
# print("7. Values > 50:", passed)