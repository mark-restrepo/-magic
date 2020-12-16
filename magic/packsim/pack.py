from magic.utils.parse import bucket_multicolor

import random
import numpy as np
import pandas as pd


class ZnrPack:
    def __init__(self, card_df, mythic_p=0.119):
        """
        Creates a random pack of 14 Zendikar Rising Magic cards
        :param card_df: Dataframe containing all ZNR cards and metadata
        :param mythic_p: Probability of this pack having a mythic rare
        """
        # Decide if the pack will contain a mythic rare
        if random.random() < mythic_p:
            self.mythic_pack = True
        else:
            self.mythic_pack = False

        # Sample the cards for the pack
        self.commons = self._sample_cards(card_df, 'common', 10)
        self.uncommons = self._sample_cards(card_df, 'uncommon', 3)
        if self.mythic_pack:
            self.rare = self._sample_cards(card_df, 'mythic', 1)
        else:
            self.rare = self._sample_cards(card_df, 'rare', 1)

        # Build the pack
        self.pack_df = pd.concat([card_df.loc[self.commons],
                                 card_df.loc[self.uncommons],
                                 card_df.loc[self.rare]])

    def get_mean_avg_pick(self, by_color=False):
        """
        Get's the mean average pick value for this pack
        :param by_color: Boolean value, if true returns dict of 5 results, one for each color
        :return: dict of str:double
        """
        if by_color:
            buckets = bucket_multicolor(self.pack_df)
            return {k: v['avg_pick'].mean() for k, v in buckets.items()}
        else:
            return {'overall': self.pack_df['avg_pick'].mean()}

    def make_pick(self, color=None):
        """
        Makes a pick from the pack, removing one card from the pack_df and returning it
        :param color: String value, will select from those colors first if a value is passed
        :return: Series of the pick
        """
        if color:
            color_idx = self.pack_df['color'].apply(lambda val: any(c in val for c in color))
            if any(color_idx):
                trim_df = self.pack_df[color_idx]
                pick = trim_df.sort_values('avg_pick').iloc[0]
                if self.pack_df.loc[pick.name]['avg_pick'] < 8:
                    self.pack_df.drop(pick.name, inplace=True)
                    return pick

        pick = self.pack_df.sort_values('avg_pick').iloc[0]
        self.pack_df.drop(pick.name, inplace=True)
        return pick

    def _sample_cards(self, card_df, rarity, n):
        """
        Internal helper function. Sample cards from card_df to create a pack
        :param card_df: df of the ZNR cardpool
        :param rarity: rarity to sample on
        :param n: number of cards to return
        :return: ids of sampled cards
        """
        pool = card_df[card_df['rarity'] == rarity].index
        return np.random.choice(pool, replace=False, size=n)
