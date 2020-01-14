import argparse
import json
import os

parser = argparse.ArgumentParser(description="Assemble or edit corpus of words for solving NYT Spelling Bee puzzle.")
parser.add_argument('--base_word_list', default='', help='Path to word list for constructing jumble dictionary.')
parser.add_argument('--in_jumble_dict_path', default='./jumble_dicts/jumble_dict.json', help='Path to jumble dict json path')
parser.add_argument("--out_jumble_dict_path", default='./jumble_dicts/jumble_dict.json', help='Path to write edited jumble dict to.')
parser.add_argument('--edit_word_list_json', default='', help='Path to json file containing words to add and words to remove from existing jumble dict.')

args = parser.parse_args()

def generate_jumble_dict(word_list_path):
    """
    :param word_list_path: str, path to word list (1 per line) to construct jumble dict from.
    :return: jumble_dict: dict, english words keyed by sorted letters they contain, ex: { 'aabcsu' : ['abacus'] }
    """
    jumble_dict = {}

    assert os.path.isfile(word_list_path), "Input word list file %s does not exist." % word_list_path

    with open(word_list_path) as f:
        word_list = f.read().splitlines()

    assert len(word_list) > 0, "Input word list is empty."

    for word in word_list:
        key = ''.join(sorted(word))
        jumble_dict.setdefault(key, []).append(word)

    print("%d words in word list" % len(word_list))
    print("%d keys in jumble dict" % len(jumble_dict))
    print('\n')

    return jumble_dict

def edit_jumble_dict(jumble_dict, words_to_add = [], words_to_remove=[]):
    """
    Add each word in words to add to jumble dict using its sorted letters as a key,
    by either creating a new entry or appending to existing list.
    Ex:
        Word to add: "abacus"
        key: 'aabcsu', value: ['abacus']
    """
    if words_to_add:
        for word_to_add in words_to_add:
            sorted_letters = ''.join(sorted(word_to_add))

            # Cannot json serialize sets
            if word_to_add not in jumble_dict.get(sorted_letters, []):
                jumble_dict.setdefault(sorted_letters, []).append(word_to_add)
    """
    Remove each word in words to remove from jumble dict by sorting its letters to find the key,
    then filtering it out of the list of values.

    Ex:
        Word to remove:
            'domination'
            jumble_dict before:
                key: 'adiimnnoot', value: ['admonition', 'domination'],
            after:
                key: 'adiimnnoot', value: ['admonition'],
    """
    if words_to_remove:
        for word_to_remove in words_to_remove:
            sorted_letters = ''.join(sorted(word_to_remove))
            existing_entry = jumble_dict.pop(sorted_letters, [])

            edited_entry = [i for i in existing_entry if i != word_to_remove]
            if len(edited_entry) > 0:
                jumble_dict[sorted_letters] = edited_entry

    return jumble_dict

def write_jumble_dict_json(jumble_dict, out_jumble_dict_path):
    with open(out_jumble_dict_path, 'w') as f:
        json.dump(jumble_dict, f)

if __name__ == "__main__":

    assert bool(args.base_word_list) != bool(args.edit_word_list_json), "User must provide base word list or list of words to add/remove (but not both)"

    #Generate jumble dict from word list in text file
    if args.base_word_list:
        print("Generating jumble dict from word list...")
        jumble_dict = generate_jumble_dict(args.base_word_list)

        print("Writing jumble dict to %s... " % args.out_jumble_dict_path)
        write_jumble_dict_json(jumble_dict, args.out_jumble_dict_path)

    #Edit existing jumble dict using a json containing words to add and/or words to remove
    elif args.edit_word_list_json:
        with open(args.edit_word_list_json) as f:

            print("Editing existing jumble dict %s..." % args.in_jumble_dict_path)
            with open(args.in_jumble_dict_path) as f:
                jumble_dict = json.load(args.in_jumble_dict_path)

            print("Getting words to add/remove from %s..." % args.edit_word_list_json)
            edit_words_dict = json.load(f)
            words_to_add = edit_words_dict.get('words_to_add', [])
            words_to_remove = edit_words_dict.get('words_to_remove', [])

            print("Editing jumble dict...")
            edited_jumble_dict = edit_jumble_dict(jumble_dict, words_to_add, words_to_remove)

            print("Writing edited jumble dict to %s..." % args.out_jumble_dict_path)
            write_jumble_dict_json(jumble_dict, args.out_jumble_dict_path)