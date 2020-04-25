# Sentiment-Analysis
Recreation of the paper "Thumbs up? Sentiment Classification using Machine Learning Techniques" by Bo Pang and Lillian Lee.

### Approach

- Features are constructed as mentioned in the paper. Features are:
  1. unigrams (occuring atleast 4 times) [frequncies as values]
  2. unigrams (occuring atleast 4 times) [presence as values]
  3. bigrams (top ~ 15000)
  4. unigrams + bigrams [presence as values]
  5. POS tagged unigrams (occuring atleast 4 times)
     - used nltk pos tagger for tagging words
  6. adjectives (all of them)
  7. top unigrams (according to the number of adjectives, aroung 3000)
  8. unigrams along with positions

  > Program for Processing the data is in `/setup.ipynb`

- Three models:
  1. Multinomial Navie Bayes
  2. Support Vector Classifier
  3. Logistic Regression
 
   are trained on 3-fold and mean accuracies are printed.
  
> Code is in `/Sentiment Analysis.ipynb`

### Results

| Features | #of features	| Naive Bayes	| SVC	| Logistic Regression |
| -------- | ------------ | ----------- | --- | ------------------- |
| unigram freqs |	15521	|	79.86	| 70.29	|	82.07 |
| unigram pres|	15521	|	82.14	|	83.21	|	84.79 |
| uni+bigrams	| 31042	|	83.14	|	81.71	|	85.14 |
| bigrams pres |	15521	|	81.07	|	75.50	|	78.14 |
| POS Tags | 17380	|	81.50	|	82.36	|	85.00 |
| adjectives | 3065	|	78.29	| 76.71	|	77.50 |
| top unigrams	| 3065	|	82.36	|	83.64	|	83.00 |
| uni positions	| 21744	|	81.71	|	76.93	|	79.50 |
