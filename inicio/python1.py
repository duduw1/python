
from time import sleep, time
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    time.sleep(6)
   

if __name__ == "__main__":
    print("Hello wordinharia")
