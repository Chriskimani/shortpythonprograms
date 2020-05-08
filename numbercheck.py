def isPhoneNumber(text):
    if len(text) != 12: # edit length to suit your sequence
        return False
    for i in range(0, 3): # edit first pattern program is to recognise 
        if not text[i].isdecimal(): 
            return False
    if text[4] != ' ': # Edit first gap in the sequence 
        return False
    if i in range(5,8): # Edit second pattern check
        if not text[i].isdecimal():
            return False
    if text[8] != ' ':
        return False
    for i in range(9,12): # Edit third pattern check and add more block for more patters
        if not text[i].isdecimal():
            return False
    return True
email = ' call me tomorrow on 0411 222 333 or 0422 333 444' # change variable name 
foundNumber = False 
for i in range(len(email)): # change to name of variable in line 18 
    sequence = email[i:i+12]
    if isPhoneNumber(sequence):
        print('phone number found: ' + sequence + ' in the email')
        foundNumber = True
if not foundNumber:
    print('could not find any numbers in the email')
    
        

        

