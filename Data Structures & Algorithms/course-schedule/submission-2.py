class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        
        # create adjacency list from prerequisites
        # and count degrees (how many dependency) of courses
        course_graph = defaultdict(list)
        in_degrees = {i: 0 for i in range(numCourses)}
        queue = deque()
        
        for prerequisite, course in prerequisites:
            course_graph[prerequisite].append(course)
            in_degrees[course] += 1

        for course, degree in in_degrees.items():
            if degree == 0:
                queue.append(course)
        
        enrolled_course_count = 0

        while queue:
            prerequisite = queue.popleft()
            enrolled_course_count += 1

            for course in course_graph[prerequisite]:
                in_degrees[course] -= 1
                if in_degrees[course] == 0:
                    queue.append(course)

        return enrolled_course_count == numCourses