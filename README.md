# NetworkSecurityCourse
Codes of lesson of Network Security in winter and spring of 2023 

There is a __report__ in each file that describe what is happening in that. 

# Affine Cipher
The Affine cipher is a type of monoalphabetic substitution cipher, wherein each letter in an alphabet is mapped to its numeric equivalent, encrypted using a simple mathematical function, and converted back to a letter.

# Shift Cipher
A Shift cipher is a simple method of encoding messages. Shift ciphers use a substitution method where letters in the alphabet are shifted by some fixed number of spaces to yield an encoding alphabet. A Shift cipher with a shift of 1 would encode an A as a B, an M as an N, and a Z as an A, and so on.

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

$P^{-1} P K = P^{-1} C$

$K = P^{-1} C$

So if we find the inverse of P we can attack very easy.

# Bias
In here we will give all the possible inputs to the 8th S-box to find the bias of outputs. We can see that S-Box has a uniform distribution.

# The Miller–Rabin primality test
The Miller–Rabin primality test or Rabin–Miller primality test is a probabilistic primality test: an algorithm which determines whether a given number is likely to be prime, similar to the Fermat primality test and the Solovay–Strassen primality test.

It is of historical significance in the search for a polynomial-time deterministic primality test. Its probabilistic variant remains widely used in practice, as one of the simplest and fastest tests known.

Gary L. Miller discovered the test in 1976; Miller's version of the test is deterministic, but its correctness relies on the unproven extended Riemann hypothesis. Michael O. Rabin modified it to obtain an unconditional probabilistic algorithm in 1980. 

The algorithm can be written in pseudocode as follows. The parameter k determines the accuracy of the test. The greater the number of rounds, the more accurate the result.

    Input #1: n > 2, an odd integer to be tested for primality
    Input #2: k, the number of rounds of testing to perform
    Output: “composite” if n is found to be composite, “probably prime” otherwise

    let s > 0 and d odd > 0 such that n − 1 = 2sd  # by factoring out powers of 2 from n − 1
    repeat k times:
        a ← random(2, n − 2)  # n is always a probable prime to base 1 and n − 1
        x ← ad mod n
        repeat s times:
            y ← x2 mod n
            if y = 1 and x ≠ 1 and x ≠ n − 1 then # nontrivial square root of 1 modulo n
                return “composite”
            x ← y
        if y ≠ 1 then
            return “composite”
    return “probably prime”

# Elgamal
In cryptography, the ElGamal encryption system is an asymmetric key encryption algorithm for public-key cryptography which is based on the Diffie–Hellman key exchange. It was described by Taher Elgamal in 1985.
     
    1.Bob generates public and private keys: 
      Bob chooses a very large number q and a cyclic group Fq.
      From the cyclic group Fq, he choose any element g and
      an element a such that gcd(a, q) = 1.
      Then he computes h = ga.
      Bob publishes F, h = ga, q, and g as his public key and retains a as private key.
    2.Alice encrypts data using Bob’s public key : 
      Alice selects an element k from cyclic group F 
      such that gcd(k, q) = 1.
      Then she computes p = gk and s = hk = gak.
      She multiples s with M.
      Then she sends (p, M*s) = (gk, M*s).
    3.Bob decrypts the message : 
      Bob calculates s′ = pa = gak.
      He divides M*s by s′ to obtain M as s = s′

# Diffe-Hellman key exchange
The Diffie Hellman key exchange algorithm can be used to encrypt; one of the first schemes to do is ElGamal encryption. One modern example of it is called Integrated Encryption Scheme, which provides security against chosen plain text and chosen clipboard attacks.
