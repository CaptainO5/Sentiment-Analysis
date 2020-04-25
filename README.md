# Sentiment-Analysis
Recreation of the paper "A Sentimental Education: Sentiment Analysis Using Subjectivity  Summarization Based on Minimum Cuts" by Bo Pang and Lillian Lee.

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
