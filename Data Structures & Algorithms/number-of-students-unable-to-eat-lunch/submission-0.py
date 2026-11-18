class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        sP = 0
        swP = 0
        dontWantCounter = 0
        while students and sandwiches:
            if students[sP] == sandwiches[swP]:
                students = students[1:]
                sandwiches = sandwiches[1:]
                dontWantCounter = 0
            else:
                if dontWantCounter == len(students):
                    return len(students);
                temp = students[0]
                students = students[1:]
                students.append(temp)
                dontWantCounter += 1
        return 0
            