import dill
import pandas as pd
import numpy as np
import os
import flask
import logging
from logging.handlers import RotatingFileHandler
from time import strftime


dill._dill._reverse_typemap['ClassType'] = type
app = flask.Flask(__name__)
model = None

handler = RotatingFileHandler(filename='app.log', maxBytes=100000, backupCount=10)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


def load_model(path):
    # load the pre-trained model
    global model
    with open(path, 'rb') as f:
        model = dill.load(f)
    print(model)


model_path = f"{os.getcwd()}/models/logreg_pipeline.dill"
load_model(model_path)


@app.route("/", methods=["GET"])
def general():
    return """Welcome to animals classification process. Please use 'http://<address>/predict' to POST"""


@app.route("/predict", methods=["POST"])
def predict():
    data = {"success": False}
    dt = strftime("[%Y-%b-%d %H:%M:%S]")
    if flask.request.method == "POST":
        counter = 0
        for k, v in flask.request.get_json().items():
            counter += 1
        if counter < 16:
            data['error'] = "Вы ввели не все признаки. Необходимое количество: 16"
            data['success'] = False
            return flask.jsonify(data)
        elif counter > 16:
            data['error'] = "Вы ввели больше признаков. Необходимое количество: 16"
            data['success'] = False
            return flask.jsonify(data)
        df = pd.DataFrame.from_dict(pd.json_normalize(flask.request.get_json()), orient='columns')
        try:
            preds = model.predict_proba(df)
        except AttributeError as e:
            logger.warning(f'{dt} Exception: {str(e)}')
            data['predictions'] = str(e)
            data['success'] = False
            return flask.jsonify(data)
        animal_class = int(np.where(preds[0] == max(preds[0]))[0])+1
        data["success"] = True
        data["class"] = animal_class
        data["description"] = f"Животное с данными параметрами относится к классу {animal_class}"
    return flask.jsonify(data)


if __name__ == "__main__":
    print(("* Loading the model and Flask starting server..."
           "please wait until server has fully started"))
    port = int(os.environ.get('PORT', 8180))
    app.run(host='0.0.0.0', debug=True, port=port)
