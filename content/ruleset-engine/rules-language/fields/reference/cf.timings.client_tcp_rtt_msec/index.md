<h1 id="cf-timings-client-tcp-rtt-msec">cf.timings.client_tcp_rtt_msec</h1>

**Data type:** Number

<p>The smoothed TCP round-trip time (RTT) between Cloudflare and the client in milliseconds.</p>

<p>This field is only populated for TCP (HTTP/1, HTTP/2) connections. For QUIC connections, the value is <code>0</code>.</p>

**Example value:**

```txt
20
```

**Example usage:**

```txt
# Match requests over TCP where the RTT exceeds 200 ms
cf.timings.client_quic_rtt_msec > 200
```

<h2 id="categories">Categories</h2>

- Request

**Keywords:** request, timing, tcp, rtt, performance, latency

