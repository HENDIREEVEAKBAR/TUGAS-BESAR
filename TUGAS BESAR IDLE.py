satudict1 = {'ind': "satu",'eng': "one",'sun': "hiji",'jav': "siji"}
dict2 = {'ind': "dua",'eng': "two",'sun': "dua",'jav': "loro"}
dict3 = {'ind': "tiga",'eng': "three",'sun': "tilu",'jav': "telu"}
dict4 = {'ind': "empat",'eng': "four",'sun': "opat",'jav': "papat"}
dict5 = {'ind': "lima",'eng': "five",'sun': "lima",'jav': "limo"}
dict6 = {'ind': "enam",'eng': "six",'sun': "genep",'jav': "enem"}
dict7 = {'ind': "tujuh",'eng': "seven",'sun': "tujuh",'jav': "pitu"}
dict8 = {'ind': "delapan",'eng': "eight",'sun': "dalapan",'jav': "wolu"}
dict9 = {'ind': "sembilan",'eng': "nine",'sun': "salapan",'jav': "songo"}
dict10 = {'ind': "sepuluh",'eng': "ten",'sun': "sapuluh",'jav': "sepuluh"}



angka = input("Masukkan angka anda: ")

def ind_eng():
    if angka == 'sepuluh':
        print(dict10.get('ind'), '=', dict10.get('eng'))
    elif angka == 'sembilan':
        print(dict9.get('ind'), '=', dict9.get('eng'))
    elif angka == 'delapan':
        print(dict8.get('ind'), '=', dict8.get('eng'))
    elif angka == 'tujuh':
        print(dict7.get('ind'), '=', dict7.get('eng'))
    elif angka == 'enam':
        print(dict6.get('ind'), '=', dict6.get('eng'))
    elif angka == 'lima':
        print(dict5.get('ind'), '=', dict5.get('eng'))
    elif angka == 'empat':
        print(dict4.get('ind'), '=', dict4.get('eng'))
    elif angka == 'tiga':
        print(dict3.get('ind'), '=', dict3.get('eng'))
    elif angka == 'dua':
        print(dict2.get('ind'), '=', dict2.get('eng'))
    elif angka == 'satu':
        print(dict1.get('ind'), '=', dict1.get('eng'))
    else:print("angka tidak valid")
def ind_sun():
    if angka == 'sepuluh':
        print(dict10.get('ind'), '=', dict10.get('sun'))
    elif angka == 'sembilan':
        print(dict9.get('ind'), '=', dict9.get('sun'))
    elif angka == 'delapan':
        print(dict8.get('ind'), '=', dict8.get('sun'))
    elif angka == 'tujuh':
        print(dict7.get('ind'), '=', dict7.get('sun'))
    elif angka == 'enam':
        print(dict6.get('ind'), '=', dict6.get('sun'))
    elif angka == 'lima':
        print(dict5.get('ind'), '=', dict5.get('sun'))
    elif angka == 'empat':
        print(dict4.get('ind'), '=', dict4.get('sun'))
    elif angka == 'tiga':
        print(dict3.get('ind'), '=', dict3.get('sun'))
    elif angka == 'dua':
        print(dict2.get('ind'), '=', dict2.get('sun'))
    elif angka == 'satu':
        print(dict1.get('ind'), '=', dict1.get('sun'))
    else:print("angka tidak valid")
def ind_jav():
    if angka == 'sepuluh':
        print(dict10.get('ind'), '=', dict10.get('jav'))
    elif angka == 'sembilan':
        print(dict9.get('ind'), '=', dict9.get('jav'))
    elif angka == 'delapan':
        print(dict8.get('ind'), '=', dict8.get('jav'))  
    elif angka == 'tujuh':
        print(dict7.get('ind'), '=', dict7.get('jav'))    
    elif angka == 'enam':
        print(dict6.get('ind'), '=', dict6.get('jav'))   
    elif angka == 'lima':
        print(dict5.get('ind'), '=', dict5.get('jav'))    
    elif angka == 'empat':
        print(dict4.get('ind'), '=', dict4.get('jav')) 
    elif angka == 'tiga':
        print(dict3.get('ind'), '=', dict3.get('jav'))  
    elif angka == 'dua':
        print(dict2.get('ind'), '=', dict2.get('jav'))  
    elif angka == 'satu':
        print(dict1.get('ind'), '=', dict1.get('jav')) 
    else:print("angka tidak valid")      

print("Untuk translate ke bahasa inggris ketik 'eng'")
print("Untuk translate ke bahasa sunda ketik 'sun'")
print("Untuk translate ke bahasa jawa ketik 'jav'")
translate = input("Masukkan bahasa untuk ditranslate: ")

if translate == "eng":
    ind_eng()
elif translate == "sun":
    ind_sun()
elif translate == "jav":
    ind_jav()
else: print("Masukkan bahasa yang ingin ditranslate dengan benar!")

print(" ind ")
if ind == ind:
     print (ind) 
elif ( eng == eng )
print (eng)
elif (sun == sun )
print (sun)
elif (jav)
print (jav)
else
    print ("masukan kode bahasa yang benar") 
eng = (["one" , "two", "three"])
print(eng[1])

list_bahasa = [dict_ind]
