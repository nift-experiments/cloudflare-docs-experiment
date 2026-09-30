<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 27, 2026</time><h2 id="post-title">Post-Quantum Encryption and Key Transparency on Cloudflare Radar</h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> now tracks post-quantum encryption support on origin servers, provides a tool to test any host for post-quantum compatibility, and introduces a Key Transparency dashboard for monitoring end-to-end encrypted messaging audit logs.</p>
<h4 id="post-quantum-origin-support">Post-quantum origin support</h4>
<p>The new <a href="/api/resources/radar/subresources/post_quantum/"><code>Post-Quantum</code></a> API provides the following endpoints:</p>
<ul>
<li><a href="/api/resources/radar/subresources/post_quantum/subresources/tls/methods/support/"><code>/post_quantum/tls/support</code></a> - Tests whether a host supports post-quantum TLS key exchange.</li>
<li><a href="/api/resources/radar/subresources/post_quantum/methods/summary/"><code>/post_quantum/origin/summary/{dimension}</code></a> - Returns origin post-quantum data summarized by key agreement algorithm.</li>
<li><a href="/api/resources/radar/subresources/post_quantum/methods/timeseries_groups/"><code>/post_quantum/origin/timeseries_groups/{dimension}</code></a> - Returns origin post-quantum timeseries data grouped by key agreement algorithm.</li>
</ul>
<p>The new <a href="https://radar.cloudflare.com/post-quantum">Post-Quantum Encryption</a> page shows the share of customer origins supporting <a href="/ssl/post-quantum-cryptography/pqc-support/#x25519mlkem768">X25519MLKEM768</a>, derived from daily automated TLS scans of TLS 1.3-compatible origins. The scanner tests for algorithm support rather than the origin server's configured preference.</p>
<p><img src="/assets/upstream/images/radar/pq-origin-support.png" alt="Screenshot of the origin post-quantum support graph on Radar" /></p>
<p>A host test tool allows checking any publicly accessible website for post-quantum encryption compatibility. Enter a hostname and optional port to see whether the server negotiates a post-quantum key exchange algorithm.</p>
<p><img src="/assets/upstream/images/radar/pq-host-test.png" alt="Screenshot of the post-quantum host test tool on Radar" /></p>
<h4 id="key-transparency">Key Transparency</h4>
<p>A new <a href="https://radar.cloudflare.com/key-transparency">Key Transparency</a> section displays the audit status of Key Transparency logs for end-to-end encrypted messaging services. The page launches with two monitored logs: WhatsApp and Facebook Messenger Transport.</p>
<p>Each log card shows the current status, last signed epoch, last verified epoch, and the root hash of the Auditable Key Directory tree. The data is also available through the <a href="/key-transparency/api/">Key Transparency Auditor API</a>.</p>
<p><img src="/assets/upstream/images/radar/key-transparency-dashboard.png" alt="Screenshot of the Key Transparency dashboard on Radar" /></p>
<p>Learn more about these features in our <a href="https://blog.cloudflare.com/radar-origin-pq-key-transparency-aspa">blog post</a> and check out the <a href="https://radar.cloudflare.com/post-quantum">Post-Quantum Encryption</a> and <a href="https://radar.cloudflare.com/key-transparency">Key Transparency</a> pages to explore the data.</p>
</div></article></div>
