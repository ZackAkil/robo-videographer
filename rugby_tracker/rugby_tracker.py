
'''
File for processing images and producing predictions
on where the action is happening within the scene.

'''

# import pkg_resources
import os

import numpy as np

from sklearn.externals import joblib

PREDICTOR_FILE_NAME = 'rugby_predictor.pkl'
UPPER_FRAME = 300
LOWER_FRAME = 200
THRESHOLD = 30
HORZ_DIFF_SUM_BINS = 20
VERT_SUM_NORMALISER = UPPER_FRAME - LOWER_FRAME

# load prediction model
MODULE_PATH = os.path.dirname(os.path.abspath(__file__)) + '/'
PREDICTOR = joblib.load(MODULE_PATH + PREDICTOR_FILE_NAME)


def predict_action_pos(frame_1, frame_2):
    predictor_input = transform_images(frame_1, frame_2)
    return PREDICTOR.predict(predictor_input)


def transform_images(frame_1, frame_2):
    vert_diff_sums = get_verticle_diff_sum(frame_1, frame_2)
    horz_diff_sum_binned = bin_sum(vert_diff_sums, HORZ_DIFF_SUM_BINS)

    pass

def get_verticle_diff_sum(frame_1, frame_2):
    diff = (frame_1[LOWER_FRAME:UPPER_FRAME] - frame_2[LOWER_FRAME:UPPER_FRAME])>THRESHOLD
    return diff.sum(axis=0)

def bin_sum(data_array, bins):
    bin_size = int(len(data_array)/bins)
    return data_array.reshape(-1, bin_size).sum(axis=1)
