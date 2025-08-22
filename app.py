from flask import Flask, request, render_template

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/predictdata',methods=["GET","POST"])
def predict_datapoint():
    if request.method=="GET":
        return render_template('home.html')
    else:
        data = CustomData(
            area=float(request.form.get('area')),
            bedrooms=float(request.form.get('bedrooms')),
            bathrooms=float(request.form.get('bathrooms')),
            stories=float(request.form.get('stories')),
            mainroad=request.form.get('mainroad'),
            guestroom=request.form.get('guestroom'),
            basement=request.form.get('basement'),
            hotwaterheating=request.form.get('hotwaterheating'),
            airconditioning=request.form.get('airconditioning'),
            parking=float(request.form.get('parking')),
            prefarea=request.form.get('prefarea'),
            furnishingstatus=request.form.get('furnishingstatus')
        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)

        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        return render_template("home.html",results=results[0])


if __name__ == "__main__":
    app.run(host="0.0.0.0")


