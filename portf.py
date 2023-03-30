from flask import Flask, render_template

data = {}

app = Flask(__name__)

class Data:
    occupation = "Your Job"
    resume ="Resume Url"
    image = "https://icon2.cleanpng.com/20180523/wxj/kisspng-businessperson-computer-icons-avatar-clip-art-lattice-5b0508dc2ee812.2252011515270566041921.jpg"
    insta = "Instagram Url"
    git = "github Url"
    twitter ="twitter Url"
    linkedin = "linkedin Url"
    about = "Enter details about You!"
    age = 0
    email = "example@gmail.com"
    phone = "+910000000000"
    address = "Your Address"
    language = "Hindi,English"
    Programming = "your Skills"
    tools = "your Skills"
    internet = "Your Skills"
    other = "other Skills"
    work = [
        {"time":"JUNE 2021 - PRESENT",
             "company":"MATRIX ANALYTICS CORPORATION",
             "post":"Python Programmer",
             "info":"Delivered Model Risk Management Dashboards to track model performance post deployment for a lending client.Working on building code, enhanced templates and defining a best practice for one of the key milestones of XAI model development process of Credit risk management models of MATRiX."},
         {"time":"JUNE 2019 - APRIL 2020",
             "company":"MATRIX ANALYTICS CORPORATION",
             "post":"Data Scientist Intern",
             "info":"Built suite of AI based revenue and balance models for one of the major banking client.Automated the task of Exploratory Data Analysis by writing a Python Script to perform analysis on any given dataset. Developed front-end forms for clients to get user-input and run Machine Learning models for the client using JavaScript"},
         {"time":"SEPTEMBER 2017 - DECEMBER 2017",
             "company":"CENTRAL DRUG RESEARCH INSTITUTE",
             "post":"Research Intern",
             "info":"Analyzed over 30 research papers and data sources to gather data on the spread of Parkinson’s Disease Visualized various trends in the spread of Parkinson’s Disease across the Globe using Tableau."},
        
        ]
    projects =[
        {"time":"JUNE 2021 - PRESENT",
             "name":"MATRIX Game",
             "info":"Delivered Model Risk Management Dashboards to track model performance post deployment for a lending client.Working on building code, enhanced templates and defining a best practice for one of the key milestones of XAI model development process of Credit risk management models of MATRiX."},
         {"time":"JUNE 2019 - APRIL 2020",
             "name":"ML Model",
             "info":"Built suite of AI based revenue and balance models for one of the major banking client.Automated the task of Exploratory Data Analysis by writing a Python Script to perform analysis on any given dataset. Developed front-end forms for clients to get user-input and run Machine Learning models for the client using JavaScript"},
         {"time":"SEPTEMBER 2017 - DECEMBER 2017",
             "name":"Own Text Transformer",
             "info":"Analyzed over 30 research papers and data sources to gather data on the spread of Parkinson’s Disease Visualized various trends in the spread of Parkinson’s Disease across the Globe using Tableau."},]
    education = [
        {"time":"2018 - 2020",
             "name":"Master's Degree",
             "course":"M.S. in Information Systems",
             "collage":"STEVENS INSTITUTE OF TECHNOLOGY",
             "info":"Relevant Coursework: Web Mining, Knowledge Discovery in Databases, Marketing Analytics",
             "projects":["Human Trafficking Knowledge Graph - A knowledge graph generating project that helped identify over 100 cases of Human Trafficking around NYC. Judged as the best solution for the competition.",'Hate Comment Detector – A flask powered website to automatically filter hate comments from Twitter and Live News using Logistic Regression algorithm.'],
        },
        {"time":"2014 - 2018",
             "name":"Bachelor's Degree",
             "course":"B.Tech in Computer Science",
             "collage":"SGGS Nanded",
             "info":"Relevant Coursework: Web Development, Advanced Database Management Systems, Object Oriented Programming, Data Mining and Business Intelligence",
             "projects":["AutoPlay - A Machine Learning model to predict the outcome of a cricket game beforehand, based on the past records and performances.",'Hate Comment Detector – A flask powered website to automatically filter hate comments from Twitter and Live News using Logistic Regression algorithm.'],
        },
        ]
    def __init__(self,name="Your Name"):
        self.name = name
        
    def getData(self):
        dt = {
    "name":self.name,
    "resume":self.resume,
    "occupation":self.occupation,
    "image":self.image,
    "insta":self.insta,
    "git":self.git,
    "twitter":self.twitter,
    "linkedin":self.linkedin,
    "about":self.about,
    "age": self.age,
    "email": self.email,
    "phone": self.phone,
    "address": self.address,
    "language": self.language,
    "Programming":self.Programming,
    "tools": self.tools,
    "internet": self.internet,
    "other": self.other,
    "work":self.work,
    "projects":self.projects,
    "education":self.education,
    }
        return dt


# flask endpoint
@app.route("/")
def index():
    return render_template("index.html",data=data)
    

def RunApp(port,dataobj):
    '''
    function for running app
    @param port
    @param dataobj
    '''
    global data
    data = dataobj
    app.run(port=port)

# if __name__ == "__main__":
#     app.run(debug=True)