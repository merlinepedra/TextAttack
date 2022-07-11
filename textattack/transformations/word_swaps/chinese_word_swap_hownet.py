import OpenHowNet

from .word_swap import WordSwap


class ChineseWordSwapHowNet(WordSwap):
    """Transforms an input by replacing its words with synonyms provided by
    WordNet."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hownet_dict = OpenHowNet.HowNetDict(init_sim=True)

    def _get_replacement_words(self, word):
        """Returns a list containing all possible words with N characters
        replaced by a homoglyph."""
        return self.hownet_dict.get_nearest_words(word, language="zh", K=3, merge=True)
