#!/usr/bin/python3
#it's using google_translator module

import sys
from google_trans_new import google_translator  

query = str(sys.argv[1:])
parse_query = query.replace(',',"").replace("'","")[1:-1]

translator = google_translator()  
translate_text = translator.translate(parse_query,lang_tgt='id')  
print(translate_text)