# NetworkSecurityCourse
Codes of lesson of Network Security in winter and spring of 2023 

# Affine Cipher
The Affine cipher is a type of monoalphabetic substitution cipher, wherein each letter in an alphabet is mapped to its numeric equivalent, encrypted using a simple mathematical function, and converted back to a letter.

# Caesar Cipher
A Caesar cipher is a simple method of encoding messages. Caesar ciphers use a substitution method where letters in the alphabet are shifted by some fixed number of spaces to yield an encoding alphabet. A Caesar cipher with a shift of 1 would encode an A as a B, an M as an N, and a Z as an A, and so on.

# Hill Cipher
Hill cipher is a polygraphic substitution cipher based on linear algebra.Each letter is represented by a number modulo 26. Often the simple scheme A = 0, B = 1, …, Z = 25 is used, but this is not an essential feature of the cipher. To encrypt a message, each block of n letters (considered as an n-component vector) is multiplied by an invertible n × n matrix, against modulus 26. To decrypt the message, each block is multiplied by the inverse of the matrix used for encryption.
The matrix used for encryption is the cipher key, and it should be chosen randomly from the set of invertible n × n matrices (modulo 26).

# Play Fair Cipher
The Playfair cipher or Playfair square or Wheatstone–Playfair cipher is a manual symmetric encryption technique and was the first literal digram substitution cipher. The scheme was invented in 1854 by Charles Wheatstone, but bears the name of Lord Playfair for promoting its use.
The technique encrypts pairs of letters (bigrams or digrams), instead of single letters as in the simple substitution cipher and rather more complex Vigenère cipher systems then in use. The Playfair is thus significantly harder to break since the frequency analysis used for simple substitution ciphers does not work with it. The frequency analysis of bigrams is possible, but considerably more difficult. With 600 possible bigrams rather than the 26 possible monograms (single symbols, usually letters in this context), a considerably larger cipher text is required in order to be useful.

# Permutation Cipher
In cryptography, a transposition cipher is a method of encryption which scrambles the positions of characters without changing the characters themselves. Transposition ciphers reorder units of plaintext according to a regular system to produce a ciphertext which is a permutation of the plaintext.

# Substitution Cipher
In cryptography, a substitution cipher is a method of encrypting in which units of plaintext are replaced with the ciphertext, in a defined manner, with the help of a key; the "units" may be single letters (the most common), pairs of letters, triplets of letters, mixtures of the above, and so forth. The receiver deciphers the text by performing the inverse substitution process to extract the original message. 

# Shift Attack
If we want to attack we just need one plain word and one cipher word to compare them and find the difference.

# Affine Attack
As we know in Affine cipher we just have an equation with two values of 'a' and 'b', so for attacking we just need to have a brute force on a and b.

# Hill Attack
As we know the structure of Hill cipher is:

[p1 p2 p3] K = [c1 c2 c3]
 
But if we concat three block of plain text and three block of cipher text we will have:

PK = C

Now for attacking to Hill cipher we can do:

P^-1 P K = P^-1 C

K = P^-1 C

So if we find the inverse of P we can attack very easy.
