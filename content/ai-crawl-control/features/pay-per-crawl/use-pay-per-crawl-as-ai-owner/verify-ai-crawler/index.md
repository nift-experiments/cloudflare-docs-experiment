<pre><code class="language-mermaid">graph LR&#10;A[Set up your&lt;br&gt;Cloudflare Account] --&gt; B[Verify your&lt;br&gt;AI crawler]:::highlight&#10;B --&gt; C[Discover&lt;br&gt;payable content]&#10;C --&gt; D[Connect to&lt;br&gt;Stripe]&#10;D --&gt; E[Crawl pages]&#10;classDef highlight fill:#F6821F,color:white&#10;</code></pre>
<p>Once you have connected your Stripe account, set up your AI crawler as a <a href="/bots/concepts/bot/verified-bots/">verified bot</a>.</p>
<h2 id="content-access-restriction">Content access restriction</h2>
<p>When an AI crawler tries to access content protected by pay per crawl, it receives a HTTP status code 402. This indicates payment is required. The HTTP header of the response includes the cost of the content.</p>
<p>For example, the response header may look like below:</p>
<pre><code>HTTP/2 402&#10;date: Fri, 06 Jun 2025 08:42:38 GMT&#10;content-type: text/plain; charset=utf-8&#10;crawler-price: USD 0.01&#10;server: cloudflare&#10;</code></pre>
<p>To access this content, you must verify your AI crawler.</p>
<h2 id="1-follow-web-bot-auth-protocol"><ol>
<li>Follow Web Bot Auth protocol</li>
</ol></h2>
<p>Ensure your AI crawler identifies itself with the required headers for Web Bot Auth.</p>
<p>Follow the steps found in <a href="/bots/reference/bot-verification/web-bot-auth/">Web Both Auth</a>.</p>
<h2 id="2-follow-verified-bot-policy"><ol start="2">
<li>Follow verified bot policy</li>
</ol></h2>
<p>Ensure your AI crawler follows Cloudflare's <a href="/bots/concepts/bot/verified-bots/">verified bots policy</a>.</p>
<h2 id="3-submit-verification-request"><ol start="3">
<li>Submit verification request</li>
</ol></h2>
<p>Submit a form to add your AI crawler to Cloudflare's list of verified bots.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/2769.md")
</div>
