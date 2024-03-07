#Riley Pollard
#Wednesday Class, Thursday 2pm Lab

def fileNameChange():
    #type your code here
    filepath = input().strip()

    with open(filepath,"r") as file:
        for line in file:
            modifiedfile = line.strip().replace('_photo.jpg', '_info.txt')
            print(modifiedfile)
    return

if __name__ == '__main__':
    fileNameChange()
