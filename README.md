# toposoid-common-image-recognition-web
This is a WEB API that works as a microservice within the Toposoid project.
Toposoid is a knowledge base construction platform.(see [Toposoid　Root Project](https://github.com/toposoid/toposoid.git))
This microservice is responsible for vectorizing data for image recognition. outputs the result in JSON.

[![Test And Build](https://github.com/toposoid/toposoid-common-image-recognition-web/actions/workflows/action.yml/badge.svg)](https://github.com/toposoid/toposoid-common-image-recognition-web/actions/workflows/action.yml)

<img width="1158" src="https://github.com/toposoid/toposoid-common-image-recognition-web/assets/82787843/2a7d1dd1-7ce9-4832-bb67-f171164b5c6a">


## Dependency in toposoid Project

## Requirements
* Docker version 20.10.x, or later
* docker-compose version 1.22.x

## Recommended Environment For Standalone
* Required: at least 5.65G of HDD(Docker Image Size)

## Setup For Standalone
```bssh
docker-compose up
```

The first startup takes a long time until docker pull finishes.
## Usage
```bash
curl -X POST -H "Content-Type: application/json" -d '{"url": "http://images.cocodataset.org/val2017/000000039769.jpg"}' http://localhost:9013/getFeatureVector
```
* ref. http://localhost:9013/docs

## Note
* This microservice uses 9013 as the default port.

## License
toposoid/toposoid-common-image-recognition-web is Open Source software released under the [Apache 2.0 license](https://www.apache.org/licenses/LICENSE-2.0.html).

## Author
* Makoto Kubodera([Linked Ideal LLC.](https://linked-ideal.com/))

Thank you!
