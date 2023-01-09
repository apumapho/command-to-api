import subprocess
from flask import Flask

app = Flask(__name__)
COMMAND = 'date'
DEFAULT_FORMAT = '+%Y-%m-%d'


def run_command(command = COMMAND, date_format = DEFAULT_FORMAT):
    if not date_format.startswith('+'):
        date_format = '+' + date_format
    # TODO: add error checking on following command to be sure it properly runs
    return subprocess.run([COMMAND, date_format], capture_output=True, text=True).stdout.strip()


@app.route('/run')
@app.route('/run/<date_format>')
def main(date_format = DEFAULT_FORMAT):
    date = run_command(date_format=date_format)
    return {'date': date}  # Flask automatically jsonifies a dict you return
