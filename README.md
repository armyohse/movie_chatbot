# Movie chatbot       

* Cornell movie script data

* Seq2Seq tensorflow RNN Encoder-Decoder with Attention

* Deployed on slack API

![Alt text](https://camo.githubusercontent.com/8d80a980e563249371921b5494403878de6e47f4/68747470733a2f2f7777772e6c64732e636f6d2f77702d636f6e74656e742f75706c6f6164732f323031362f30362f63686174626f745f776f726b666c6f775f76322e737667)

# Introduction

Why Chatbot :

A chatbot can have a conversation with a customer but isn't limited by technology because the AI technology is built in to the software.  

What is Seq2Seq :

Seq2seq model is also called RNN encoder-decoder. A Seq2seq model usually consists of one encoder and one decoder. The goal
for Seq2seq in testing time is to generate a sequence given another sequence. 

![Alt text](https://image.slidesharecdn.com/tensorflow05-neural-machine-translation-seq2seq-170704044418/95/tensor-flow05-neuralmachinetranslationseq2seq-6-638.jpg?cb=1504913489)

# Data

Cornell Movie--Dialogs Corpus

This corpus contains a large metadata-rich collection of fictional conversations extracted from raw movie scripts.

- 220,579 conversational exchanges between 10,292 pairs of movie characters
- involves 9,035 characters from 617 movies
- in total 304,713 utterances

# Model

* Pre-processing data
* Bucketing
* Encoder inputes
* 1024 dimension 3 LSTM layers
* Weighted cross-entropy loss for a sequence of logits

* Seq2seq in Tensorflow
   <pre>
   outputs, state = embedding_rnn_seq2seq(encoder_inouts, decoder_inputs, cell, num_encoder_symbols, num_decoder_symbols, embedding_size, output_projection=None, feed_previous=False)          
    </pre>           
   
* Input Length Distribution
   ![Alt text](https://discuss.pytorch.org/uploads/default/original/1X/fc5bf5d4ce1463e65397bd4c5b2c79fabc05692b.png)
   
# Test
* Result after 98,000 Epoch trained 

* Slack Demo


![Alt text](https://raw.githubusercontent.com/armyohse/movie_chatbot/master/image/Screen%20Shot%202017-10-15%20at%207.40.32%20AM.png)

* Test demo on prompt

![Alt text](https://raw.githubusercontent.com/armyohse/movie_chatbot/master/image/Screen%20Shot%202017-10-15%20at%207.50.49%20AM.png)

# Environment
* Python 3.6 / Tensorflow 1.3 / Cuda 7.5 

* Google cloud GPU (NVIDIA Tesla K80)
 
# Steps for Execution

  * data_utils.py = pre-process data
  * seq2seq_model.py = Tensorflow Seq2seq model 
  * train_bot.py = train data
  * bot.py = launching bot in prompt
  * deploy_slack.py = deploy on slack
