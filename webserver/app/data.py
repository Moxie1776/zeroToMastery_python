from flask import Blueprint, render_template

dp = Blueprint(
    'data',
    __name__,
    template_folder='templates',
    # url_prefix='/data'
  )


@dp.route('/', methods=['GET'])
def home():
  # return ('Hello World')
  return render_template('index.html')


@dp.route('/about', methods=['GET'])
def about():
  return render_template('about.html')


@dp.route('/works', methods=['GET'])
def works():
  return render_template('works.html')
