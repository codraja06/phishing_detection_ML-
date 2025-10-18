from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return '''
    <form action="/submit" method="POST" class="content">
      <div class="search"
        <label for="url">Enter URL:</label>
        <input id="url" type="url" name="url" placeholder="Enter the URL" required>
      </div>
      <input class="submit" type="submit" value="Submit">
    </form>
    '''

@app.route('/submit', methods=['POST'])
def submit():
    user_url = request.form['url']
    return f"<h2>You entered: {user_url}</h2>"

if __name__ == '__main__':
    app.run(debug=True)
