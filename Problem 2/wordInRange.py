#Riley Pollard
#Wednesday Class, Thursday 2pm Lab

def wordInRange():
    #Type your code here
    filename = input()
    string1 = input() #string 1 is lower bound
    string2 = input() #string 2 is higher bound

    with open(filename, 'r') as myfile:
        lines = myfile.readlines()

    for eachline in lines:
        word = eachline.strip()
        if string1 <= word and word <= string2:
            print(word + ' - in range')
        else:
            print(word + ' - not in range')
    
if __name__ == '__main__':
    wordInRange()