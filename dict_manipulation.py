students_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
student_grades={}
for key in students_scores:
     if(students_scores[key]<100 and students_scores[key]>=90):
         student_grades[key]="outstanding"
     elif(students_scores[key]<90 and students_scores[key]>=81):
         student_grades[key]="exceeds expectation"
     elif(students_scores[key]<80 and students_scores[key]>=70):
         student_grades[key]="acceptable"
     else:
         student_grades[key]="good"
         
print(student_grades)
         