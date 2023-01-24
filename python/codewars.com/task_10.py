'''
    Simple Encryption #1 - Alternating Split 💥

    - Implement a pseudo-encryption algorithm which given a string S and an integer N
    - Concatenates all the odd-indexed characters of S with all 
    - The even-indexed characters of S.
    - This process should be repeated N times.

    Examples:

    encrypt("012345", 1)  =>  "135024" 
    encrypt("012345", 2)  =>  "135024"  ->  "304152"
    encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"

    Together with the encryption function, you should also implement 
    A decryption function which reverses the process.

    If the string S is an empty value or the integer N is not positive, 
    return the first argument without changes.

    Task URL: https://www.codewars.com/kata/simple-encryption-number-1-alternating-split

'''

'''
    Note: 

    When I did submit my solution to this problem this message appears to me.
    
    Our servers are configured to only allow a certain amount of time for your code to execute. 
    In rare cases the server may be taking on too much work and simply wasn't able to run your code efficiently enough. 
    Most of the time though this issue is caused by inefficient algorithms. 
    If you see this error multiple times you should try to optimize your code further.

    This means my algorithms are not efficient 😑😔
    But I will work on it to improve my algorithm performance 💪. 

'''


def encrypt(text: str, n: int):
    if not text:
        return text
    elif n < 0:
        return text
    else:
        odd_index = ''
        even_index = ''
        count = 0
        result = []
        while True:
            for i in range(0, len(text)):
                if i % 2:
                    odd_index += text[i]
                else:
                    even_index += text[i]
            count += 1
            if count <= n:
                result.append(odd_index + even_index)
                odd_index = ''
                even_index = ''
            if count == n:
                break
        return result


print(encrypt('finally, I did solve it', 3))


def decrypt(encrypted_text: str, n: int):
    if not encrypted_text:
        return encrypted_text
    elif n < 0:
        return encrypted_text
    else:
        half_index = len(encrypted_text) // 2
        odd_index = encrypted_text[0:half_index]
        even_index = encrypted_text[half_index:]

        content = ''
        count = 0
        result = []

        while True:
            for i in range(0, half_index):
                content += even_index[i] + odd_index[i]

            if len(even_index) != 0:
                content += even_index[-1]

            count += 1

            if count <= n:
                result.append(content)
                content = ''
            if count == n:
                break

        return result


print(decrypt('ial Iddsleifnly  i ov t', 3))
