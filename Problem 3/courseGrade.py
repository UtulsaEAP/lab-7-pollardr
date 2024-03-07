#Riley Pollard
#Wednesday Class, Thursday 2pm Lab

def courseGrade():
    
    # TODO: Declare any necessary variables here. 
    
    exam1tot = 0
    exam2tot = 0
    exam3tot = 0

    studentgrade = []
      
    # TODO: Read a file name from the user and read the tsv file here. 
    inputfile = input()

    try:
        with open(inputfile, 'r') as file:
            for line in file:
                # split the name and exams up
                lastname, firstname, exam1, exam2, exam3 = line.split('\t')
                print("something")

                #make grades into ints
                exam1 = int(exam1)
                exam2 = int(exam2)
                exam3 = int(exam3)
                
                #get avg and letter grade
                average = (exam1 + exam2 + exam3)/3
                if average >= 90:
                    lettergrade = 'A'
                elif 80 <= average < 90:
                    lettergrade = 'B'
                elif 70 <= average < 80:
                    lettergrade = 'C'
                elif 60 <= average < 70:
                    lettergrade = 'D'
                else:
                    lettergrade = 'F'
                studentgrade.append((lastname, firstname, exam1, exam2, exam3, lettergrade))

                #add to total class test totals
                exam1tot += exam1
                exam2tot += exam2
                exam3tot += exam3
    except:
        print('File not found')
        return
    
    #get class average per exam
    numberofstudents = len(studentgrade)
    avgexam1 = exam1tot / numberofstudents
    avgexam2 = exam2tot / numberofstudents
    avgexam3 = exam3tot / numberofstudents


    # TODO: Compute student grades and exam averages, then output results to a text file here.
    
    #name based on which TSV file
    if  inputfile == "./Problem 3/StudentInfo.tsv":
        outputfile = "./report.txt"
    elif inputfile == "./Problem 3/StudentInfo1.tsv":
        outputfile = "./report1.txt"
    else:
        outputfile = "./report2.txt"
        
    #actual ouput    
    with open(outputfile, 'w') as outputfile:
        for student in studentgrade:
            outputfile.write('\t'.join(map(str, student)) + '\n')

        outputfile.write(f'\nAverages: midterm1 {avgexam1: .2f}, midterm2 {avgexam2: .2f}, final {avgexam3: .2f}')  


if __name__ == "__main__":
    courseGrade()
    
    