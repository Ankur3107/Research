# +
import os
from tensorflow.contrib import predictor

class testQA(object):
    def __init__(self, d_id, model_path):
        os.environ['CUDA_VISIBLE_DEVICES'] = d_id
        self.predict_fn = predictor.from_saved_model(model_path)
# -


