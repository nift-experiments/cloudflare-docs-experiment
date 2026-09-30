<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 4, 2025</time><h2 id="post-title">Gain visibility into user actions in Zero Trust Browser Isolation sessions</h2>
<div class="changelog-badges"><span>browser-isolation</span></div><div class="changelog-body"><p>We're excited to announce that new logging capabilities for <a href="/cloudflare-one/remote-browser-isolation/">Remote Browser Isolation (RBI)</a> through <a href="/logs/logpush/logpush-job/datasets/account/">Logpush</a> are available in Beta starting today!</p>
<p>With these enhanced logs, administrators can gain visibility into end user behavior in the remote browser and track blocked data extraction attempts, along with the websites that triggered them, in an isolated session.</p>
<pre><code class="language-json">{&#10;	&quot;AccountID&quot;: &quot;$ACCOUNT_ID&quot;,&#10;	&quot;Decision&quot;: &quot;block&quot;,&#10;	&quot;DomainName&quot;: &quot;www.example.com&quot;,&#10;	&quot;Timestamp&quot;: &quot;2025-02-27T23:15:06Z&quot;,&#10;	&quot;Type&quot;: &quot;copy&quot;,&#10;	&quot;UserID&quot;: &quot;$USER_ID&quot;&#10;}&#10;</code></pre>
<p>User Actions available:</p>
<ul>
<li><strong>Copy &amp; Paste</strong></li>
<li><strong>Downloads &amp; Uploads</strong></li>
<li><strong>Printing</strong></li>
</ul>
<p>Learn more about how to get started with Logpush in our <a href="/logs/logpush/">documentation</a>.</p>
</div></article></div>
