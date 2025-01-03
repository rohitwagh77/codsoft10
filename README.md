# Forest Fire Prediction System

This project is a web-based application for predicting the risk of forest fires using the Fire Weather Index (FWI). The prediction is based on user-input meteorological and environmental parameters. The application utilizes machine learning models and Flask as the web framework.

## Features

- Predicts the risk of forest fires using relevant input features.
- Calculates the Fire Weather Index (FWI) based on the input data.
- User-friendly interface with an input form.
- Scalable design using Flask.
- Includes a favicon and static assets for better user experience.

## Prerequisites

1. Python 3.x installed on your system.
2. Required Python libraries:
   - Flask
   - Numpy
   - Pickle (for loading the pre-trained model and scaler)

## Directory Structure

```
├── application.py        # Main Flask application file
├── static
│   ├── favicon.ico       # Favicon for the web app
│   └── style.css         # CSS for styling the web app
├── templates
│   ├── index.html        # Home page with input form
│   └── home.html         # Page to display prediction results
├── Model
│   ├── MinMaxScaler.pkl  # Pre-trained scaler for feature scaling
│   └── Classification.pkl # Pre-trained classification model
├── README.md             # Project documentation
├── Algerian_forest_fires_cleaned_dataset.csv # Dataset for FWI analysis
```

## Installation and Setup

1. Clone the repository.
2. Ensure you have Python 3.x installed.
3. Install required libraries using:
   ```bash
   pip install flask numpy
   ```
4. Place the pre-trained model and scaler files in the `Model` directory.
5. Ensure the dataset `Algerian_forest_fires_cleaned_dataset.csv` is in the project root directory for analysis purposes.

## Running the Application

1. Run the Flask application:
   ```bash
   python application.py
   ```
2. Open a web browser and navigate to `http://127.0.0.1:5000` to access the application.

## Input Parameters for Prediction

The application accepts the following input parameters through the form:

- **Temperature (°C):** Ambient temperature in Celsius.
- **Relative Humidity (%):** Atmospheric relative humidity percentage.
- **Wind Speed (km/h):** Speed of the wind in kilometers per hour.
- **Rain (mm):** Amount of rainfall in millimeters.
- **Fine Fuel Moisture Code (FFMC):** Indicates the moisture content of litter and other fine fuels.
- **Duff Moisture Code (DMC):** Represents the moisture content of loosely compacted organic layers of moderate depth.
- **Drought Code (DC):** Indicates the moisture content of deep, compact organic layers.
- **Initial Spread Index (ISI):** Numerical rating of the expected fire spread rate.
- **Buildup Index (BUI):** Combines the DMC and DC to give an indication of the total fuel availability.

## Fire Weather Index (FWI) Calculation

Based on the dataset analysis, the Fire Weather Index (FWI) is computed using:

```
FWI = 0.5 * FFMC + 0.3 * ISI + 0.2 * BUI
```

The threshold for predicting fire occurrence is derived from the dataset:

- **FWI > 20** indicates a higher likelihood of fire.
- **FWI ≤ 20** indicates a lower likelihood of fire.

## Example Workflow

1. Enter the required parameters into the form.
2. Submit the form.
3. The application displays:
   - The predicted fire risk (Fire/No Fire).
   - The calculated Fire Weather Index (FWI).

## Known Issues and Future Enhancements

- The dataset has certain limitations, and the accuracy of the predictions depends on the training data.
- Future updates will include:
  - Improved prediction models with higher accuracy.
  - Additional input parameters for better predictions.
  - Visualizations of FWI trends.

## Credits

- Dataset: Algerian Forest Fire Dataset.
- Model: Pre-trained classification model created using machine learning techniques.

## License

This project is for educational purposes only and is not licensed for commercial use.
