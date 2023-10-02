from flask import Flask, render_template, request
import pdfkit

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == 'POST':
        url = request.form['url']
        html = request.form['html']

        # Define Path of wkhtmltopdf.exe
        pathToWkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
        
        # Point pdfkit configuration to wkhtmltopdf.exe
        config = pdfkit.configuration(wkhtmltopdf=pathToWkhtmltopdf)

        # Convert HTML file to PDF File
        pdfkit.from_string(html, 'html.pdf', configuration=config)
        
        # Convert url to PDF File
        pdfkit.from_url(url, 'url.pdf', configuration=config)

    return render_template("index.html")