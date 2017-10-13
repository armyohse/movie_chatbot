# Movie chatbot       

* Cornell movie script data

* Seq2Seq tensorflow deep learning model  

![Alt text](https://www.lds.com/wp-content/uploads/2016/06/chatbot_workflow_v2.svg)

# Introduction

Why reddit :

Most growing technology community.  

Python vs R :

Most hottest two language in data science community.

Aim of this project is to :

Count words frequency grouped for each day for two subreddits.

Predict number of posts comments, ups, downs.

![Alt text](https://github.com/armyohse/reddit_test/blob/master/image/dag.png?raw=true "Optional Title")

# Data

Historical data were downloaded and feeded into kafka, transformed with spark and saved into hbase table with.

Realtime data is being transformed the same way.


* **Ingestion Layer**: Kafka is being used for Data Ingestion. As it is highly scalable , has low latency and high throughput.

 * Reddit post transformed into the following:
 <pre>
        #1
        subreddit letter (R|P),
        sec_to_day #seconds till the start of the post day in utc
        postid
        post_title
        link_to_post
        features
            title_len
            title_num_tokens
            body_len
            body_num_tokens
            post_time
            post_weekday
            post_month
            post_over18
        targets
            num_comments
            ups
            downs

        #2
        subreddit letter (R|P)
        seconds till the start of the post day in utc
        postid
        post_body
        post_title
 </pre>
 * Python app utilizes PRAW library to subscribe on live updates from /r/Python, /r/RLanguage

# Lambda architecture

* **Speed Layer**: Spark Streaming is being used for the stream processing.
  * #1 json simply saved into hbase table
  * #2 json transformed into (word,frequency) pairs that uses to increment appropriate counter in hbase table

* **Batch Layer**: The Batch layer is used for training ml models.
  * Machine learning model was trained on downloaded historical data.

* **Database**: Hbase is used for data storage  because of its consistent and high scale distributed processing nature.
    It provides high speed read , writes and aggregation.
   * Historical data is stored in the following format in table 'historical_reddit'
   <pre>
             {
             'k':f'M{subreddit}{day secs utc}{post.id}',
             'cf':'d',
             'q':'m',
             'value':[features,targets]
             }
             {
             'k':f'M{subreddit}{day secs utc}{post.id}',
             'cf':'d',
             'q':'g',
             'value':[post_title,link_to_post]
             }
             {
             'k':f'W{subreddit}{day secs utc}{token}',
             'cf':'d',
             'q':'w',
             'value':token
             }
             {
             'k':f'W{subreddit}{day secs utc}{token}',
             'cf':'d',
             'q':'c',
             'value':frequency
             }
    </pre>           
   * Realtime data is stored additionally with predicted values in table 'upstream_reddit'
   <pre>
             {
             'k':f'M{subreddit}{day secs utc}{post.id}',
             'cf':'d',
             'q':'p',
             'value':predicted_targets
             }
    </pre>           

* **User Interface/Front-End**: Bokeh python library allows to display huge streaming dataset with high perfomance in web browser.
# Screen-shot

![Alt text](https://github.com/armyohse/reddit_test/blob/master/image/word3.png)

* **Frequent word usage**: Realtime most frequent wors usage in subreddit.

![Alt text](https://github.com/armyohse/reddit_test/blob/master/image/ml.png)

* **Machine Learning(Prediction)**: Predict Vote up / down based on word usage compare to historical data

![Alt text](https://github.com/armyohse/reddit_test/blob/master/image/bokeh_plot_100vs10.png)

* **Bokeh Graphic**: How many times "R language" mention in "Python subreddit", "Python" mention in "R subreddit"

![Alt text](https://github.com/armyohse/reddit_test/blob/master/image/happyword.png)

* **Bokeh Graphic**: Comparing python and R frequently word use "awesome", "cool", "fun", "happy", "helpful", "interesting" in their comments.

* **Demo**

 * #Steps for Execution

  * launch hbase_seed.py to create hbase table and fill them with initial data
  * launch kafka_reddit_historical_data.py to start downloading historical data into kafka
  * launch submit_s-p.py to start historicalStream that process and save data into hbase table 'historical_reddit'
  * launch submit_s-p.py to start trainStream that load train ml model on historical data and save trained model in aws s3
  * launch kafka_reddit_upstream.py to start streaming data into kafka
  * launch submit_s-p.py to start upStream that process and save data into hbase table 'upstream_reddit'
  * launch bokeh_server.py to start bokeh web server with UI
  * open http://spark_master_public_dns_name/bokeh_server to open UI
