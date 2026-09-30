<p>Use Dedicated CDN Egress IPs in combination with different Cloudflare products.</p>
<h2 id="access-and-cni">Access and CNI</h2>
<p>You can use Dedicated CDN Egress IPs combined with <a href="/network-interconnect/">Cloudflare Network Interconnect (CNI)</a> to secure your applications with <a href="/cloudflare-one/access-controls/policies/">Cloudflare Access</a> without installing software or customizing code on your server.</p>
<p>While Access allows you to enforce policies at the hostname level, other solutions are usually necessary to protect against origin IP bypass <sup><a href="#footnote-1">1</a></sup>. With Dedicated CDN Egress IPs, you only allow a small number of IPs (that are not publicly listed) through your network firewall and, with Cloudflare Network Interconnect, you can use a completely private path between Cloudflare and your application server, without exposure to the public Internet. For details and background, refer to the <a href="https://blog.cloudflare.com/access-aegis-cni">Cloudflare blog</a>.</p>
<p>Dedicated CDN Egress IPs are included within <a href="/network-interconnect/">BGP advertisement over CNI</a>.</p>
<h2 id="data-localization-suite">Data Localization Suite</h2>
<p><a href="/data-localization/">Data Localization Suite (DLS)</a> is an enterprise add-on that enables you to choose the location where Cloudflare encrypts, decrypts, and stores data.</p>
<p>To ensure egress will happen from DLS-specified locations, make sure you have Dedicated CDN Egress IPs provisioned in those locations. Refer to <a href="/smart-shield/configuration/dedicated-egress-ips/how-it-works/egress-ips/#ips-allocation">IPs allocation</a> for details.</p>
<h2 id="load-balancing">Load Balancing</h2>
<p><a href="/load-balancing/">Cloudflare Load Balancing</a> allows you to intelligently distribute traffic across your origins by issuing regular monitors (that assess origin health) and following the traffic steering policies you define.</p>
<p>By default, the Load Balancing monitors will use public Cloudflare IP addresses.</p>
<p>To avoid inconsistencies between what the Load Balancing monitors report and what you observe in service traffic with Dedicated CDN Egress IPs, make sure to turn on the <strong>Simulate Zone</strong> option in the <a href="/load-balancing/monitors/create-monitor/#create-a-monitor">monitor settings</a>.</p>
<h2 id="spectrum">Spectrum</h2>
<p><a href="/spectrum/">Spectrum</a> allows you to route email, file transfer, games, and more over TCP or UDP through Cloudflare. This means you can mask your origin and protect it from DDoS attacks.</p>
<p>While you can use <a href="/byoip/">BYOIP</a> or static IPs to control which IPs are used for ingress with Spectrum, Dedicated CDN Egress IPs allows you to have a more strict list of <a href="/smart-shield/configuration/dedicated-egress-ips/how-it-works/egress-ips/">egress IPs</a> as well.</p>
<p>Dedicated CDN Egress IPs with Spectrum supports both TCP and UDP application types. HTTP/HTTPS types are also supported, although through a different configuration.</p>
<p>If you are interested in any of these solutions, contact your account team.</p>
<h2 id="workers">Workers</h2>
<p><a href="/workers/">Workers</a> provides a serverless execution environment for you to create applications leveraging Cloudflare's global network.</p>
<p>Refer to the sections below for information on how Dedicated CDN Egress IPs pair up with Workers.</p>
<h3 id="fetch"><code>fetch</code></h3>
<p><a href="/workers/runtime-apis/fetch/"><code>fetch()</code> requests</a> that access services on your origin will use Dedicated CDN Egress IP addresses.</p>
<p>Workers subrequests — requests from one Worker to another — are expected to use different IPs. However, <a href="/workers/runtime-apis/fetch/"><code>fetch()</code> requests</a> to external origins made by a Worker invoked via a subrequest will use Dedicated CDN Egress IP addresses.</p>
<h3 id="connect"><code>connect</code></h3>
<p>For <a href="/workers/runtime-apis/tcp-sockets/"><code>connect()</code> requests</a> - which create outbound TCP connections from Workers - Dedicated CDN Egress IPs are <strong>not</strong> used.</p>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">When an attacker knows your origin server IP and uses it to directly interact with the target application.</li></ol></section>
