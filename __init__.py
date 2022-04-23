from flask import Flask, render_template, request
from get_data import get_data
from make_graph import make_graph
import file_handle as fh

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    s_fname, l_fname = fh.get_filepaths()
    if request.method == 'POST':
        data = get_data(request)
        make_graph(filename=s_fname, **data)
        data.update({
            'figure': l_fname})
        return render_template('input_page.html', **data)
    else:
        return render_template('input_page.html')



