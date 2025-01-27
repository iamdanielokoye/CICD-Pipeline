# Secure CI/CD Pipeline with GitHub Actions

This project demonstrates a secure CI/CD pipeline using GitHub Actions. The pipeline performs the following steps:

1. **Linting**: Checks code style using Flake8.
2. **Testing**: Runs unit tests with Pytest.
3. **Build**: Creates a Docker image for the application.
4. **Security Scans**: Scans the Docker image with Trivy and performs static code analysis with SonarQube.
5. **Deployment**: Deploys the application to a Kubernetes cluster.

## Prerequisites
- Docker
- Kubernetes (Minikube or Kind recommended for local setup)
- GitHub Actions enabled in your repository
- Trivy installed for local scans
- SonarQube server (optional for local analysis)

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/secure-cicd-pipeline.git
   ```

2. Navigate to the `app/` directory and build the Docker image:
   ```bash
   docker build -t app:latest .
   ```

3. Deploy the application to Kubernetes:
   ```bash
   kubectl apply -f kubernetes/
   ```

4. Access the application via the NodePort or Ingress URL.

## Future Enhancements
- Add monitoring with Prometheus and Grafana.
- Enhance security scans with Checkov.
- Include deployment to a cloud provider like AWS or GCP.

## License
This project is licensed under the MIT License.
```