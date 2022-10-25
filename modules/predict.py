import dill
import json
import os
import glob
import logging
import pandas as pd

from datetime import datetime


path = os.environ.get('PROJECT_PATH', '..')


def last_added_file(folder):
    files = list(filter(os.path.isfile, glob.glob(folder + "/*")))
    if len(files) > 0:
        files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
        return files[0]
    else:
        return None


def get_predict():
    file_name = last_added_file(f'{path}/data/models')

    with open(file_name, 'rb') as file:
        model = dill.load(file)

    df_prediction = pd.DataFrame(columns=(['car_id', 'predict']))

    for filename in glob.glob(f'{path}/data/test/*.json'):
        with open(filename) as f:
            form = json.load(f)
            df = pd.DataFrame.from_dict([form])
            y = model.predict(df)

            df_prediction = pd.concat([df_prediction, pd.DataFrame({'car_id': df.id, 'predict': y})])

    df_prediction.to_csv(
        f'{path}/data/predictions/predictions_{datetime.now().strftime("%Y%m%d%H%M")}.csv', index=False
    )
    logging.info(f'Predict is saved as {df_prediction}')


if __name__ == '__main__':
    get_predict()
