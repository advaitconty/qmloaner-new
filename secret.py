def mongo_host_connection(username, password, default=False):
    if default == True:
        return ("mongodb+srv://user:CATerOmPe@guitar-data.naorta7.mongodb.net/?retryWrites=true&w=majority&appName=guitar-data")
    
    else:
        return (f"mongodb+srv://{username}:{password}@guitar-data.naorta7.mongodb.net/?retryWrites=true&w=majority&appName=guitar-data")


GEMINI_API_KEY = "AIzaSyB9w7GXKfW57dA_pq6myEZT1OYdhzJ0gtM"
# ATTENDANCE_EMAILS = ["elias_wong_yi_hang@students.edu.sg",
#                      "chen_li_yan@moe.edu.sg",
#                      "faith_ang_si_ying@moe.edu.sg",
#                      "toh_mei_fang_belinda@moe.edu.sg",
#                      "ryan_lim_jun_long@students.edu.sg",
#                      "faaiz_ashraf@students.edu.sg"]
LOAN_EMAILS = [""]  # to be finalised with Ryan later
TEST_EMAILS = ["advait@contractor.net",
               "ryanlim2009@gmail.com"]
NAMES = ['Goh Feng Yi Justin', #S1
         'Kaw Jun Kai Joshua', 
         'Lucas Chen Yiwei', 
         'Christopher Soh Zhi Yong', 
         'Ignatius Teow Jun Hong', 
         'Lucas Kevin Tan Ming', 
         'Gabriel Ho Yan Rui',
         'Laconi Giuliano', #S2 
         'Elliot Ho Yihui', 
         'Hazim Matin Bin Helmy', 
         'Wong Jun Xi Lucius', 
         'Ethan Ryo Young', 
         'Sim Jun Kai Noah', 
         'Greg Tan Hee Theang', 
         'Lee Cit Hoi, Kiran', 
         'Axel Soong Hong Wei', 
         'Alexander Saviour', 
         'Elijah Nathan Joseph', 
         'Goh Toh Yo', 
         'Haziq Matin Bin Helmy', 
         'Isaiah Tamayo Abella', 
         'Caleb Yang Jingyang',  
         'Tan Shao Xi', #S3
         'Anay Shandilya', 
         'Lee Jing Song Ryan', 
         'Vancoppenolle Julien Joo Duk', 
         'Evan Elijah Koh Yong Zhe', 
         'Thaddeus Lee Guan Zong', 
         'Dhivyan S/O Siva Kumar', 
         'Ayaan Ahmad Khan', #S4
         'Dylan Wee Yong Hao', 
         'Ethan Chng Jun Kai', 
         'Luke Lim', 
         'Wong An Yu', 
         'Elias Wong Yihang', 
         'Kaeson Liang Z Kai', 
         'Ryan Lim Jun Long (Lin Junlong)', 
         'Faaiz Ashraf', 
         'Samson Wong Bing Cheng']
QM_CODE = "Soote Flap   "
EMAIL_ID = "spsge.loans@hotmail.com"
EMAIL_PASSWORD = "BAtARgLaxwOrNEQ"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587