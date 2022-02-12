data "http" "example" {
  url = var.ENDPOINT #"http://localhost:5000/"

  # Optional request headers
  request_headers = {
    Accept = "application/json"
  }
}
