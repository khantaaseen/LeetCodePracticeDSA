class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        students = deque(students)
        sandwiches = deque(sandwiches)
        count = 0
        
        while count < len(students):
            if students[0] == sandwiches[0]:
                sandwiches.popleft()
                count = 0
            else:
                students.append(students[0])
                count += 1
            students.popleft()
        return len(students)