from Flask import Flask
app = Flask(__name__)

@app.route(‘/’)
def hello_world():
  return ‘Hello, world!’

If __name__ == ‘__main__’:
  app.run(debug=True)
