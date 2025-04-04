students = {
    "iosif":{"age": 18 , "skills" : ["Programming","Football","Martial Arts"],"hometown":"drama"},
    "petros": {"age" : 19 , "skills" : ["basketball" , "drawing", "volleyball"], "hometown":"thessalonikh"},
    "marios" : {"age" : 20 , "skills" : ["handball" , "coding", "skateboarding"], "hometown":"larisa"}
}

for name, data in students.items():
    print(f"mathitis: {name}, ilikia: {data['age']}, hometown: {data['hometown']},skills: {', '.join(data['skills'])}")