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


def encrypt(text: str, n: int) -> str:

    if not text or n < 0:
        return text

    for _ in range(n):

        odd_chars = []
        even_chars = []

        for i, char in enumerate(text):

            if i % 2:
                odd_chars.append(char)
            else:
                even_chars.append(char)

        text = ''.join(odd_chars + even_chars)

    return text


def decrypt(encrypted_text: str, n: int) -> str:

    if not encrypted_text or n < 0:
        return encrypted_text

    length = len(encrypted_text)
    half_length = length // 2

    for _ in range(n):

        odd_chars = encrypted_text[:half_length]
        even_chars = encrypted_text[half_length:]

        decrypted_chars = []

        for i, j in zip(even_chars, odd_chars):

            decrypted_chars.append(i)
            decrypted_chars.append(j)

        if length % 2 == 1:

            decrypted_chars.append(even_chars[-1])

        encrypted_text = ''.join(decrypted_chars)

    return encrypted_text


text = 'finally, I did solve it'
n = 3
encrypted_text = encrypt(text, n)
print(encrypted_text)

decrypted_text = decrypt(encrypted_text, n)
print(decrypted_text)


# def encrypt(text: str, n: int):
#     if not text:
#         return text
#     elif n < 0:
#         return text
#     else:
#         odd_index = ''
#         even_index = ''
#         count = 0
#         result = []
#         while True:
#             for i in range(0, len(text)):
#                 if i % 2:
#                     odd_index += text[i]
#                 else:
#                     even_index += text[i]
#             count += 1
#             if count <= n:
#                 result.append(odd_index + even_index)
#                 odd_index = ''
#                 even_index = ''
#             if count == n:
#                 break
#         return result


# print(encrypt('finally, I did solve it', 3))


# def decrypt(encrypted_text: str, n: int):
#     if not encrypted_text:
#         return encrypted_text
#     elif n < 0:
#         return encrypted_text
#     else:
#         half_index = len(encrypted_text) // 2
#         odd_index = encrypted_text[0:half_index]
#         even_index = encrypted_text[half_index:]

#         content = ''
#         count = 0
#         result = []

#         while True:
#             for i in range(0, half_index):
#                 content += even_index[i] + odd_index[i]

#             if len(even_index) != 0:
#                 content += even_index[-1]

#             count += 1

#             if count <= n:
#                 result.append(content)
#                 content = ''
#             if count == n:
#                 break

#         return result


# print(decrypt('ial Iddsleifnly  i ov t', 3))
