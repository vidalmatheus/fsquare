# {{name}}

## {{description}}


# F-Square cycle development

1. Implement your features on localhost:3001 (API Mock)
2. Validate that with a stakeholder (go back one step if needed)
3. Use TDD to develop the back-end API for the feature
4. Check if everything is okay on the actual front-end on localhost:3000 (go back one step if needed)
5. Push your changes! \o/

# System Design

<p align="center">
  <img src="https://github.com/vidalmatheus/fsquare/blob/master/img/system_design.png?raw=true" />
</p>

# Pipe-and-Filter Pattern

<p align="center">
  <img src="https://github.com/vidalmatheus/fsquare/blob/master/img/filteronproject.png?raw=true" />
</p>

# Dev commands
By running the shell script `dev.sh`, you'll have the following commands to help your development:

- **devhelp**: Print the help commands

- **dkdev**: Runs a dockerized *postgresql*, *nginx* and *metabase*

- **dkdb**: Runs a dockerized *postgresql* database on port 5432

- **dknginx**: Runs a dockerized *nginx* on port 80 to 8000 (back), 3000 (front), 3001 (mocked front)

- **pytest**: Runs python tests

- **pycoverage**: Runs python tests with flake8 and coverage report

- **dkbuild**: Builds a docker image for this project

- **dkfulldev**: Runs a dockerized *postgresql*, *nginx*, *metabase* and the project image
