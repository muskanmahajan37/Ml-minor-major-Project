alphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz012345678910*#/"
sentance= input("Enter the Sentence")
key=int(input("Enter key"))
dec_data =""
for i in sentance:
  if i in alphabets:
     pos = alphabets.find(i)
     dec_pos = pos-key
     dec_data =dec_data +alphabets[dec_pos%65]
  else:
       dec_data= dec_data +i
print(dec_data)    
        
  
