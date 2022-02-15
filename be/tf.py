from python_terraform import *
from pprint import pprint

tf = Terraform(working_dir="./terraform")
# return_code, stdout, stderr = tf.init()
# pprint(f"{return_code} {stdout} {stderr}")

var = [{"_id": "test", "data": "test"}, {"_id": "test", "data": "test"}]

return_code, stdout, stderr = tf.apply(
    var={
        "project_list": "b",
        "project_list": json.dumps(var),
    }
)
pprint(f"{return_code} {stdout} {stderr}")

# terraform apply -var='project_list=[{"_id": "test1", "data": "test1"}]' -auto-approve

# terraform apply -var='project_list=[{"_id": "test", "data": "test"}, {"_id": "test", "data": "test"}]' -auto-approve
