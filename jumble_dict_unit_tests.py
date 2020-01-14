import unittest
import generate_jumble_dict
import json

class TestJumbleDict(unittest.TestCase):

    def test_generate_jumble_dict(self):
        """
        Generate a jumble dict from a text file containing a list of words.
        """
        data = {
            'aagnorrt': sorted(['arrogant', 'tarragon']),
            'eerst': sorted(['steer', 'ester', 'reset', 'trees']),
            'deirw': sorted(['weird', 'wider', 'wired'])
        }

        test_word_list_path = './unit_testing_data/test_jumble_word_list.txt'

        generated_jumble_dict = generate_jumble_dict.generate_jumble_dict(test_word_list_path)

        self.assertEqual(data, generated_jumble_dict)

    def test_add_word_to_jumble_dict(self):
        """
        Add a single word to an existing entry in an existing jumble dict.
        """
        jumble_dict_with_added_word = {
            'aagnorrt': sorted(['arrogant', 'tarragon']),
            'eerst': sorted(['steer', 'ester', 'reset', 'trees']),
            'deirw': sorted(['weird', 'wider', 'wired'])
        }

        jumble_dict_without_added_word = {
            'aagnorrt': sorted(['arrogant', 'tarragon']),
            'eerst': sorted(['steer', 'ester', 'reset', 'trees']),
            'deirw': sorted(['weird', 'wider'])
        }

        results = generate_jumble_dict.edit_jumble_dict(jumble_dict_without_added_word, words_to_add=['wired'])

        self.assertEqual(jumble_dict_with_added_word, results)

    def test_add_entry_to_jumble_dict(self):
        """
        Add multiple words as a new entry to an existing jumble dict.
        """
        jumble_dict_with_added_word = {
            'aagnorrt': sorted(['arrogant', 'tarragon']),
            'eerst': sorted(['steer', 'ester', 'reset', 'trees']),
            'deirw': sorted(['weird', 'wider', 'wired'])
        }

        jumble_dict_without_added_entry = {
            'aagnorrt': sorted(['arrogant', 'tarragon']),
            'eerst': sorted(['steer', 'ester', 'reset', 'trees']),
        }

        results = generate_jumble_dict.edit_jumble_dict(jumble_dict_without_added_entry, words_to_add=['weird', 'wider', 'wired'])

        self.assertEqual(jumble_dict_with_added_word, results)

    def test_add_words_from_edit_json_to_jumble_dict(self):
        """
        Load a list of words to add from an edit word dict json and add them to a jumble dict.
        """
        jumble_dict_with_words_to_add = {
            'aagnorrt': sorted(['arrogant', 'tarragon']),
            'eerst': sorted(['steer', 'ester', 'reset', 'trees']),
            'deirw': sorted(['weird', 'wider', 'wired'])

        }

        jumble_dict_without_words_to_add = {
            'aagnorrt': sorted(['arrogant', 'tarragon']),
            'eerst': sorted(['steer', 'ester', 'reset', 'trees']),
        }

        with open('./unit_testing_data/test_edit_word_dict.json') as f:
            edit_words_dict = json.load(f)
            words_to_add = sorted(edit_words_dict.get('words_to_add',[]))

        results = generate_jumble_dict.edit_jumble_dict(jumble_dict_without_words_to_add, words_to_add=words_to_add)

        self.assertEqual(jumble_dict_with_words_to_add, results)

    def test_remove_word_from_jumble_dict(self):
        """
        Remove a single word from an entry in a jumble dict.
        """
        jumble_dict_with_word_to_remove = {
            'aagnorrt': sorted(['arrogant', 'tarragon']),
            'eerst': sorted(['steer', 'ester', 'reset', 'trees']),
            'deirw': sorted(['weird', 'wider', 'wired'])
        }

        jumble_dict_without_word_to_remove = {
            'aagnorrt': sorted(['arrogant', 'tarragon']),
            'eerst': sorted(['steer', 'ester', 'reset', 'trees']),
            'deirw': sorted(['weird', 'wider'])
        }

        results = generate_jumble_dict.edit_jumble_dict(jumble_dict_with_word_to_remove, words_to_remove=['wired'])

        self.assertEqual(jumble_dict_without_word_to_remove, results)

    def test_remove_entry_from_jumble_dict(self):
        """
        Remove multiple words (a complete entry) from a jumble dict.
        """

        jumble_dict_with_entry_to_remove = {
            'aagnorrt': sorted(['arrogant', 'tarragon']),
            'eerst': sorted(['steer', 'ester', 'reset', 'trees']),
            'deirw': sorted(['weird', 'wider', 'wired'])
        }

        jumble_dict_without_entry_to_remove = {
            'aagnorrt': sorted(['arrogant', 'tarragon']),
            'eerst': sorted(['steer', 'ester', 'reset', 'trees']),
        }

        results = generate_jumble_dict.edit_jumble_dict(jumble_dict_with_entry_to_remove, words_to_remove=['weird', 'wider', 'wired'])

        self.assertEqual(jumble_dict_without_entry_to_remove, results)

    def test_remove_words_from_edit_json_to_jumble_dict(self):
        """
        Load a list of words to remove from an edit word dict json and remove them from a jumble dict.
        """

        jumble_dict_with_words_to_remove = {
            'aagnorrt': sorted(['arrogant', 'tarragon']),
            'eerst': sorted(['steer', 'ester', 'reset', 'trees']),
            'deirw': sorted(['weird', 'wider', 'wired'])
        }

        jumble_dict_without_words_to_remove = {
            'aagnorrt': sorted(['arrogant', 'tarragon']),
            'eerst': sorted(['steer', 'ester', 'reset', 'trees']),
        }

        with open('./unit_testing_data/test_edit_word_dict.json') as f:
            edit_words_dict = json.load(f)
            words_to_remove = sorted(edit_words_dict.get('words_to_remove',[]))

        results = generate_jumble_dict.edit_jumble_dict(jumble_dict_with_words_to_remove, words_to_remove=words_to_remove)

        self.assertEqual(jumble_dict_without_words_to_remove, results)

if __name__ == '__main__':
    unittest.main()