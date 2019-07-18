from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def page():
   return render_template('page.html')

@app.route('/about')
def about():
   return render_template('about.html')



if __name__ =='__main__':
   app.run(debug=True, host='0.0.0.0')
