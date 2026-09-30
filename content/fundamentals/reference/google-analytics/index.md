<p>Using Cloudflare does not affect Google Analytics (GA) tracking if it is added to the website <a href="https://support.google.com/analytics/answer/9304153#add-tag">in one of ways recommended by Google</a>.</p>
<h2 id="standard-ga-setup">Standard GA setup</h2>
<p>Cloudflare proxies traffic to your origin web server, but the GA JavaScript code never actually sends traffic to your server. Instead, it executes directly in a user's browser and does not interact with Cloudflare.</p>
<p>Cloudflare only affects analytics tools that read logs directly from your web server (like awstats).</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8794.md")
</aside>
<h2 id="zaraz">Zaraz</h2>
<p>As an alternative to the standard setup of Google Analytics with tag/snippet, Cloudflare offers a way to use Google Analytics with <a href="/zaraz/">Zaraz</a>. Zaraz is a solution that allows Google Analytics to collect data without its script loaded on the website. If GA is set up this way, then not all features may be available.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8793.md")
</aside>
