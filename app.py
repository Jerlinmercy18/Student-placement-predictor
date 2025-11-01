from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('placement_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    cgpa = float(request.form['cgpa'])
    iq = int(request.form['iq'])
    comm = int(request.form['comm'])
    pred = model.predict([[cgpa, iq, comm]])

    result = "🎉 Student is likely to be Placed!" if pred[0] == 1 else "❌ Student may not be placed."
    return render_template('index.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
  
