<h1 id="cf-edge-l4-delivery-rate">cf.edge.l4.delivery_rate</h1>

**Data type:** Integer

<p>The most recent data delivery rate estimate for the client connection, in bytes per second.</p>

<p>This metric reflects the rate at which data is being successfully delivered over the connection.</p>
<p>Returns <code>0</code> when L4 statistics are not available for the request.</p>

**Example value:**

```txt
123456
```

**Example usage:**

```txt
# Match requests where the delivery rate is below 100 KB/s
cf.edge.l4.delivery_rate < 100000
```

<h2 id="categories">Categories</h2>

- Request

**Keywords:** request, l4, delivery rate, bandwidth, network, performance, transport

