def get_filepaths():
    from random import choice
    import string

    file_folder_raw = 'https://www.pythonanywhere.com/user/mattjkenney/files/home/mattjkenney/'
    directory = 'mysite/templates/figures/'

    figname = ''
    for i in range(10):
        figname += choice(string.ascii_lowercase)
    figname += '.png'

    save_filename = directory + figname
    load_filename = file_folder_raw + save_filename

    return save_filename, load_filename