def get_num_of_characters(input_str):
    count = 0
    for char in input_str:
        count += 1
    return count



if _name_ == '_main_':
    print('Enter a sentence or phrase:')
    input_str = input()
    print('You entered: {}'.format(input_str))
    print('Number of characters: ', get_num_of_characters(input_str))
    print('String with no whitespace: ', input_str.replace(' ', ''))
