<p>Adaptive routing controls features that modify the routing of requests to pools and endpoints in response to dynamic conditions, such as during the interval between active health monitoring requests.
Zero-downtime failover will trigger a single retry only if there is another healthy endpoint in the pool and a <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-521/">521, 522, 523, 525 or 526 error code</a> is occurring. No other error codes will trigger a zero-downtime failover operation.</p>
<h2 id="failover-across-pools">Failover across pools</h2>
<p>When there are no healthy endpoints in the same pool, failover across pools extend the zero-downtime failover of requests to healthy endpoints in alternate pools according to the failover order defined by traffic and endpoint steering.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="geo-steering-limitation">Geo-steering limitation</h3>
@markup("md", "content/.markup/bodies/10328.md")
</aside>
<h3 id="enable-failover-across-pools">Enable failover across pools</h3>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Load Balancing</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Navigate to your Load Balancers and select <strong>Edit</strong>.</li>
<li>From <strong>Adaptive Routing</strong>, enable <strong>Failover across pools</strong>.</li>
</ol>
<h2 id="http-2-goaway-handling">HTTP/2 GOAWAY handling</h2>
<p>When an origin sends a GOAWAY frame, Cloudflare stops sending new requests on that connection but does not mark the endpoint as unhealthy. Safe-to-retry requests (typically GET) are automatically retried on a new connection. Non-idempotent requests (such as POST or PUT) may not be retried unless the request was not yet sent on the closing connection.</p>
