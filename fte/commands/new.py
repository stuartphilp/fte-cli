"""The new command, generates directories and templates for adding tests to a project."""

import os

from json import dumps
from .base import Base
from string import Template

JENKINSFILE = """
node {
    def PROJECT_NAME = {{project}}
    def GITHUB_PATH = {{github_url}}
    def ENV = {{env}}

    stage 'Git checkout'
    echo 'Checking out git repository'
    git url: 'https://github.com/${GITHUB_PATH}'

    stage 'Build project'
    echo 'Building ${PROJECT_NAME} for ${ENV}'
    buildProject(${PROJECT_NAME}', ${ENV})

    stage 'Run tests'
    echo 'Executing tests for ${PROJECT_NAME} on ${ENV}'
    runTests(${PROJECT_NAME}', ${ENV})

    stage 'Wait for approval'
    input 'Approve promotion?'
}

def buildProject(String project, String env){
    sh "/bin/build --env ${env}"
}

def runTests(String project, String env){
    sh "/bin/test --env ${env} "
}
"""

class New(Base):

    def run(self):

        if not os.path.exists("tests"):
          os.makedirs("tests")
        else:
          print "./tests directory already exists. Skipping."

        if not os.path.isfile("Jenkinsfile"):
          with open("Jenkinsfile", 'w') as output_file:
            output_file.write(JENKINSFILE)
        else:
          print "Jenkinsfile already exists. Skipping."


