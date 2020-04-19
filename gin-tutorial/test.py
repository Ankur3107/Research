import gin
gin.parse_config_file('config.gin')
import use_gin
print(use_gin.my_other_func())
