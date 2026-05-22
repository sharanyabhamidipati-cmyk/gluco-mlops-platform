**# Prometheus & Grafana Queries

## API Request Throughput

```promql
sum(rate(gluco_api_requests_total[1m]))
```

Measures API requests per second.

---

## Average API Latency

```promql
sum(rate(gluco_api_request_latency_seconds_sum[1m]))
/
sum(rate(gluco_api_request_latency_seconds_count[1m]))
```

Measures average API response latency.

---

## P95 Latency

```promql
histogram_quantile(
  0.95,
  sum(rate(gluco_api_request_latency_seconds_bucket[1m])) by (le)
)
```

Measures 95th percentile response latency.

---

## Prediction Request Rate

```promql
sum(rate(gluco_predictions_total[1m]))
```

Measures prediction throughput.

---

## Prometheus Target Health

```promql
up
```

Checks whether Prometheus targets are healthy.

---

## Kubernetes Running Pods

```promql
count(kube_pod_status_phase{phase="Running"})
```

Counts running Kubernetes pods.

---

## CPU Usage Per Pod

```promql
sum(rate(container_cpu_usage_seconds_total[1m])) by (pod)
```

Shows CPU usage per pod.

---

## Memory Usage Per Pod

```promql
sum(container_memory_usage_bytes) by (pod)
```

Shows memory usage per pod.**
