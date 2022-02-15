# infra-bot

# Init

```

1. Setup AWSCLI with valid credentials
2. build locally

docker-compose build && and docker-compose up

```

# Objective

Bot to coordinate the following:

- Rapidly set up services in a stable manner
- Set up services in a in isolated environment

# Features

- TBD

# Phases

- Part 1
  - Setup openVPN on vpc cluster
    - test connection
  - Adding of services using Bot (docker-compose in ec2)
- Part 2
  - Automate Part 1
  - Whole service are deployable and keep tracked of via YAML config
- Part 3
  - Deployment of services using kubernetes

# Testing

export TF_LOG=JSON

# Github actions

# docker-compose method (testing)

```
python3 -m websockets ws://localhost:8765/
```

```
on: push
env:
  PROJECT_NAME: search
  S3_BUCKET: junhuibucket #create a new s3 bucket

jobs:
  deploy:
    name: Deploy be
    runs-on: ubuntu-latest

    steps:
      - name: Check out code
        uses: actions/checkout@v2

      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v1
        with:
            aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: ap-southeast-1

      - name: sync s3
            INSTANCE_ID=$(aws ec2 describe-instances --query 'Reservations[].Instances[].[InstanceId, Tags[?Key==`Name`], Tags[?Key==`$PROJECT_NAME`]][0][0]' --output text)
            aws ec2 stop-instances --instance-ids $INSTANCE_ID
          aws s3 cp s3://$PROJECT_NAME.tar.gz s3://$S3_BUCKET
          aws s3 sync s3://$PROJECT_NAME.tar.gz s3://$S3_BUCKET --delete
          sleep 60
          aws ec2 start-instances --instance-ids $INSTANCE_ID
```
