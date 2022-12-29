import re


def get_min_size(x: str, y: str):
    if x is None or y is None:
        return None
    x_result = sum(map(float, re.findall(r'\d+', x)))
    y_result = sum(map(float, re.findall(r'\d+', y)))
    if x_result < y_result:
        return x
    return y
