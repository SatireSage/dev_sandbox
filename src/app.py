from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('setup'))

@app.route('/setup', methods=['GET','POST'])
def setup():
    if request.method == 'POST':
        ## Temporarily just grabbing data locally here, remove comment when SSH credentials is implemented
        studentID = request.form.get('studentID')
        allocationTime = int(request.form.get('allocationTimeHours'))*60 + int(request.form.get('allocationTimeMinutes'))

        if allocationTime > 300:
            return render_template('setup.html', warning='Maximum Allocation Time is 5 Hours')
        elif allocationTime == 0:
            return render_template('setup.html', warning='Cannot Have 0 Allocation Time')
        
        print(f'[REQUEST] StudentID: {studentID} Time: {(allocationTime//60)}h{allocationTime%60}m')
        return redirect(url_for('credentials'))
    return render_template('setup.html', warning="")

@app.route('/credentials', methods=['GET'])
def credentials():
    return render_template('credentials.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
