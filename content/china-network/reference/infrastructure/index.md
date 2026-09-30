<h2 id="china-data-centers">China data centers</h2>
<p>For up-to-date information, refer to the <a href="https://www.cloudflare.com/china-network/">Cloudflare China Network</a> page.</p>
<h3 id="network-ip-addresses">Network IP addresses</h3>
<p>Cloudflare publishes a list of IP addresses for JD Cloud data centers, used by Cloudflare when connecting to the origin networks of customers to retrieve assets. These addresses are not the same IP addresses returned to website visitors as part of DNS resolution.</p>
<p>You can obtain the list of JD Cloud data center IP addresses via Cloudflare API. Use the <a href="/api/resources/ips/methods/list/">Cloudflare/JD Cloud IP Details</a> operation with the <code>networks=jdcloud</code> query string parameter:</p>
<pre class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/ips \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;ipv4_cidrs&quot;: [&#10;			// (...)&#10;		],&#10;		&quot;ipv6_cidrs&quot;: [&#10;			// (...)&#10;		],&#10;		&quot;jdcloud_cidrs&quot;: [&#10;			// (...)&#10;		],&#10;		&quot;etag&quot;: &quot;&lt;ETAG&gt;&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<p>The <code>jdcloud_cidrs</code> array lists the IP addresses of JD Cloud data centers.</p>
<p>Cloudflare will add new IP addresses to this list 30 days in advance before connecting from those IP addresses to an origin server. If you are using the China Network on JD Cloud, you should update your firewalls to reflect any IP address changes at least once every 30 days.</p>
