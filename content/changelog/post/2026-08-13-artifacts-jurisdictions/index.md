<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 13, 2026</time><h2 id="post-title">Data localization support for Artifacts</h2>
<div class="changelog-badges"><span>artifacts</span></div><div class="changelog-body"><p>Artifacts now supports jurisdictions, allowing you to select the European Union or the United States as the only location where repo data is stored and processed.</p>
<p>Select a jurisdiction when you create a namespace. Every repo in that namespace automatically uses the selected jurisdiction.</p>
<pre><code class="language-bash">curl --request POST \&#10;  &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/artifacts/namespaces&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;namespace&quot;: &quot;my-eu-namespace&quot;,&#10;    &quot;jurisdiction&quot;: &quot;eu&quot;&#10;  }&#x27;&#10;</code></pre>
<p>Jurisdictions cannot be changed after namespace creation. If you omit the jurisdiction, Artifacts creates an unrestricted namespace.</p>
<p>For supported jurisdictions and usage details, refer to <a href="/artifacts/guides/data-localization/">Data localization</a>.</p>
</div></article></div>
