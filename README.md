# Typing Shapes
Which words have the most common shapes on the keyboard?


Inspired by [Matt Parker's video](https://youtu.be/Mf2H9WZSIyw?t=843), where he claims that typing the word _minimum_ is the maximum fun because of its shape on the keyboard, I set out to find which other words have that same shape. (For example, _minimum_ transposed one key to the left, gives _nubunyb_, but that's not a word.)

It turns out that no other word has the shape of _minimum_ :-(. In fact, most word shapes are unique.

So I set out to find the most common word shape on a Qwerty keyboard (for words of at least 4 letters).


![Six letter shapes](WaxingEscortPaths.png)

### Results

Using the list of 466,550 words from https://github.com/dwyl/english-words , ignoring words with characters outside of A-Z (~11%), the most common shape had four instances:

1. Dede
1. Juju
1. Kiki
1. Lolo


### And what about Dvorak!?

_Minimum_ is still unique on Dvorak. But there was a shape with five occurences, and another with six.

1. Dada
1. Hoho
1. Lyly
1. Nunu
1. Sisi
1. Tete

### What's the longest duplicated shape?

On Qwerty, there were 10 pairs of 6 letter words that shared a shape:


These were:

1. Aguara and Shists
1. Busied and Nidorf
1. Cammas and Geller
1. Cinura and Vomits
1. Escort and Waxier (Pictured above)
1. Imperf and Unowed
1. Kellet and Nammad
1. Lekker and Mannas
1. Reggie and Saccha
1. Riedel and Shazam

On Dvorak, the longest words that shared a shape were 5 letters long. the Triplet:

1. Dagga, Hocco and Terre

Finding the longest word was found by manually incrementing the _MINIMUM_WORD_LENGTH_