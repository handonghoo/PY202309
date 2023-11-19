# student.csv 파일을 읽습니다.
from fileinput import close


lines = open("students.csv", "r", encoding="utf8").readlines()

students = {} #학생성적정보를 저장할 딕셔너리

# 학생 클래스를 선언합니다.
class Student:

    def __init__(self, name, korean, math, english):
        self.name = (name)
        self.korean = float(korean)
        self.math = float(math)
        self.english = float(english)

    def get_average(self):
        return (self.korean + self.math + self.english) / 3




# 학생 정보를 딕셔너리에 저장하는 함수를 수정합니다.
def loadData():
    student_list = []
    for line in lines[1:]:
        # 이름, 국어, 수학, 영어 순으로 데이터를 분리합니다.
        name, korean, math, english = line.split(",")

        # 학생 정보를 학생 클래스 인스턴스로 생성합니다.
        student = Student(name, korean, math, english)

        # 학생 정보를 딕셔너리에 저장합니다.
        students[name] = student


# 학생 별 평균 점수를 계산하는 함수를 수정합니다.
def getAverage():
    with open("average.txt", "w") as output_file:
        for name, student in students.items():
            # 평균 점수를 계산합니다.
            average = student.get_average()

            # 평균 점수를 출력합니다.
            print(name, "의 평균 점수는", average, "입니다.")

            # 평균 점수를 파일로 출력합니다.
            output_file.write(f"{name}: {average}\n")


# 학생 정보를 딕셔너리에 저장합니다.
loadData()


# 학생 별 평균 점수를 계산합니다.
getAverage()
