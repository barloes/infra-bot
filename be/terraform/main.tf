terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}

provider "aws" {
  profile = "default"
  region  = "ap-southeast-1"
}

# module "testec2" {
#   source = "./modules"

#   //manage ec2 num at modules/simpleec2/ec2.tf
#   project_name      = "test"
#   instance_type     = "t4g.small"
#   ami_id            = "ami-03d20fc12884694ee"
#   key_name          = "cicd"
#   vpc_cidr          = "10.0.0.0/16"
#   availability_zone = "ap-southeast-1a"
#   bucket_name       = "junhuibucket"
# }
