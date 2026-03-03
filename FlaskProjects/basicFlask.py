from flask import Flask
import random
app = Flask(__name__)   #Flask constructor

#Decorator to tell the application which URL to associate with the following function
@app.route('/') #'/' is the root directory of the site
def helloFlask(): # define a function that will be called upon visitation of the associated URL
    return 'Hello Flask' #flask really doesn't give a damn what data you give it

@app.route('/randomnumber')
def randomnumber():
    d20 = random.randint(1,20)
    return "On a D20, you rolled: "+ f"{d20}"

if __name__=='__main__':
    app.run(debug=True) #run the application in debug mode

