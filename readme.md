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

Iimage is automatically built and deployed through the Jenkins pipeline after changes in GitHub.

<br/>

![]()

## Expected output

Probit is primarily used for fat finger orders. In the event of market volatility and lack of liquidity, these extreme orders can be executed.

The tool is now used for order monitoring.

![expected output](https://i.imgur.com/VEfFNs9.png)

![expected output](https://i.imgur.com/W1ox8l7.png)


## Pytest
To run tests, use `pytest -v -s` command.

![](https://i.imgur.com/4Jr7WS3.png)