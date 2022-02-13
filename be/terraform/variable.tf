variable "project_list" {
  type = list(object({
    _id  = string
    data = string
  }))
}
