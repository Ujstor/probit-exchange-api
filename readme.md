# **ProBit Global exchange API**

1. Clone git repo

2. Create and add credentials in `.env` file
    ```
    ID=             #probit API id
    SECRET=         #probit API secret
    KEY=            #random string
    ```
3. Run `python main.py`

4. Open `127.0.0.1:5000` in local browser

# Docker

To build the Docker image from the code, run:

```
docker compose -f .\docker-compose-dev.yml up
```

If you want to pull the image from the Docker repository instead, use:

```
docker compose -f .\docker-compose-prod.yml up
```

Image is automatically built and deployed through the Jenkins pipeline after changes in GitHub, and it expects a .env file for loading variables.

<br/>

![](https://i.imgur.com/e4OqvK9.png)

# Jenkins Pipeline


Pipeline is designed to automate the building and deployment of a Docker image for the Probit Exchange API. It is configured to execute different stages of the CI/CD process based on the branch being built. It assumes you have a specific versioning strategy for your application, denoted by "Patch," "Minor," and "Major."


## Pipeline Execution Flow

The pipeline is executed as follows:

1. Code is checked out from the GitHub repository.
2. The environment is prepared by copying the `.env` file.
3. Tests are run.
4. If the branch is 'master', a Docker image tag is generated.
5. If the branch is 'master', a Docker image is built with the generated tag.
6. If the branch is 'master', the Docker image is pushed to Docker Hub.
7. If the branch is 'master', the Docker image is removed.

## Execution Conditions

The stages for image tagging, building, deploying, and environment cleanup are conditional and will only run when the branch being built is 'master'.

Please ensure that you have the necessary plugins and tools set up in your Jenkins environment to support Docker and the required scripts for testing. Scripts are in [IaC Repo](https://github.com/Ujstor/k8s-infra/tree/master/jenkins/scripts)




<br/>


## Expected output

Probit is primarily used for fat finger orders. In the event of market volatility and lack of liquidity, these extreme orders can be executed.

The tool is now used for order monitoring.

![expected output](https://i.imgur.com/VEfFNs9.png)

![expected output](https://i.imgur.com/W1ox8l7.png)


## Pytest
To run tests, use `pytest -v -s` command.

![](https://i.imgur.com/4Jr7WS3.png)