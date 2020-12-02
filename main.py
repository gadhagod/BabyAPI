from flask import Flask, request

app = Flask(__name__)

def to_baby(in_string):
    return(in_string.lower()
        .replace('sh', 's')
        .replace('r', 'w')
        .replace('l', 'w')
        .replace('ing', 'in')
        .replace('th', 'd')
        .replace(' de ', ' da ')
    )

@app.route('/v1')
def main():
    return({'translated': to_baby(request.args.to_dict()['text'])})