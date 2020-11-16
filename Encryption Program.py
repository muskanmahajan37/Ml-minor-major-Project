alphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz012345678910*#/"
sentance= input("Enter the Sentence")
key=int(input("Enter key"))
enc_data =""
for i in sentance:
  if i in alphabets:
     pos = alphabets.find(i)
     enc_pos = pos+key
     enc_data =enc_data +alphabets[enc_pos%65]
  else:
       enc_data= enc_data +i
print(enc_data)    
        
