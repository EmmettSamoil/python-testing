import random
ready = ''
mylist = ["Blood", "Gunna", "Bo"]
nameFirst = input('Enter your First Name: ')
nameLast = input('Enter your Last Name: ')
def main():
    while ready != 'Yes':
        print (mylist)
        add = input('Add name to list(Type skip to skip):')
        if add != "skip":
            mylist.append(add)
        else :
            print (mylist)
            remove = input('Remove name from list(Type skip to skip):')
            if remove != 'skip':
                mylist.remove(remove)
            else :
                end(mylist, nameFirst, nameLast)
                return 

def end(mylist, nameFirst, nameLast):
    print (mylist)
    ready = input('If you are ready to generate a nickname type Yes. If you are not ready type No:')
    if ready == 'Yes':
        Option = input('Pick 1 for random name or type nickname:')
        if Option == '1':
            print(f"{nameFirst} {random.choice(mylist)} {nameLast}")
        else:
            print(f"{nameFirst} {Option} {nameLast}")
    else:
         main()
        
if __name__ == "__main__":
    main()