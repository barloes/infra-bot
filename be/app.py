from flask import Flask, request, jsonify
from pymongo import MongoClient
import subprocess
import json
import os


MONGODB_URL = os.getenv("MONGODB_URL")

mongo_client = MongoClient(f"{MONGODB_URL}")
db = mongo_client["db"]
collection = db["project"]

app = Flask(__name__)


def create_project(name):
    item = {
        "_id": name,
        "data": name,
    }
    res = collection.insert_one(item)
    app.logger.info(res)


def tf_apply(data):

    var = json.dumps(data)
    subprocess.call("terraform init", shell=True, cwd="./terraform")
    subprocess.call(
        f"terraform apply -var='project_list={var}' -auto-approve",
        shell=True,
        cwd="./terraform",
    )


@app.route("/tf")
def hello_world():

    project_list = list(collection.find({}))
    var = {"project_list": project_list}
    app.logger.info(f"{project_list}")

    tf_apply(project_list)

    return jsonify({"msg": str("done")})


@app.route("/add")
def add():
    project = request.args.get("project")
    if project:
        create_project(project)

    return jsonify({"msg": str("done")})


@app.route("/update")
def update():
    project = request.args.get("project")
    if project:
        create_project(project)

    return jsonify({"msg": str("done")})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
