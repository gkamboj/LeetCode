class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        ind, students_sum = 0, sum(students)
        while students:
            if students[0] == sandwiches[0]:
                students_sum -= students.pop(0)
                sandwiches.pop(0)
            elif (sandwiches[0] and not students_sum) or (not sandwiches[0] and students_sum == len(students)):
                return len(students)
            else:
                top_student = students.pop(0)
                students.append(top_student)
        return 0
            
''' Approach: Keep maintaining the sum of students array. If there are no matching students with preference
of top sandwich (checked by line-8 condition), return False. If array becomes empty, means all sandwiches
are consumed. Return 0 in that case.
'''        