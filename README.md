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
curl -X POST -H "Content-Type: application/json" -H 'X_TOPOSOID_TRANSVERSAL_STATE: {"userId":"test-user", "username":"guest", "roleId":0, "csrfToken":""}' -d '{"url": "http://images.cocodataset.org/val2017/000000039769.jpg"}' http://localhost:9013/getFeatureVector
```
* ref. http://localhost:9013/docs

## Note
* This microservice uses 9013 as the default port.

## License
This program is offered under a commercial and under the AGPL license.
For commercial licensing, contact us at https://toposoid.com/contact.  For AGPL licensing, see below.

AGPL licensing:
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

## Author
* Makoto Kubodera([Linked Ideal LLC.](https://linked-ideal.com/))

Thank you!
