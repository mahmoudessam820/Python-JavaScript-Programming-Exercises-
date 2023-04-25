'''
    Count the smiley faces!

    Given an array (arr) as an argument complete the function 
    CountSmileys that should return the total number of smiling faces.

    Rules for a smiling face:

    - Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
    - A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
    - Every smiling face must have a smiling mouth that should be marked with either ) or D

    No additional characters are allowed except for those mentioned.

    Valid smiley face examples: :) :D ;-D :~)
    Invalid smiley faces: ;( :> :} :]

    Example:

    countSmileys([':)', ';(', ';}', ':-D']); // should return 2;
    countSmileys([';D', ':-(', ':-)', ';~)']); // should return 3;
    countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;

    Note:

    In case of an empty array return 0. 
    You will not be tested with invalid input (input will always be an array). 
    Order of the face (eyes, nose, mouth) elements will always be the same.

    Task URI: https://www.codewars.com/kata/583203e6eb35d7980400002a
'''


def count_smileys(arr):
    valid_smiley = [':)', ':D', ';-D', ':~)', ';~)', ';D', ':-D', ':-)', ';~D']
    smile = [x for x in arr if x in valid_smiley]
    return len(smile)


print(count_smileys([':)', ';(', ';}', ':-D', ';~D']))
