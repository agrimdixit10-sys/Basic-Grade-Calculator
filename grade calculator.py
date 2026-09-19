
roll_no = int(input("Enter your roll number: "))
#perccentage calculator
subject = input("Enter your subject name : ")
if subject == "science":
  print("55/100")

elif subject == "maths":
    print("70/100")

elif subject == "English":
    print("100/100")
elif subject == "Hindi":
    print("55/100")
elif subject == "ai":
 print("95/100")
elif subject == "sst":
    print("87/100")
else:
    print("Subject not found:").end
score = int(input("Enter score of subject : "))
total = int(input("Enter total marks : "))
percentage = (score / total )* 100
print("percentage=", percentage, "%")


#grade rating
if score > 90:
    print("Grade: A")
elif score > 80:
    print("Grade: B")
elif score > 70:
    print("Grade: C")
elif score > 60:
    print("Grade: D")
elif score > 50:
    print("Grade: E")
elif score > 33:
    print("Grade: F")
elif score  < 33:
    print("Fail")
else:
    print("Enter a valid score:")