class CourseData:
    def __init__(self, dept, courseNum, CourseName, Numcredits, lectDays, startTime, endTime, avgGrade):
        self.department = dept
        self.number = courseNum
        self.name = CourseName
        self.credits = Numcredits
        self.lectDays = lectDays
        self.startTime = startTime
        self.endTime = endTime
        self.avgGrade = avgGrade

    def printBlock(self, iter):
        template = "COURSE {iteration}: {dept}{courseNum}: {CourseName}\nNumber of Credits: {credits}\nDays of Lectures: {lectureDays}\nLecture Time: {startTime} – {endTime}\nStat: on average, students get {averageGrade}% in this course\n"
        print(template.format(iteration=iter, dept=self.department, courseNum=self.number, CourseName=self.name, credits=self.credits, lectureDays=self.lectDays, startTime=self.startTime, endTime=self.endTime, averageGrade=self.avgGrade))



if __name__ == "__main__":
    with open("classesInput.txt", "r") as reader:
        numEntries = eval(reader.readline())
        for i in range(numEntries):
            c = CourseData(reader.readline().strip(), reader.readline().strip(), reader.readline().strip(), reader.readline().strip(), reader.readline().strip(), reader.readline().strip(), reader.readline().strip(), reader.readline().strip())
            c.printBlock(i+1)

