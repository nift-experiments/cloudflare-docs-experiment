<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 2, 2025</time><h2 id="post-title">Removed unused meta fields from DNS records</h2>
<div class="changelog-badges"><span>dns</span></div><div class="changelog-body"><p>Cloudflare is removing five fields from the <code>meta</code> object of DNS records. These fields have been unused for more than a year and are no longer set on new records. This change may take up to four weeks to fully roll out.</p>
<p>The affected fields are:</p>
<ul>
<li>the <code>auto_added</code> boolean</li>
<li>the <code>managed_by_apps</code> boolean and corresponding <code>apps_install_id</code></li>
<li>the <code>managed_by_argo_tunnel</code> boolean and corresponding <code>argo_tunnel_id</code></li>
</ul>
<p>An example record returned from the API would now look like the following:</p>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;&lt;ID&gt;&quot;,&#10;		&quot;zone_id&quot;: &quot;&lt;ZONE_ID&gt;&quot;,&#10;		&quot;zone_name&quot;: &quot;example.com&quot;,&#10;		&quot;name&quot;: &quot;www.example.com&quot;,&#10;		&quot;type&quot;: &quot;A&quot;,&#10;		&quot;content&quot;: &quot;192.0.2.1&quot;,&#10;		&quot;proxiable&quot;: true,&#10;		&quot;proxied&quot;: false,&#10;		&quot;ttl&quot;: 1,&#10;		&quot;locked&quot;: false,&#10;		&quot;meta&quot;: {&#10;			&quot;auto_added&quot;: false,&#10;			&quot;managed_by_apps&quot;: false,&#10;			&quot;managed_by_argo_tunnel&quot;: false,&#10;			&quot;source&quot;: &quot;primary&quot;&#10;		},&#10;		&quot;comment&quot;: null,&#10;		&quot;tags&quot;: [],&#10;		&quot;created_on&quot;: &quot;2025-03-17T20:37:05.368097Z&quot;,&#10;		&quot;modified_on&quot;: &quot;2025-03-17T20:37:05.368097Z&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<p>For more guidance, refer to <a href="/dns/manage-dns-records/">Manage DNS records</a>.</p>
</div></article></div>
