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

## Docker

Build and start the Docker containers using Docker Compose:

```bash
docker compose up
```

Application deployment can be achieved using docker-compose and hosting on the cloud self-hosting service provided by [Collify]().
<br>
<br>


Probit is primarily used for fat finger orders. In the event of market volatility and lack of liquidity, these extreme orders can be executed.

The tool is now used for order monitoring.

## Expected output
![expected output](https://i.imgur.com/VEfFNs9.png)

![expected output](https://i.imgur.com/W1ox8l7.png)


