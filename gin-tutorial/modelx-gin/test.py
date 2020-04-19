
import gin
gin.parse_config_file('config.gin')

from model_gin import BiLSTMGRUSpatialDropout1D
from tensorflow.keras.layers import *
from tensorflow.keras.models import *

input_shape = (100,)
model_input = Input(shape=input_shape)
bilstm_layers = BiLSTMGRUSpatialDropout1D()(model_input)

output = Dense(3, activation='softmax')(bilstm_layers)
full_model = Model(inputs=model_input, outputs=output)
print(full_model.summary())
