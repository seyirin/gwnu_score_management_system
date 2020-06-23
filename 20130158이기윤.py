def main():

    students = []

    fp = open('score.csv','r')
    lines = fp.readlines()
    fp.close()

    for line in lines:
        line = line.strip()   
        items = line.split(',')

        student = {}
        student['id'] = int(items[0])
        student['name'] = items[1]
        student['kor'] = int(items[2])
        student['eng'] = int(items[3])
        student['math'] = int(items[4])
        student['total'] = 0
        student['avg'] = 0.0
        student['ranking'] = 0

        students.append(student)

    for student in students:
        student['total'] = student['kor'] + student['eng'] + student['math'] 
        student['avg'] = student['total'] / 3    

    sorted_students = sorted(students, key = lambda x : x['total'], reverse=True)

    count = 1
    for student in sorted_students:
        student['ranking'] = count
        count = count + 1

    result_students = sorted(sorted_students, key = lambda x : x['id'])

    fp = open('score.csv', 'w')

    for student in result_students:
        line = ','.join([str(student['id']),str(student['name']),str(student['kor']),str(student['eng']),
                         str(student['math']),str(student['total']),str(student['avg']),str(student['ranking']),'\n'])
        fp.write(line)

    fp.close()

    for student in sorted_students:
        print(student) 

if __name__ == "__main__":
    main()
