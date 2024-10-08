from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Assuming the input data comes from a form and is a list of floats
    input_data = [float(x) for x in request.form.values()]
    
    # Perform the prediction
    p = model.predict([input_data])
    if(p>0.75):
        prediction="highly"
    elif(p <0.60):
        prediction="less"
    else:
        prediction="medium"    
    
   
    return render_template('submit.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
