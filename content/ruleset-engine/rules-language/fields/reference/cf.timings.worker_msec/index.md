<h1 id="cf-timings-worker-msec">cf.timings.worker_msec</h1>

**Data type:** Integer

<p>The time spent executing a Cloudflare Worker in milliseconds.</p>

<p>This field provides the wall-clock time that a Cloudflare Worker spent handling the request, measured in milliseconds.</p>
<p>Use this field to identify slow Worker executions, set up alerts for performance regressions, or add Worker execution time as a request header using Transform Rules for downstream observability.</p>
<p>If the request did not invoke a Worker, the value of this field will be <code>0</code>.</p>

**Example value:**

```txt
12
```

**Example usage:**

```txt
# Matches requests where the Worker execution time exceeded 500 milliseconds
cf.timings.worker_msec > 500
```

<h2 id="categories">Categories</h2>

- Request

**Keywords:** request, timing, workers, performance, latency

