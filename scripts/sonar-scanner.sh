#!/bin/bash
# Example SonarQube analysis script
sonar-scanner \
  -Dsonar.projectKey=flask-app \
  -Dsonar.sources=. \
  -Dsonar.host.url=http://localhost:9000 \
  -Dsonar.login=<your-token>