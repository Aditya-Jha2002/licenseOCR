This is a python model for extracting info from id

*****************************************************
Problem:
*****************************************************
	Extract information from image of RCI License by OCR in proper format.
		Information like - 
					Name, Year of Birth, Gender, UID


*****************************************************
Solution:
*****************************************************
	Steps:
		-> Take image
		-> crop to box(which has text in it)
		-> convert into gray scale(mono crome)
		-> give to tesseract
		-> text(output of tesseract)
	Now we will process this text means we will get meaningful information from it.
		-> find name
		-> find phone number
		-> find for RCI Id
	then we will validate the data with the info provided by the user, and the license.
	
*****************************************************
Dependent packages
*****************************************************
use the command
'''pip install -r requirements.txt'''
then run
'''uvicorn app:app --reload'''


*****************************************************
Structure and Usage
*****************************************************
	Directories:
		prediction_service -
			which contains code files for prediction service		
		static -
			place to store static file
		app.py - 
			fast_api file
			
	Usage:
		python file_name.py [input image]
		Output will be JSON object name
*****************************************************
:100:
