#Riley Pollard
#Wednesday Class, Thursday 2pm Lab

def fileNameChange():
    #type your code here

    return

if __name__ == '__main__':
    fileNameChange()



    #Riley Pollard
#Wednesday Class, Thursday 2pm Lab

def courseGrade():
    
    # TODO: Declare any necessary variables here. 

    studentgrade = []
      
    # TODO: Read a file name from the user and read the tsv file here. 
    inputfile = input()

    try:
        with open(inputfile, 'r') as file:
            for line in file:
                # split the name and exams up
                lastname, firstname, exam1, exam2, exam3 = line.strip().split('\t')
                print("something")

        
    except:
        print('File not found')
        return
    
  

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
