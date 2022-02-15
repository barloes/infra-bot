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

locals {
  name          = "junhui-infra-bot"
  key_name      = "cicd"
  ami_id        = "ami-03d20fc12884694ee"
  instance_type = "t4g.nano"
  ecr_name      = "junhuiimage"
  az            = "ap-southeast-1a"
}

module "s3" {
  source      = "./modules/s3"
  bucket_name = local.name
}

module "ecr" {
  source   = "./modules/ecr"
  ecr_name = local.name
}

module "vpc" {
  source   = "./modules/vpc"
  vpc_cidr = "10.0.0.0/16"
  name     = "infra-bot"
}

module "ec2" {
  source   = "./modules/ec2"
  for_each = { for x in var.project_list : x._id => x }

  project_name = each.value._id

  vpc_id        = module.vpc.vpc_id
  subnet_id     = module.vpc.subnet_id[local.az].id
  ami_id        = local.ami_id
  key_name      = local.key_name
  bucket_name   = local.name
  instance_type = local.instance_type
}
