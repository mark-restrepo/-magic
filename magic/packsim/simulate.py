from magic.packsim.config import ZNR_CARDLIST
from magic.packsim.pack import ZnrPack

import numpy as np
import pandas as pd
import json


def load_cards(fn=ZNR_CARDLIST):
    with open(fn, 'r') as file:
        r = file.read()
    j = json.loads(r)

    df = pd.DataFrame(j)
    return df


def generate_packs(card_df, n_packs=1000):
    packs = []
    for i in np.arange(0, n_packs):
        zp = ZnrPack(card_df)
        packs.append(zp)
    return packs
