from magic.packsim.simulate import load_cards, generate_packs
from magic.utils.constants import WUBRG
from magic.utils.parse import bucket_multicolor

import pandas as pd
import matplotlib.pyplot as plt

card_df = load_cards()
all_buckets = bucket_multicolor(card_df)
all_avg_pick = [all_buckets[color]['avg_pick'] for color in WUBRG]

all_fig, all_ax = plt.subplots()
all_ax.boxplot(all_avg_pick)
all_ax.set_title('Average Pack Take by Color, for all cards')
all_ax.set_xlabel('Color')
all_ax.set_ylabel('Average Pack Taken')
all_ax.set_xticklabels(WUBRG)
all_fig.savefig('images/avgPickAll.png')

packs = generate_packs(card_df)

# All
for i in range(14):
    pack_df = pd.concat([zp.pack_df for zp in packs]).fillna(0)
    pack_buckets = bucket_multicolor(pack_df)
    pack_avg_pick = [pack_buckets[color]['avg_pick'] for color in WUBRG]
    fig, ax = plt.subplots()
    ax.boxplot(pack_avg_pick)
    ax.set_title('After {0} picks'.format(i))
    ax.set_ylim(0, 16)
    ax.set_title('Average Card Power by Color After {0} Picks'.format(i))
    ax.set_xlabel('Color')
    ax.set_ylabel('Average Pack Taken')
    ax.set_xticklabels(WUBRG)
    fig.savefig('images/pick_{0}'.format(i))
    plt.close()
    picks = [pack.make_pick() for pack in packs]

packs = generate_packs(card_df)

# Black
for i in range(14):
    pack_df = pd.concat([zp.pack_df for zp in packs]).fillna(0)
    pack_buckets = bucket_multicolor(pack_df)
    pack_avg_pick = [pack_buckets[color]['avg_pick'] for color in WUBRG]
    fig, ax = plt.subplots()
    ax.boxplot(pack_avg_pick)
    ax.set_title('After {0} picks'.format(i))
    ax.set_ylim(0, 16)
    ax.set_title('Average Card Power by Color After {0} Picks When Black is Cut'.format(i))
    ax.set_xlabel('Color')
    ax.set_ylabel('Average Pack Taken')
    ax.set_xticklabels(WUBRG)
    fig.savefig('images/blackcut_pick_{0}'.format(i))
    plt.close()
    picks = [pack.make_pick(color='B') for pack in packs]

packs = generate_packs(card_df)

# Orzhov
for i in range(14):
    pack_df = pd.concat([zp.pack_df for zp in packs]).fillna(0)
    pack_buckets = bucket_multicolor(pack_df)
    pack_avg_pick = [pack_buckets[color]['avg_pick'] for color in WUBRG]
    fig, ax = plt.subplots()
    ax.boxplot(pack_avg_pick)
    ax.set_title('After {0} picks'.format(i))
    ax.set_ylim(0, 16)
    ax.set_title('Average Card Power by Color After {0} Picks When Orzhov is Cut'.format(i))
    ax.set_xlabel('Color')
    ax.set_ylabel('Average Pack Taken')
    ax.set_xticklabels(WUBRG)
    fig.savefig('images/orzhov_pick_{0}'.format(i))
    plt.close()
    picks = [pack.make_pick(color='BW') for pack in packs]
