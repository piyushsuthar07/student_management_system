import pickle
from Student import Student

file_name = "student.pkl"
student = []
def save_data(s):
    global student
    student.append(s)
    with open(file_name, "wb") as file:
        pickle.dump(student, file)

def load_student():
    with open(file_name, "rb") as file:
        complete_data = pickle.load(file)
    for ele in complete_data:
        print(ele.display())
