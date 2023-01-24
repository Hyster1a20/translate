import translate 
from translate import Translator

#base + res (variables) 
#translator azbi rah mne lang to lang 
#from_langage , to_langage

base = Translator(from_lang="English",to_lang="Spanish")

res = base.translate("hello") 

#u can change the word u want to translate in the fx base.translate() 

print(res)
