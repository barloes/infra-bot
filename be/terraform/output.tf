output "http_res" {
  value = jsondecode(data.http.example.body).name
}
