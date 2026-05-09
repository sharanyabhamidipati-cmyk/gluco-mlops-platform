# Gluco MLOps Platform

## Project Overview

Gluco MLOps Platform is an end-to-end cloud-native MLOps project built using FastAPI, Docker, Kubernetes, GitHub Actions, Prometheus, and Grafana.

The platform exposes a machine learning inference API for glucose risk prediction, containerizes the application using Docker, deploys it on Kubernetes, automates CI validation using GitHub Actions, and integrates observability using Prometheus and Grafana.

This project demonstrates production-style DevOps, Platform Engineering, SRE, and MLOps concepts including monitoring, metrics instrumentation, Kubernetes deployment, and CI automation.

---

# Features

- FastAPI-based ML inference API
- Docker containerization
- Kubernetes deployment using Minikube
- GitHub Actions CI pipeline
- Prometheus metrics integration
- Grafana monitoring dashboards
- Health check endpoint
- Request throughput monitoring
- Request latency monitoring
- ML prediction metrics tracking
- Kubernetes ServiceMonitor integration
- Helm-based monitoring stack deployment

---

# Architecture

```text
                    +----------------------+
                    |      GitHub Repo     |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | GitHub Actions CI/CD |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    |   Docker Container   |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | Kubernetes Deployment|
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    |  FastAPI ML Service  |
                    +----------+-----------+
                               |
             +----------------+----------------+
             |                                 |
             v                                 v
+------------------------+      +---------------------------+
| Prometheus Monitoring  | ---> | Grafana Dashboards        |
+------------------------+      +---------------------------+
