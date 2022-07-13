BACKGROUND_COLOR = "#B1DDC6"

import pandas as pd
import random

data = pd.read_csv("./day_31/data/french_words.csv")
to_learn  = data.to_dict(orient="records")
print(to_learn)
print(random.choice(to_learn))