import streamlit as st
import PIL
from PIL import ImageDraw
import sqlite3
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
from sqlalchemy import create_engine, text
import mysql.connector as sql
import sqlalchemy
import pymysql
import tempfile
import os
import easyocr

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="Risvana123",
    database="Businesscard"

)

mycursor = mydb.cursor()
#mycursor.execute("create table carddetails(name varchar(100),position varchar(100),phoneno1 varchar(100),phoneno2 varchar(100),website varchar(100),gmail varchar(100),address varchar(100),company_name varchar(100),address1 varchar(100),company_name1 varchar(100));")
engine=create_engine("mysql+pymysql://root:Risvana123@localhost:3306/Businesscard",pool_size=10, max_overflow=20)
reader=easyocr.Reader(["en"])
file = st.file_uploader("Upload a file", type=["png", "jpg", "jpeg"])
if file is not None:
    # Save the uploaded file to a temporary directory
    temp_dir = tempfile.TemporaryDirectory()
    temp_file_path = os.path.join(temp_dir.name, file.name)
    with open(temp_file_path, "wb") as f:
        f.write(file.read())

    # Display uploaded image
    st.image(file)

    # Read text from the uploaded image
    bounds = easyocr.Reader(['en']).readtext(temp_file_path, detail=0)
    st.success("Data Extracted Successfully")
    st.write(bounds)
    name,position,phoneno1,phoneno2,website,gmail,address,company_name,address1,company_name1=bounds
    # Cleanup: Delete the temporary directory and file
    temp_dir.cleanup()
    submit=st.checkbox("Press Data Inserted to Database")
    if submit:
        mycursor.execute("insert into carddetails(name,position,phoneno1,phoneno2,website,gmail,address,company_name,address1,company_name1) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(name,position,phoneno1,phoneno2,website,gmail,address,company_name,address1,company_name1))
        mydb.commit()
        st.success("Data inserted Successfully")
        sq = text("select * from carddetails")
        with engine.begin() as conn:
            sql_return=pd.read_sql_query(sq, conn)
        st.write(sql_return)
        name_sql = sql_return.iloc[-1]["name"]
        position_sql = sql_return.iloc[-1]["position"]
        phoneno1_sql = sql_return.iloc[-1]["phoneno1"]
        phoneno2_sql= sql_return.iloc[-1]["phoneno2"]
        website_sql= sql_return.iloc[-1]["website"]
        gmail_sql = sql_return.iloc[-1]["gmail"]
        address_sql = sql_return.iloc[-1]["address"]
        company_name_sql = sql_return.iloc[-1]["company_name"]
        address1_sql = sql_return.iloc[-1]["address1"]
        company_name1_sql = sql_return.iloc[-1]["company_name1"]
        submit=st.button("New Business Card")
        if submit:
            image1 = Image.new("RGB", (600, 400), (153, 255, 255))
            draw = ImageDraw.Draw(image1)
            (x, y) = (50, 50)
            color = "rgb(0,0,0)"
            font = ImageFont.truetype("arial.ttf", size=60)
            draw.text((x, y), name_sql, fill=color, font=font)
            (x, y) = (50, 110)
            color = "rgb(0,0,0)"
            font = ImageFont.truetype("arial.ttf", size=40)
            draw.text((x, y), position_sql, fill=color, font=font)
            (x, y) = (70, 150)
            color = "rgb(0,0,0)"
            font = ImageFont.truetype("arial.ttf", size=30)
            draw.text((x, y), phoneno1_sql, fill=color, font=font)
            (x, y) = (70, 180)
            color = "rgb(0,0,0)"
            font = ImageFont.truetype("arial.ttf", size=30)
            draw.text((x, y), phoneno2_sql, fill=color, font=font)
            (x, y) = (70, 220)
            color = "rgb(0,0,0)"
            font = ImageFont.truetype("arial.ttf", size=30)
            draw.text((x, y), website_sql, fill=color, font=font)
            (x, y) = (70, 260)
            color = "rgb(0,0,0)"
            font = ImageFont.truetype("arial.ttf", size=30)
            draw.text((x, y), gmail_sql, fill=color, font=font)
            (x, y) = (70, 300)
            color = "rgb(0,0,0)"
            font = ImageFont.truetype("arial.ttf", size=20)
            draw.text((x, y), address_sql, fill=color, font=font)
            (x, y) = (270, 325)
            color = "rgb(0,0,0)"
            font = ImageFont.truetype("arial.ttf", size=50)
            draw.text((x, y), company_name_sql, fill=color, font=font)
            (x, y) = (400, 325)
            color = "rgb(0,0,0)"
            font = ImageFont.truetype("arial.ttf", size=50)
            draw.text((x, y), company_name1_sql, fill=color, font=font)
            st.image(image1)
else:
    st.write("No file uploaded")

