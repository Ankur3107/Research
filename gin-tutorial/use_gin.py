import gin

@gin.configurable
def my_other_func(a, b, c):
    return a, b, c
