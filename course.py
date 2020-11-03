import random

def create_outline():
    """
    TODO: implement your code here
    """
    #step 3
    print("Course Topics:")
    students = (
    "Nyari", 
    "Mark", 
    "Thando"
    )

    status = (
        "STARTED",
        "GRADED",
        "COMPLETED",
    )
    Course_Topics = set([
    'Introduction to Python',
    'Tools of the Trade',
    'How to make decisions',
    'How to repeat code',
    'How to structure data',
    'Functions',
    'Modules'
    ])
    
    listed_topics = list(Course_Topics)
    sorted_topics = sorted(listed_topics)
    for topics in sorted_topics:
        print('* ' + topics)
    
    #step 2
    problems = ["Problem 1", "Problem 2", "Problem 3"]
    print("Problems:")
    problem_topics = {}
    for x in listed_topics:
        problem_topics[x] = problems
    for key, value in problem_topics.items():
        print('*', key, ': ', end='')
        print(*value, sep=', ')
    
    #step 3
    c = 0
    a = 0
    print("Student Progress:")
    while a < len(students):
        b = random.randint(0, 2)
        result = (str(a + 1)+ '.', students[b], ' - ', sorted_topics[b], ' - ', problems[b], f"[{status[c]}]")
        print(*result)
        a += 1
        c += 1

if __name__ == "__main__":
    create_outline()
