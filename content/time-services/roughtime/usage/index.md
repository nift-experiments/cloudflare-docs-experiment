<p>The &quot;Hello, world!&quot; of Roughtime is very simple: the client sends a request over UDP to the server and the server responds with a signed timestamp.</p>
<p>You just need the server's address and public key to run the protocol:</p>
<ul>
<li><strong>Server address</strong>: <code>roughtime.cloudflare.com:2003</code> (resolves to an IP address in our <a href="https://www.cloudflare.com/learning/cdn/glossary/anycast-network/">anycast IP range</a>). You can use either IPv4 or IPv6.</li>
<li><strong>Public key</strong>: <code>0GD7c3yP8xEc4Zl2zeuN2SlLvDVVocjsPSL8/Rl/7zg=</code></li>
</ul>
<p>To get started, download and run Cloudflare's <a href="https://github.com/cloudflare/roughtime">Go client</a>:</p>
<pre><code class="language-go">go install github.com/cloudflare/roughtime/cmd/getroughtime@latest&#10;getroughtime -ping roughtime.cloudflare.com:2003 -pubkey 0GD7c3yP8xEc4Zl2zeuN2SlLvDVVocjsPSL8/Rl/7zg=&#10;</code></pre>
<h2 id="beta-notice">Beta notice</h2>
<p>Cloudflare Roughtime is currently in beta. As such, our root public key may
change in the future. We will keep this page up-to-date with the most current public key.</p>
<p>You can also obtain it programmatically using DNS. For example:</p>
<pre><code class="language-sh">dig TXT roughtime.cloudflare.com | grep -oP &#x27;TXT\s&quot;\K.*?(?=&quot;)&#x27;&#10;</code></pre>
<h2 id="next-steps">Next steps</h2>
<p>Beyond just getting the Roughtime from Cloudflare, you may want to use it to <a href="/time-services/roughtime/recipes/">keep your clock in sync</a>.</p>
