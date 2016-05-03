from flask import Flask

app = flask(__name__)

@app.route("/")
def home():
  return "Under Construct"

if __name__ == '__main__':
  app.run(port=5000, debug = True)
