<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 30, 2026</time><h2 id="post-title">Shared dictionaries passthrough now in open beta</h2>
<div class="changelog-badges"><span>speed</span></div><div class="changelog-body"><p><a href="/speed/optimization/content/shared-dictionaries/">Shared dictionaries</a> (<a href="https://www.rfc-editor.org/rfc/rfc9842.html">RFC 9842</a>) let an origin compress a response against a previous version of the same resource that the browser already has cached, so only the difference between versions travels over the wire. Shared dictionaries passthrough is now in open beta on all plans.</p>
<h4 id="what-changed">What changed</h4>
<p>In passthrough mode, Cloudflare:</p>
<ul>
<li>Forwards the <code>Use-As-Dictionary</code> and <code>Available-Dictionary</code> headers between client and origin without modification.</li>
<li>Treats <code>dcb</code> (Dictionary-Compressed Brotli) and <code>dcz</code> (Dictionary-Compressed Zstandard) as valid <code>Content-Encoding</code> values end to end, without recompressing them.</li>
<li>Extends the cache key to vary on <code>Available-Dictionary</code> and <code>Accept-Encoding</code> so each delta-compressed variant is cached correctly.</li>
</ul>
<p>Your origin manages the dictionary lifecycle: deciding which assets are dictionaries, attaching <code>Use-As-Dictionary</code> headers, and producing deltas in response to <code>Available-Dictionary</code> requests. Cloudflare handles the transport and the cache.</p>
<p>In internal testing on a 272 KB JavaScript bundle, the asset shrinks from 92.1 KB with Gzip to 2.6 KB with delta Zstandard against the previous version — a 97% reduction over standard compression — with download times improving by 81–89% versus Gzip.</p>
<p>Shared dictionaries work with browsers that advertise <code>dcb</code> or <code>dcz</code> in <code>Accept-Encoding</code>. Today, this includes Chrome 130 or later and Edge 130 or later.</p>
<h4 id="get-started">Get started</h4>
<p>Turn on passthrough for your zone with a single API call:</p>
<pre><code class="language-bash">curl --request PATCH --url https://api.cloudflare.com/client/v4/zones/$ZONE_ID/settings/shared_dictionary_mode</code></pre>
<p>You can also turn it on under <strong>Speed</strong> &gt; <strong>Settings</strong> &gt; <strong>Content Optimization</strong> in the <a href="https://dash.cloudflare.com/?to=/:account/:zone/speed/optimization">Cloudflare dashboard</a>. For full origin setup instructions and a working test recipe, refer to <a href="/speed/optimization/content/shared-dictionaries/">Shared dictionaries</a>, or try the live demo at <a href="https://canicompress.com/">canicompress.com</a>.</p>
</div></article></div>
