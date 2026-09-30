<h1 id="cf-timings-client-quic-rtt-msec">cf.timings.client_quic_rtt_msec</h1>

**Data type:** Integer

<p>The smoothed QUIC round-trip time (RTT) between Cloudflare and the client in milliseconds.</p>

<p>This field is only populated for QUIC (HTTP/3) connections. For TCP connections, the value is <code>0</code>.</p>

**Example value:**

```txt
42
```

**Example usage:**

```txt
# Match requests over QUIC where the RTT exceeds 200 ms
cf.timings.client_quic_rtt_msec > 200
```

<h2 id="categories">Categories</h2>

- Request

**Keywords:** request, timing, quic, rtt, performance, latency, http3

