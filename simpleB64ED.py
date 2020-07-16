#Imports

import sys
import base64

#Get arg existance

if len(sys.argv) > 1:
	bleh = sys.argv[1]
	
else:
	bleh = 'Please Put in Valid E for Encode D for Decode'
	print(bleh)

# Determine the intent
	#Decode
if sys.argv[1] == 'D': 
	print('Decoding')
	txt = input()
	print(base64.b64decode(txt))

	#Encode
elif sys.argv[1] == 'E':
	print('Encode')
	txt = input()
	s = txt.encode()
	print(base64.b64encode(s))

	## Code by XiohNithe / FenexFox
	## https://fendev.xyz