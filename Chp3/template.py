#Write a Progr to fill in a letter template give below with the name and Date
letter = ''' 
       Dear <|Name|>,
       Your are selected!
       <|Date|>
         '''
name = input("To get money please Enter Your full Name : ")
print(letter.replace('<|Name|>',name).replace("<|Date|>","22 december 2005"))