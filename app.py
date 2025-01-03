from flask import Flask, request, render_template, send_from_directory
import pickle
import os
import numpy as np

application = Flask(__name__)
app = application

# Load scaler and model
scaler = pickle.load(open(r"C:\Users\aditya\Desktop\Pregrad\Pregrad_august\Model\MinMaxScaler.pkl", "rb"))
model = pickle.load(open(r"C:\Users\aditya\Desktop\Pregrad\Pregrad_august\Model\Classification.pkl", "rb"))

# Favicon route
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon'
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    result = ""
    fwi_value = None

    if request.method == 'POST':
        try:
            # Gather inputs from the form
            Temperature = float(request.form.get('Temperature'))
            RH = float(request.form.get('RH'))
            Ws = float(request.form.get('Ws'))
            Rain = float(request.form.get('Rain'))  # Optional, might exclude
            FFMC = float(request.form.get('FFMC'))
            DMC = float(request.form.get('DMC'))
            DC = float(request.form.get('DC'))  # Optional, might exclude
            ISI = float(request.form.get('ISI'))
            BUI = float(request.form.get('BUI'))

            # Use only required features
            input_features = [Temperature, RH, Ws, FFMC, DMC, ISI, BUI]

            # Preprocess inputs
            new_data = scaler.transform([input_features])  # Scale the input features

            # Predict the fire risk using the model
            predict = model.predict(new_data)

            # Calculate the FWI based on the dataset's analyzed formula
            fwi_value = 0.3 * FFMC + 0.4 * ISI + 0.3 * BUI

            # Adjust result based on FWI threshold
            if fwi_value >= 6.00:
                result = "Fire"
            else:
                result = "No Fire"

        except ValueError as e:
            result = f"Error: {e}"

        return render_template('home.html', result=result, fwi_value=fwi_value)
    else:
        return render_template('home.html', result=result, fwi_value=fwi_value)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
