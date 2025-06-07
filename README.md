# twitter-sentiment-us-election-2016
Twitter Sentiment Analysis of the 2016 US Presidential Election

This project analyzes Twitter data related to the 2016 US presidential election, comparing Twitter sentiment for Hillary Clinton and Donald Trump to official polling data. The analysis explores the relationship between social media opinion and traditional polls, as well as geographical and topical patterns in the data.

## About
This repository contains the code and analysis for a project conducted during my Master’s studies at the University of Amsterdam in 2020. The project explores the relationship between Twitter sentiment and polling data during the 2016 US presidential election.

## Project Structure
├── DataLoading.ipynb         # Data loading and initial formatting

├── PreProcessing.ipynb       # Data filtering, tokenization, and normalization

├── Model.ipynb               # Sentiment model training, prediction, and analysis

├── fds_utils.py              # Utility functions for processing and cleaning tweets

├── data/

│   ├── geotagged_tweets_20160812-0912.jsons    # Raw tweet data (JSONL)

│   ├── presidential_polls.csv                  # Official poll data

│   ├── tweets_sample.pkl                       # Intermediate tweet data

│   ├── tweets_sample_normalized.pkl            # Preprocessed tweet data

## Data
For the election-related dataset tweets were collected via Twitter's Streaming API in the 
period 12 September 2016 to 12 October 2016. The monitored hashtags and accounts were: 
'@HillaryClinton', '#maga', '#trumppence16', '#hillaryclinton', '#hillary', '#crookedhillary', 
'#donaldtrump', '#dumptrump', '@realDonaldTrump', '#nevertrump', '#imwithher', 
'#neverhillary', '#trump'. 
The total number of tweets in the original dataset was 26,687,737. After selecting only those 
tweets with geolocation, the number was reduced to 657307

## Workflow Overview
### 1. Data Loading
Load raw Twitter data from a JSONL file and extract key fields such as tweet text, date, language, country, and city.

Store the extracted data in a pandas DataFrame for further processing.

### 2. Data Preprocessing
Filtering: Remove non-English and undefined language tweets to focus the analysis on English-language discussions. Remove tweets made outside of US.

Tokenizing: Use NLTK's TweetTokenizer to split tweet text into tokens (words, hashtags, mentions, etc.).

Normalizing: Lemmatize tokens and remove stopwords and links, preparing the data for sentiment analysis and topic modeling.

### 3. Sentiment Analysis
Train a sentiment classifier using NLTK and a labeled tweet dataset.

Predict sentiment (positive/negative) for each tweet, creating a new column with the predicted label.

This lets us measure and compare the overall positivity/negativity of online discussions about each candidate.

### 4. Topic Modelling
Apply topic modeling (e.g., LDA) to identify major themes of discussion for all tweets and for tweets about each candidate.

This helps us understand what topics dominate the conversation for each candidate and guides the separation of tweets by subject.

### 5. Candidate-Specific Analysis
Separate tweets for Trump and Clinton based on keywords, hashtags, and topic modeling results.

Calculate and visualize sentiment distributions for both candidates.

### 6. Compare Sentiment with Polls
Merge daily Twitter sentiment scores with official polling data for both Trump and Clinton.

Plot sentiment vs. polls: Analyze whether Twitter sentiment trends correspond to trends in traditional polling data, and discuss similarities or differences.

### 7. Geographical Analysis
Aggregate sentiment by city: Identify top cities by tweet volume and analyze sentiment distribution in each.

Visualize the geographical distribution of positive/negative sentiment for both candidates.

## How to Run
Requirements:
requirements.txt

Run the Notebooks in Order:

Start with DataLoading.ipynb to load and extract the data.

Continue with PreProcessing.ipynb for cleaning and preparing the data.

Use Model.ipynb for sentiment analysis, topic modeling, and comparisons with polls.

## Main Files
DataLoading.ipynb
Load, extract, and structure raw tweet data for analysis.

PreProcessing.ipynb
Filtering, tokenization, normalization, and splitting by candidate/topic.

Model.ipynb
Sentiment analysis, topic modeling, comparison with polls, and visualization.

fds_utils.py
Helper functions for data extraction, token normalization, etc.

data/geotagged_tweets_20160812-0912.jsons
Raw tweet data (not provided here due to size).

data/presidential_polls.csv
Poll data for 2016 US presidential candidates (not provided here due to size).

## Project Goals
Understand the relationship between Twitter sentiment and official polling results during the 2016 US election.

Explore the main topics of conversation associated with each candidate.

Examine geographical patterns in political sentiment as expressed on Twitter.

## Credits
NLTK for text processing and sentiment modeling.

## References
2016 US Election Polls.
https://www.kaggle.com/fivethirtyeight/2016-election-polls, last accessed 2020/09/25.
