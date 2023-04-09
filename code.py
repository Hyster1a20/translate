import translate 
from translate import Translator

#base+res (variables) 
#translator azbi rah mne lang to lang 
#from_langage , to_langage

base = Translator(from_lang="English",to_lang="Spanish")

res = base.translate("hello") 

print(res)
