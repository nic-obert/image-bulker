from flask import Flask, render_template, request, send_from_directory

from bulker import bulk_file


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'


@app.route('/')
def index_page():
    """
    Render the index page.
    """
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_page():
    """
    Get the uploaded file and bulk it up.
    """

    file = request.files.get('upload-file')

    print(file)
    if not file:
        return render_template('error.html', error='No file uploaded.')
    
    final_size = request.form.get('final-size')
    if not final_size:
        return render_template('error.html', error='No final size specified.')

    filename, new_size = bulk_file(file, int(final_size), app.config['UPLOAD_FOLDER'])

    return send_from_directory('../uploads', filename, as_attachment=True)

