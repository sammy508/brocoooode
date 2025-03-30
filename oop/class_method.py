

# # class method = Allows operations related to class itself 
#                 Take(cls) as the 1st parameter , which represents the class itself

class student : 
    count = 0
    totsl_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        student.count+=1
        student.totsl_gpa += gpa

    # Instamce method

    def get_info(self):
        return f"{self.name} obtain {self.gpa}"
    

    @classmethod
    def get_count(cls):
        return f"Total num of student {cls.count}"   # by using cls method i get access to the class method

    @classmethod
    def get_avg_gpa(cls):
        if cls.count == 0:
             return 0
        else:
            return f"Total avg Gpa of student {cls.totsl_gpa / cls.count}"   # by using cls method i get access to the class method
    
student1 = student("Sammy",22)
student1 = student("samira",21)
student1 = student("bdur",20)

print(student.get_count())
print(student.get_avg_gpa())