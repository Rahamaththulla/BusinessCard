# BusinessCard

# What is EasyOCR?
EasyOCR, as the name suggests, is a Python package that allows computer vision developers to effortlessly perform Optical Character Recognition.It is a Python library for Optical Character Recognition (OCR) that allows you to easily extract text from images and scanned documents. In my project I am using easyOCR to extract text from business cards.

When it comes to OCR, EasyOCR is by far the most straightforward way to apply Optical Character Recognition:

1.The EasyOCR package can be installed with a single pip command.

2.The dependencies on the EasyOCR package are minimal, making it easy to configure your OCR development environment. 

3.Once EasyOCR is installed, only one import statement is required to import the package into your project.

4.From there, all you need is two lines of code to perform OCR — one to initialize the Reader class and then another to OCR the image via the readtext function

# Project Overview
BizCardX is a user-friendly tool for extracting information from business cards. The tool uses OCR technology to recognize text on business cards and extracts the data into a SQL database after classification using regular expressions. Users can access the extracted information using a GUI built using streamlit. The BizCardX application is a simple and intuitive user interface that guides users through the process of uploading the business card image and extracting its information. The extracted information would be displayed in a clean and organized manner, and users would be able to easily add it to the database with the click of a button. Further the data stored in database can be easily Read, updated and deleted by user as per the requirement.

# Want to see demo video of my project? -






# Libraries/Modules used for the project!
1.Pandas - (To Create a DataFrame with the scraped data)

2.mysql.connector - (To store and retrieve the data)

3.Streamlit - (To Create Graphical user Interface)

4.EasyOCR - (To extract text from images)

# Workflow

To get started with BusinessCard Data Extraction and stored mysql database that data used to create new BusinessCard, follow the steps below:

Install the required libraries using the pip install command. Streamlit, mysql.connector, pandas, easyocr.
       
       pip install [Name of the library]
       
Execute the “BusinessCard.py” using the streamlit run command.    
 
      streamlit run BusinessCard.py
      
A webpage is displayed in browser, First upload the file(".png", ".jpg")format that file extracting data with help of easyocr package. The extracting data stored in mysqldatabase. That stored data used to create a new BusineeCard.   
      
       
