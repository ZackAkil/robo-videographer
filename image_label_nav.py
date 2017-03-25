from os import listdir
from os.path import isfile, join
import pandas as pd

class Image_Label_Cycler():
    '''
    Class for managing the navigation through and labeling of a
    folder of images that are labeled by epoch (in seconds).
    e.g 18279712.786.jpg

    '''
    image_folder_path = ''
    file_names = None
    pos_store = {}
    current_image_name = ''

    def get_file_names(self):
        onlyfiles = [f for f in listdir(self.image_folder_path) if isfile(join(self.image_folder_path, f))]
        all_file_names = pd.Series(onlyfiles)
        self.file_names = all_file_names[all_file_names.str.contains('jpg')].sort_values()
        return self.file_names

    def get_index(self, file_name):
        return self.file_names[self.file_names == file_name].index[0]

    def get_next_file_name(self, file_name, step=1):
        i = self.get_index(file_name)
        return self.file_names.loc[i+step]

    def next_photo(self, step=1):
        self.current_image_name = self.get_next_file_name(self.current_image_name, step) 

    def set_image_pos_value(self, file_name, pos_value):
        self.pos_store[file_name] = pos_value

    def set_current_pos_value(self, pos_value):
        self.set_image_pos_value(self.current_image_name,
                                 pos_value)

    def get_image_pos_value(self, file_name):
        if file_name in self.pos_store.keys():
            return self.pos_store[file_name]
        else:
            return None

    def get_current_pos_value(self):
        return self.get_image_pos_value(self.current_image_name)

    def get_latest_unlabeled_image_file_name(self):
        for f in self.file_names:
            if f not in self.pos_store.keys():
                return f

    def set_latest_unlabeled_image_file_name(self):
        self.current_image_name = self.get_latest_unlabeled_image_file_name()

    def save_labels(self, file_name):
        pd.Series(self.pos_store).to_csv(file_name)

    def load_labels(self, file_name):
        label_sr = pd.Series().from_csv(file_name)
        self.pos_store = label_sr.to_dict()
        return self.pos_store

    def __init__(self, image_folder_path, label_csv_file_name = None):
        self.image_folder_path = image_folder_path
        self.get_file_names()
        if label_csv_file_name:
            self.load_labels(label_csv_file_name)
        self.set_latest_unlabeled_image_file_name()
