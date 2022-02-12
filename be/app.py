from flask import Flask, request, jsonify
import os
from python_terraform import *

ENDPOINT = os.getenv("ENDPOINT")

variable = {"ENDPOINT": ENDPOINT}

tf = Terraform(working_dir="/app/terraform", variables=variable)
app = Flask(__name__)


@app.route("/")
def hello_world():
    tf.apply()

    return_code, stdout, stderr = tf.apply()
    app.logger.info(f"{return_code} {stdout} {stderr}")
    return jsonify({"name": "jun"})


@app.route("/test")
def test():
    cwd = os.getcwd()  # Get the current working directory (cwd)
    files = os.listdir(cwd)  # Get all the files in that directory
    res = f"Files in {cwd}: {files}"

    return jsonify({"name": res})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
