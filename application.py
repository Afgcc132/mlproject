from flask import Flask, render_template, request
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)

# Create the pipeline object once when the app starts.
# This is much more efficient as it loads the model only one time.
predict_pipeline = PredictPipeline()
##Ruta para la página principal
@application.route('/')
def home():
    return render_template('index.html')

@application.route('/predictdata', methods=['POST', 'GET' ])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
        
    else :
        data = CustomData(  
            gender= request.form.get('gender'),
            race_ethnicity= request.form.get('ethnicity'),
            parental_level_of_education= request.form.get('parental_level_of_education'),
            lunch= request.form.get('lunch'),
            test_preparation_course= request.form.get('test_preparation_course'),
            reading_score= int(request.form.get('reading_score')),
            writing_score= int(request.form.get('writing_score'))
        )
        pred_df = data.get_data_as_dataframe()
        print(pred_df)
        # Use the globally created pipeline object
        results = predict_pipeline.predict(pred_df)
        return render_template('home.html', results=results[0])

if __name__ == "__main__":
    app.run(host='0.0.0.0')
