# infra-bot

- Only docker-compose projects are supported as of 16-Feb-2022
- Infra-bot stores project info onto mongodb which is utilized to create the infrastrucutre using terraform.
- In short, it is an easier alternative to writing terraform script as the program will auto generate them for you.
- I hope to add support for kubernetes applicaiton in the near future

# Features

- [ ] Add security group (ingress)
- [ ] Add docker images to pull from ECR

# Init

```
1. Setup AWSCLI with valid credentials
2. Docker-compose build && and docker-compose up
3. Add project and apply it (will update)
4. Follow [Github Actions Examples](https://github.com/barloes/search/tree/main/.github/workflows) in adding github actions to your project
5. Done
```

# Objective

Bot to coordinate the following:

- Rapidly set up services in a stable manner
- Set up services in a in isolated environment

# websocket (testing)

```
python3 -m websockets ws://localhost:8765/
```
