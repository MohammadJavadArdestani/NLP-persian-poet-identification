# NLP-persian-poet-identification
In this NLP problem, given a line from one of three famous Iranian poets(Ferdowsi, Hafez, and Molavi), and get poet name as output.<br>
we use a unigram and a bigram model trained on a train-data(over 9 thousand lines of poems for each poet) and calculate the probability by backoff model.<br>
(ci | ci-1) = y3\*P(ci | ci-1) + y2\*P(ci) + y1*e <br>
y1 + y2 + y3 = 1 <br>
0 < e < 1 <br>
you can set y1,y2,y3 and e for several times and find the best one to increase your accuracy <br>
for this data you can get accuracy= 90% by y1 = 0.05, y2 = 0.1, y3 =0.85, e = 10 ^-6 <br>

