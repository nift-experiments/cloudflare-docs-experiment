<p>A distributed denial-of-service (DDoS) attack is where a large number of computers or devices, usually controlled by a single attacker, attempt to access a website or online service all at once. This flood of traffic can overwhelm the website's origin servers, causing the site to slow down or even crash.</p>
<pre><code class="language-mermaid">sequenceDiagram;&#10;    participant User;&#10;    participant Website;&#10;    participant Server;&#10;    participant Botnet;&#10;    User-&gt;&gt;Website: Requests to access site&#10;    Website-&gt;&gt;Origin Server: Processes user requests&#10;    Botnet-&gt;&gt;Origin Server: Sends a flood of traffic&#10;    Origin Server--&gt;&gt;Website: Slows down due to traffic overload&#10;    Origin Server--&gt;&gt;User: Unable to respond to user requests&#10;</code></pre>
<br/>
<h2 id="common-signs-of-an-attack">Common signs of an attack</h2>
<p>Common signs that you are under DDoS attack include:</p>
<ul>
<li>Your site is offline or slow to respond to requests.</li>
<li>Unexpected spikes appear in the graph of <strong>Requests Through Cloudflare</strong> or <strong>Bandwidth</strong> in your Cloudflare <strong>Analytics</strong> app.</li>
<li>Strange requests appear in your origin web server logs that do not match normal visitor behavior.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8755.md")
</aside>
