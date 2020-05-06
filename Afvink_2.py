from flask import Flask, render_template, request
import protein

# constructor
app = Flask(__name__)


# URL
@app.route('/')
def nucleotide_to_protein():
    nucleotide = request.args.get("nucleotide", "")
    translate = protein.lexicon(nucleotide)
    page_title = "Nucleotide converter"
    return render_template("afvink2.html", nucleotide=nucleotide,
                           page_title=page_title, translate=translate)


if __name__ == '__main__':
    app.run()
