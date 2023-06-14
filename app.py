from flask import Flask, render_template
import platform

app = Flask(__name__)

@app.route('/')
def index():
    # Retrieve server details
    server_details = {
        'System': platform.system(),
        'Node Name': platform.node(),
        'Release': platform.release(),
        'Version': platform.version(),
        'Machine': platform.machine(),
        'Processor': platform.processor()
    }

    # Render the template with server details
    return render_template('index.html', server_details=server_details)

if __name__ == '__main__':
    app.run()
