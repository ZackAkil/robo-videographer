
'''
File for processing images and producing predictions
on where the action is happening within the scene.

'''
import os
import numpy as np
from sklearn.externals import joblib

PREDICTOR_FILE_NAME = 'rugby_predictor.pkl'
FRAME_HEIGHT = 480
FRAME_WIDTH = 640
UPPER_FRAME = 300
LOWER_FRAME = 200
THRESHOLD = 30
HORZ_DIFF_SUM_BINS = 20
VERT_SUM_NORMALISER = UPPER_FRAME - LOWER_FRAME

# load prediction model
MODULE_PATH = os.path.dirname(os.path.abspath(__file__)) + '/'
PREDICTOR = joblib.load(MODULE_PATH + PREDICTOR_FILE_NAME)


def predict_action_pos(frame):
    prediction = feed_frame_for_prediction(frame)
    if prediction:
        return prediction[0]
    else:
        return 0.5

frame_1_store = np.ones((FRAME_HEIGHT, FRAME_WIDTH))
frame_2_store = np.ones((FRAME_HEIGHT, FRAME_WIDTH))
frame_3_store = np.ones((FRAME_HEIGHT, FRAME_WIDTH))

def feed_frame_for_prediction(frame):
    global frame_1_store
    global frame_2_store
    global frame_3_store

    frame_3_store = frame_2_store
    frame_2_store = frame_1_store
    frame_1_store = frame

    trans_frame_1 = transform_images(frame_3_store, frame_2_store)
    trans_frame_2 = transform_images(frame_2_store, frame_1_store)
    input_data = np.concatenate((trans_frame_1, trans_frame_2), axis=0)
    return PREDICTOR.predict(input_data.reshape(1, -1))

def transform_images(frame_1, frame_2):
    vert_diff_sums = get_verticle_diff_sum(frame_1, frame_2)
    horz_diff_sum_binned = bin_sum(vert_diff_sums, HORZ_DIFF_SUM_BINS)/VERT_SUM_NORMALISER
    return horz_diff_sum_binned

def get_verticle_diff_sum(frame_1, frame_2):
    diff = (frame_1[LOWER_FRAME:UPPER_FRAME] - frame_2[LOWER_FRAME:UPPER_FRAME]) > THRESHOLD
    return diff.sum(axis=0)

def bin_sum(data_array, bins):
    bin_size = int(len(data_array)/bins)
    return data_array.reshape(-1, bin_size).sum(axis=1)
