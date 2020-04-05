# Chatspace AI
This project aims to separate Chatspace from web server as independent API.

Chatspace is Korean Sentence spacing module according to grammar. Being developed by chatbot company [Pingpong](https://github.com/pingpong-ai/chatspace), it shows good performance for proofreading. 

But Chatspace uses torch as dependency. On linux, torch module takes up 750MB of disk space in linux environment. Thus it’s too heavy to run with other applications on the same server. 
