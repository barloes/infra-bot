# output "http_res" {
#   value = jsondecode(data.http.example.body).name
# }

output "project_list" {
  value = var.project_list
}
