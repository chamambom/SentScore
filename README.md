# Determining Customer Satisfaction Using Sentiment Analysis [BrandScore]

This is a living document explaining the approach taken for the thesis titled "Evaluating Customer Satisfaction Using Sentiment Analysis: A Case Study for Mobile and Fixed Internet Service Providers in Zimbabwe". 

This thesis is a research paper written in partial fulfillment of the requirements for an MSc in Big Data Analytics degree. The outcome of the thesis was to build a brand reputation engine using the following tools: Spark, Kafka, MongoDB, Twitter, and sentiment analysis.

## Approach

### Building Pipeline

Building a pipeline involved processing real-time data using Spark and MongoDB. Twitter real-time data are pulled using an API and processed using Apache Spark. The data is then staged in MongoDB, where some processing is done on the runtime.

#### Data Flow Process

The Twitter dataset is real-time stream data accessed using the Twitter API. Authentication is required to get tweets from Twitter, which is available after creating a Twitter application in developer mode to get access tokens. The data is continuously flowing to the Spark Streaming instance, where transformation is performed, and data is made available in a Spark temporary table. 

#### Data Ingestion

Fetching Twitter live streaming data requires the following steps:
- Creating a Twitter application
- Connectivity with Spark
- Processing with Spark
- Global Schema

### Processing and Visualization

#### Speed Layer Data

- Stream data from Twitter is in JSON object format, encoded using UTF-8 encoding before sending to Spark. 
- Spark Streaming context is created with a batch interval of 10 seconds. 
- Hashtags are extracted from tweet text, counted, and stored in a DataFrame.
- Data frame is sorted in descending order and top trending hashtags are stored in a Temp Table.
- For Batch layer Data, data is fetched from MongoDB with an Aggregation query for trending keywords with frequency.

### Challenges Faced and Solutions

#### Challenges 

- Determining the context of the tween when
    - A native language like Shona or Ndebele is used.
    - When a tweet is mixed between 1 or more native languages and english.
- Twitter-Spark connectivity issue: Downgraded Spark version to 2.3.x for compatibility.
- Spark-MongoDB connectivity issue: Solved by finding and adding compatible jars from Maven repositories.

## Tools Used

- **Jupyter Notebook**: Used for editing code through a web browser, facilitating a streamlined workflow.
- **Python Libraries** (pandas, pyspark): Used for initial data manipulation and connecting to the Spark pipeline.
- **MongoDB**: Used as the persistent storage database due to its ability to store different data structures efficiently.
- **Apache Spark**: Used for real-time stream processing and batch processing.
- **Tweepy API**: Used for getting real-time streaming data from Twitter.
- **Mongo-Spark-Connector**: Used for connecting Spark with the NoSQL database.