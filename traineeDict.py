# create a dict where the initials is the key and full name is the value
trainList = input('enter the list of trainees fullname: ').split(',')
def inits(fnam):
    t = ''
    for x in fnam.split():
        t = t + x[0]
    return t.upper()
dictInitials = {inits(a) : a for a in trainList}
print(dictInitials)