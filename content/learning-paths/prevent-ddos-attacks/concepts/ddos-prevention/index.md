<p>Since DDoS attacks target your web servers, the way to prevent them is to reduce requests reaching those servers.</p>
<pre><code class="language-mermaid">flowchart TD;&#10;    A[Malicious device]--&gt;|Request to application|CDN;&#10;    CDN --&gt;|Sends remaining requests|Origin;&#10;    subgraph CDN&#10;        WAF&#10;        Cache&#10;    end&#10;    A --Prevent external connections---x Origin&#10;</code></pre>
<br />
<p>Requests can come to your origin server in two ways, from your web application and from direct connections to the server itself.</p>
<hr />
<h2 id="reduce-application-requests-to-the-origin">Reduce application requests to the origin</h2>
<h3 id="caching">Caching</h3>
<p>A cache stores copies of frequently accessed resources (images, CSS files).</p>
<p>When a resource is cached - either on a user's browser or Content Delivery Network (CDN) server - requests for that resource do not have to go to your origin server. Instead, these resources are served directly by the cache.</p>
<pre><code class="language-mermaid">flowchart TD;&#10;    User--&gt;|Sends Request|Cloudflare;&#10;    Cloudflare--&gt;B&gt;Has cached content?];&#10;    B--&gt;|Yes - Requested content|User;&#10;    B--&gt;|No|Origin;&#10;    Origin--&gt;|Requested content|User;&#10;</code></pre>
<br />
<p>In the context of DDoS attacks, caching reduces the number of requests going to your origin server, which makes it harder for your server to get overwhelmed by traffic.</p>
<h3 id="web-application-firewall-waf">Web Application Firewall (WAF)</h3>
<p>A Web Application Firewall (WAF) creates a shield between a web app and the Internet. This shield checks incoming web requests and filters undesired traffic to help mitigate many common attacks.</p>
<pre><code class="language-mermaid">flowchart TD;&#10;    User--&gt;|Sends Request|WAF;&#10;    WAF--&gt;|Filters Request|Application;&#10;    Application--&gt;|Sends Request|OriginServer;&#10;    OriginServer--&gt;|Serves Content|Application;&#10;    Application--&gt;|Serves Content|User;&#10;</code></pre>
<h2 id="prevent-external-connections">Prevent external connections</h2>
<p>Generally, your origin server should only accept requests coming from your web application.</p>
<p>This is a general best practice for security, but especially important in the context of DDoS attacks. Any traffic that bypasses your web application will also bypass any WAF or caching and has a stronger chance of overwhelming your origin.</p>
<pre><code class="language-mermaid">sequenceDiagram&#10;  participant Client&#10;  participant DDoS_Protection_Service&#10;  participant Origin_Server&#10;&#10;  Client-&gt;&gt;+DDoS_Protection_Service: Request&#10;  Note right of DDoS_Protection_Service: Filtered traffic&#10;  DDoS_Protection_Service-&gt;&gt;+Origin_Server: Request&#10;  Origin_Server--&gt;&gt;-DDoS_Protection_Service: Response&#10;  DDoS_Protection_Service--&gt;&gt;Client: Response&#10;&#10;  Client-&gt;&gt;+Origin_Server: Direct connection&#10;  Note over Origin_Server: Potential DDoS Attack&#10;  Origin_Server--&gt;&gt;-Client: Error response&#10;</code></pre>
