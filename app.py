from flask import Flask, render_template, request
app = Flask(__name__)
app.debug = True

@app.route('/')
def home():
    # return the home.html template
    return render_template('home.html')

@app.route('/', methods=['POST'])
def get_mf_form():
    height = request.form['height']
    weight = request.form['weight']
    bmi = calculateBMI(height, weight)
    return "Your BMI is: " + str(bmi)

# def my_form_post(text):
#     text = request.form['text']
#     return text

# Calculate BMI
# Height is in meters
# Weight is in kilograms
def calculateBMI(height: int, weight: int) -> float:
    height = int(height)
    weight = int(weight) 
    if (height < 200 and weight < 500):
        # Convert height and weight to metric system
        height *= 0.0254
        weight *= 0.453592
        bmi: float = weight / (height * height)
    else: 
         bmi = "Incorrect Input."
    return bmi

# if __name__ == '__main__':
#    print(calculateBMI(76, 200))
    
    

    



    
