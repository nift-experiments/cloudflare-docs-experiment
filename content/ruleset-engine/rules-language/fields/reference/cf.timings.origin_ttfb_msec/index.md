<h1 id="cf-timings-origin-ttfb-msec">cf.timings.origin_ttfb_msec</h1>

**Data type:** Integer

<p>The round-trip time (RTT) between the Cloudflare global network and the origin server in milliseconds.</p>

<p>This field provides insight into origin server latency. It represents the Time to First Byte (TTFB) from the perspective of the Cloudflare edge server.</p>
<p>This metric includes both the network RTT and the time the origin server spent handling the request.</p>
<p>If the request was served from the Cloudflare CDN cache and the origin server was not reached, the value of this field will be <code>0</code>.</p>

**Example value:**

```txt
150
```

**Example usage:**

```txt
# Matches requests where the origin response time (TTFB) was greater than 2 seconds:
cf.timings.origin_ttfb_msec > 2000
```

<h2 id="categories">Categories</h2>

- Request

**Keywords:** request, timing, ttfb, performance, origin, latency

