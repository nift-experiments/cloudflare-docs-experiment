<p>Cloudflare runs one of the largest global anycast networks in the world — a network architecture where traffic is automatically routed to the nearest available data center. All current data center locations are accessible on the <a href="https://www.cloudflare.com/network/">network map</a>.</p>
<p>Within Cloudflare data centers, and between the Cloudflare network and your origin server, traffic is encrypted during transit. You can select which <a href="/ssl/origin-configuration/ssl-modes/">encryption mode</a> (controlling how strictly Cloudflare validates your server's certificate) and which <a href="/ssl/edge-certificates/additional-options/cipher-suites/">cipher suites</a> (the specific encryption algorithms used for the connection) to use.</p>
<p>Additionally, all request and response processing within a Cloudflare data center occurs in memory — traffic content is handled by automated systems and is not written to disk, except for eligible content for caching or Cache Rules you have configured. Automated controls prevent Cloudflare personnel from accessing traffic content in the processing pipeline. All cache disks are encrypted at rest (meaning data is encrypted when stored on disk, in addition to being encrypted during transmission).</p>
<p><img src="/assets/upstream/images/data-localization/http-requests-flow.png" alt="HTTP requests flow" /></p>
<p>At a high level, when an end user's device connects to any Cloudflare data center, the request is processed in the following way:</p>
<ol>
<li>
<p>Certain types of requests that can be used for cyber attacks are immediately dropped based on the addressing information (layer 3 / network layer).</p>
</li>
<li>
<p>Next, the encrypted request is decrypted (TLS termination) and inspected by the Cloudflare security and performance products you have configured — for example, Configuration Rules, WAF Custom Rules, and Rate Limiting Rules — applied in the order defined by the <a href="https://blog.cloudflare.com/traffic-sequence-which-product-runs-first/">traffic sequence</a>. This process enables the detection and prevention of a variety of cyber attacks, including application-layer (layer 7) DDoS attacks, automated bot traffic, credential stuffing (attackers using stolen username/password combinations), and SQL injection (attackers inserting malicious database commands into web requests), among others.</p>
</li>
<li>
<p>The inspected request is then passed to the caching layer. If a cached copy of the requested content is available, it is served directly to the user. If not, the request is forwarded to your origin server. Traffic between the Cloudflare data center and your origin server is encrypted, unless you have configured a different encryption mode.</p>
</li>
<li>
<p>When the response arrives from your origin server, any static and eligible content is cached onto encrypted disks. The response then passes back through your configured security and performance products before being returned to the user.</p>
</li>
</ol>
<p>By default, Cloudflare performs TLS termination (decryption of HTTPS traffic) in every data center globally — wherever the end user connects to a website or application behind Cloudflare. Customers who need to restrict where decryption occurs can configure <a href="/data-localization/regional-services/">Regional Services</a> to specify which regions handle TLS termination and traffic processing.</p>
