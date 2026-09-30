<p>The IP validation method aims to identify all of the IP addresses that a bot may use to send requests. IP validation is only used as a verification method for <a href="/bots/concepts/bot/verified-bots/">verified bots</a>.</p>
<p>Cloudflare can achieve this in two ways:</p>
<ul>
<li><strong>Using IP list provided by the bot owner</strong>: The bot owner can host a public list of IP ranges (for example, <a href="https://developers.google.com/static/search/apis/ipranges/googlebot.json">Googlebot's list</a>). Cloudflare fetches and uses this list directly for validation.</li>
<li><strong>Using Domain-based reverse DNS</strong>: The bot owner can provide a domain (or set of domains) that their bot requests originate from. Cloudflare collects the IP addresses observed in the requests with the bot's user agent, and performs reverse DNS lookups. If the reverse DNS of an IP resolves to one of the provided domains, Cloudflare considers it valid and stores it.</li>
</ul>
<h2 id="public-ip-list">Public IP List</h2>
<p>To verify a bot using a public IP list, you need to provide:</p>
<ul>
<li>A fixed and limited set of IP addresses, which can be verified via publicly accessible plain-text, <code>JSON</code>, or <code>CSV</code>.</li>
<li>IP addresses used solely by the bot owner.</li>
<li>A user-agent match pattern.</li>
</ul>
<h2 id="reverse-dns">Reverse DNS</h2>
<p>To verify a bot using reverse DNS, you need to provide:</p>
<ul>
<li>A list of domain suffixes to validate DNS records.</li>
<li>IP addresses should have PTR records set correctly.</li>
<li>A user-agent match pattern.</li>
</ul>
<h2 id="generic-user-agents">Generic user-agents</h2>
<p>User-agent patterns that match generic user-agents will be rejected by the Verified Bots API. When you add a user-agent pattern that is considered very common to the Verified Bot form, you may encounter an error message that will prompt you to correct the user-agent before you can submit again.</p>
<p>Generic user-agents include:</p>
<ul>
<li><code>Dart</code></li>
<li><code>Go-http-client</code></li>
<li><code>GuzzleHttp</code></li>
<li><code>Google Chrome</code></li>
<li><code>Mozilla Firefox</code></li>
<li><code>Safari</code></li>
<li><code>Nessus</code></li>
<li><code>Websocket++</code></li>
<li><code>cloudflare-go</code></li>
<li><code>fasthttp</code></li>
<li><code>got</code></li>
<li><code>nginx-ssl early hints</code></li>
<li><code>node</code></li>
<li><code>node-fetch</code></li>
<li><code>okhttp</code></li>
<li><code>python-requests</code></li>
<li><code>uTorrent</code></li>
</ul>
