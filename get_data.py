def get_data(request):

    xs_raw = request.form.get('xs')
    xs_dl = request.form.get('x_delim')
    ys_raw = request.form.get('ys')
    ys_dl = request.form.get('y_delim')
    #making lists
    xs = xs_raw.split(xs_dl)
    xs = [float(i) for i in xs]
    ys = ys_raw.split(ys_dl)
    ys = [float(i) for i in ys]
    data = {
        'xs': xs,
        'ys': ys}

    return data