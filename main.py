from flask import Flask, request, jsonify
from datetime import date
from chatspace import ChatSpace


# today's date
today_int = date.today()
print("test_app - Today's date:", today_int)

# Initializing Flask application
app = Flask(__name__)

# Load ChatSpace
spacer = ChatSpace()

# sentence proofreader api
@app.route("/proofread", methods=["POST"])
def sentence_proofreader():
    proofreaded = {"success": False}
    data_receive = request.get_json()
    print(data_receive)
    sentence_kor = data_receive["text"]
    spaced_text = spacer.space(sentence_kor)
    proofreaded["success"] = True
    proofreaded["spaced_text"] = spaced_text
    print(proofreaded)
    return jsonify(proofreaded)


if __name__ == "__main__":
    print(
        (
            "* Loading Chatspace model and Flask starting server..."
            "please wait until server has fully started"
        )
    )
    app.run(host="0.0.0.0", port=3000, debug=True)
