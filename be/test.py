from python_terraform import *

tf = Terraform(working_dir="./terraform")
return_code, stdout, stderr = tf.apply()

print(f"{return_code} {stdout} {stderr}")
