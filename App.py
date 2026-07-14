from flask import Flask, render_template, request
app = Flask(__name__, template_folder=".")
@app.route('/', methods=['GET', 'POST'])
def index():
success_message = None
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
success_message = f"Thank you for registering, {name}!"
    return render_template('index.html', success=success_message)
if __name__ == '__main__':
app.run(host='0.0.0.0', port=5000)

