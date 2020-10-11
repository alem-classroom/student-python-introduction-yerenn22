def reverse_dict(dict):
    dict = {v:k for k, v in dict.items()}
    return dict