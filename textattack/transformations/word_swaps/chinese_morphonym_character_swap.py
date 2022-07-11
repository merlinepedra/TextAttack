import os

from textattack.shared.data import MORPHONYM_LS

from .word_swap import WordSwap


class ChineseMorphonymCharacterSwap(WordSwap):
    """Transforms an input by replacing its words with synonyms provided by a
    homophone dictionary."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def _get_replacement_words(self, word):
        """Returns a list containing all possible words with 1 character
        replaced by a homophone."""
        word = list(word)
        candidate_words = set()
        for i in range(len(word)):
            character = word[i]
            for char_morpho_ls in MORPHONYM_LS:
                if character in char_morpho_ls:
                    for new_char in char_morpho_ls:
                        temp_word = word
                        temp_word[i] = new_char
                        candidate_words.add("".join(temp_word))
        #print(candidate_words)
        return list(candidate_words)






        for i in range(len(word)):
            character = word[i]
            character = pinyin.get(character, format="strip", delimiter=" ")
            if character in self.homophone_dict.values:
                for row in range(self.homophone_dict.shape[0]):  # df is the DataFrame
                    for col in range(0, 1):
                        if self.homophone_dict._get_value(row, col) == character:
                            for j in range(1, 4):
                                repl_character = self.homophone_dict[col + j][row]
                                if repl_character is None:
                                    break
                                candidate_word = (
                                    word[:i] + repl_character + word[i + 1 :]
                                )
                                candidate_words.append(candidate_word)
            else:
                pass
        return candidate_words
