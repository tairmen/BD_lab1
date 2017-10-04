import pickle

def create_file(name):
    data = [(
            "kv-52",
            [("Abduraimov", 48023, 20), ("Kovalev", 90454, 21), ("Depp", 48785, 40), ("Mocart", 90456, 90)]),
        (
            "kp-42",
            [("Ivanov", 43225, 33), ("Tolstoy", 42321, 66), ("Pushkin", 53213, 54), ("Ahmatova", 42343, 41)]),
        (
            "km-73",
            [("Hachaturyan", 53212, 70), ("Chaykovskiy", 23456, 77), ("Obama", 42399, 40)]),
        (
            "km-62",
            [("Bob", 31233, 18), ("Smith", 31234, 22), ("Trump", 94833, 60)])
    ]
    with open(name, 'wb') as f:
        pickle.dump(data, f)
