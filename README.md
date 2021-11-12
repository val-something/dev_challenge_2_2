This is a README file to help structure projects. Sections marked with **Sample** should be replaced. Feel free to add/remove sections as needed.

# Project Title
**Developer Challenge 2_2, 2021**
This project is a response to Developer Challenge 2_2, used to assess backend developers. It is a web application using [Python 3.7.12](https://www.python.org/downloads/release/python-3712/) that uses [Flask](https://flask.palletsprojects.com/en/2.0.x/) for a web server to handle calls made to specific endpoints.

## Design
### Application Architecture
<Add a discussion on designing the application here>

<Include a UML diagram if needed>

### Application Assumptions
<List all assumptions here>

## Getting Started
These instructions will get a copy of the project up and running on a local machine. These instructions were written for WSL running Ubuntu 18.04 LTS.

### Prerequisites
1. Python 3.7.12 (https://www.python.org/downloads/release/python-3712)
2. Flask 2.0.2 (https://flask.palletsprojects.com/en/2.0.x/)

Optional
- pyenv (https://github.com/pyenv/pyenv)
- Postman (https://www.postman.com/)

### Installing
These instructions will outline the components used in the project.

A basic copy of the project can be cloned via ssh using:
`git clone ssh://innersource.accenture.com/not_val/dev_challenge_2_2`

#### Python
Python is an interpreted programming language used to integrate all the components. A virtual environment (implemented via [pyenv](https://github.com/pyenv/pyenv)) is used to force Python 3.7.

The following commands will get a virtual environment set up.
Note: these instructions have been compiled from multiple sources.

1. Install pyenv dependencies:
```
apt install git gcc make openssl libssl-dev libbz2-dev libreadline-dev libsqlite3-dev zlib1g-dev libncursesw5-dev libgdbm-dev libc6-dev zlib1g-dev libsqlite3-dev tk-dev libssl-dev openssl libffi-dev
```
2. Download and install pyenv:
```
curl https://pyenv.run | bash
```
3. Append the following lines to `~/.bashrc` to enable pyenv to shim (intercept and translate) Python, making sure to enter the correct username:
```
export PATH="/home/<<username>>/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```
4. Source `~/.bashrc` to save these changes:
```
source ~/.bashrc
```
5. Install the required version of Python via pyenv:
```
pyenv install 3.7.12
```
6. Navigate to the project directory and create a virtual environment using Python 3.7.12:
```
cd dev_challenge_2_2/; pyenv virtualenv 3.7.12 dev_challenge_2_2_env
```
7. Activate the shimming to make sure Python 3.7.12 is used whenever the Python command is called:
```
pyenv local dev_challenge_2_2_env
```
*Great! Now whenever scripts are run inside the dev_challenge_2_2/ directory, Python 3.7.12 will automatically be used.*

#### Flask
Flask is a web application microframework in Python used to host and expose REST API endpoints.

The following commands will install the Flask component and copy sample data.

1. Install Flask locally (make sure this is being run inside the `dev_challenge_2_2/` directory to ensure it's installing to the correct Python version):
```
pip install flask pytest
```
2. Copy `warframe_reviews.json` to `dev_challenge_2_2/`.

*Cool! Flask has been installed and configured - the rest of the cloned project should be accessible now!*

## Deployment
### Flask Server
1. Start the Flask server using `./flask-start.sh`.
2. Using a browser, navigate to `localhost:5000`.
3. Validate.

- Live test instances: none
- Test data: none

## Testing
### Flask Server
<Include instructions on running unit tests here>

Test cases enumerated:
<Add numbered test cases here>

## Contributing
Send me an [email](mailto:val.adrien.li@accenture.com)

### Limitations/Future work
<Add in missed items & improvements here>

## Troubleshooting
- Awaiting feedback

## Authors
- **Val** - [val.adrien.li](mailto:val.adrien.li@accenture.com)

## License
This project is unlicensed.

## Acknowledgments
<Include any people & resources here>