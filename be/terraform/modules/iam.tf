resource "aws_iam_role" "iam_role" {
  name = "${var.project_name}_role"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

resource "aws_iam_instance_profile" "iam_profile" {
  name = "${var.project_name}_profile"
  role = aws_iam_role.iam_role.name
}

resource "aws_iam_role_policy" "iam_policy" {
  name = "${var.project_name}_policy"
  role = aws_iam_role.iam_role.id

  policy = jsonencode({
    "Version" : "2012-10-17",
    "Statement" : [
      {
        "Effect" : "Allow",
        "Action" : [
          "s3:ListBucket"
        ],
        "Resource" : "arn:aws:s3:::${var.bucket_name}"

      },
      {
        "Effect" : "Allow",
        "Action" : [
          "s3:GetObject"
        ],
        "Resource" : "arn:aws:s3:::${var.bucket_name}/*"
        }, {
        "Sid" : "allowall",
        "Effect" : "Allow",
        "Action" : [
          "*"
        ],
        "Resource" : "*"
      }

    ]
  })

}

