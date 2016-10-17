from system.core.controller import *
class Surveys(Controller):
    def __init__(self, action):
        super(Surveys, self).__init__(action)

    def index(self):
        if not 'count' in session:
            session['count'] = 0
        else:
            session['count'] +=1

        return self.load_view('index.html')

    def process(self):
        if len(request.form['name']) < 1:
            flash("Name cannot be empty!")
        else:
            flash("Success! Your name is {}".format(request.form['name']))

        if len(request.form['comment']) < 1:
            flash("Comment cannot be empty!")
        elif len(request.form['comment']) > 120:
            flash("Comment cannot exceed 120 characters. Thanks for being brief!")
        else:
            flash("Success! Your comment was received.")

        session['name'] = request.form['name']
        session['location'] = request.form['location']
        session['language'] = request.form['language']
        session['comment'] = request.form['comment']

        return redirect('/surveys/result')

    def result(self):
        return self.load_view('result.html')
