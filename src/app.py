from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('setup'))

@app.route('/setup', methods=['GET','POST'])
def setup():
    if request.method == 'POST':
        studentID = request.form.get('studentID')
        allocationTime = request.form.get('allocationTime')
        print(f'[SUBMISSION] StudentID: {studentID} Time: {allocationTime}')
    return render_template('setup.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
