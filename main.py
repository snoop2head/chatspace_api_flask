from flask import Flask, request, jsonify
from datetime import date, datetime, timedelta
import re
from chatspace import ChatSpace

spacer = ChatSpace()

# today's date
today_int = date.today()
print("test_app - Today's date:", today_int)

# app is Flask
app = Flask(__name__)


@app.route("/", methods=["POST"])
def sentence_proofreader():
    data_receive = request.get_json()
    print(data_receive)
    sentence_kor = data_receive["text"]
    spaced_text = spacer.space(sentence_kor)
    data_send = {"spaced_text": spaced_text}
    print(data_send)
    return jsonify(data_send)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
