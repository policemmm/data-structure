from os import remove
with open('datafile.txt', "x") as datafile:
    pass
def bin_maker(note, bytecount):
    bnote = (bytecount-len(note))*"00000000"
    barr = bytearray(note,'utf-8')
    for charnum in barr:
        if (len(bin(charnum)[2:]) == 8):
            bnote += bin(charnum)
        else:
            bnote += ("0"*(8-len(bin(charnum)[2:])) + bin(charnum)[2:])
    return bnote
def str_maker(bineryseq):
    string = ''
    for index in range(0,len(bineryseq),8):
        try:
            string += chr(int(bineryseq[index:index+8].lstrip('0'),2))
        except:
            pass
    return string            
def unique_idchecker(pri_key):
    with open("datafile.txt",'r') as file:
        rnge = len(file.read())
        file.seek(0)
        for count in range(rnge//1648):
            fileid = file.read(48)
            if (str_maker(fileid) == pri_key):
                raise ValueError("duplicate id finded !!!")
            file.read(1600)
        return True
def id_location(pri_key):
    with open("datafile.txt",'r') as file:
        rnge = len(file.read())
        file.seek(0)
        for count in range(rnge//1648):
            fileid = file.read(48)
            if (str_maker(fileid) == pri_key):
                return (file.tell()-48)#mishe ham kam nakard badan 1600 ta raft jolo
            file.read(1600)
        raise ValueError('id isn\'t correct')
while(True):
    state = input('What do you want to do with data structure<table>? (add, del, change, exit) :\t')
    if (state == 'add'):
        pri_key = input('Please enter your record id <Preferably not repeat> :\t')
        first_name = input('Please enter first name :\t')
        last_name = input('Please enter last name :\t')
        unique_idchecker(pri_key)
        with open('datafile.txt', "a+") as datafile:
            datafile.write(bin_maker(pri_key,6)+bin_maker(first_name,100)+bin_maker(last_name,100))
    elif (state == 'del'):
        pri_key = input('Please enter record id to delete it:\t')
        location = id_location(pri_key)
        with open('datafile.txt','r+') as datafile:
            text =datafile.read(location)
            datafile.read(1648)
            text += datafile.read()
        remove('datafile.txt')
        with open('datafile.txt','x+') as datafile:
            datafile = open('datafile.txt','w+')
            datafile.write(text)
            datafile.close()
    elif (state == 'change'):
        pri_key = input('Please enter record id to edit it :\t')
        location = id_location(pri_key)
        choice = input("What do you want to change (id, firstname, lastname):\t")
        if (choice == 'id'):
            new_id = input("Please enter your new id :\t")
            unique_idchecker(new_id)
            with open('datafile.txt','r') as datafile:
                text = datafile.read(location)
                datafile.read(48)
                text += bin_maker(new_id, 6)
                text += datafile.read()
            remove('datafile.txt')
            with open('datafile.txt','x+') as datafile:
                datafile = open('datafile.txt','w+')
                datafile.write(text)
                datafile.close()
        elif (choice == 'firstname'):
            new_firstname = input("Please enter your new firstname :\t")
            with open('datafile.txt','r') as datafile:
                text = datafile.read(location+48)
                text += bin_maker(new_firstname, 100)
                datafile.read(800)
                text += datafile.read()
            remove('datafile.txt')
            with open('datafile.txt','x+') as datafile:
                datafile = open('datafile.txt','w+')
                datafile.write(text)
                datafile.close()
        elif (choice == 'lastname'):
            new_lastname = input("Please enter your new lastname :\t")
            with open('datafile.txt','r') as datafile:
                text = datafile.read(location+848)
                text += bin_maker(new_lastname, 100)
                datafile.read(800)
                text += datafile.read()
            remove('datafile.txt')
            with open('datafile.txt','x+') as datafile:
                datafile = open('datafile.txt','w+')
                datafile.write(text)
                datafile.close()            
        else:
            raise ValueError('Wrong input !!!')
    elif (state == 'exit'):
        break
    else:
        raise ValueError('Wrong input !!!')
    