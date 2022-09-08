# NLP Persian Poet Identification
In this NLP project, model get a line from one of three famous Iranian poets(Ferdowsi, Hafez, and Molavi), and predicts the poet name as output.<br>
we use a unigram and a bigram model trained on a dataset which contains over 9 thousand lines of poems for each poet.<br>
The probability calculates by backoff model like the following:
```bash
P`(ci | ci-1) = [(y3 * P(ci | ci-1)) + (y2 * P(ci)) + (y1 * e)] 
y1 + y2 + y3 = 1 
0 < e < 1 
```
After tuning the above parameter, I got accuracy= 91 % by following parameters: 
```bash
y1 = 0.05
y2 = 0.1
y3 =0.85
e = 10 ^-6 
```

