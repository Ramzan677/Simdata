from flask import Flask, request, render_template_string, render_template
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        mobile = request.form.get('mobile')
        if mobile:
            try:
                response = requests.get(f"http://tmphpscripts.xyz/Tajammal.php?num={mobile}")
                response.raise_for_status()
                data = response.json()
                return render_template('index.html', data=json.dumps(data, indent=4))
            except requests.exceptions.RequestException as e:
                return render_template('index.html', error=str(e))
        else:
            return render_template('index.html', error="Please enter a valid mobile number.")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
