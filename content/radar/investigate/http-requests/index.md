<p>While in <a href="/radar/investigate/netflows/">NetFlows</a> we can inspect bytes and packets reaching Cloudflare's edge routers, in HTTP requests we are a layer above in the <a href="https://en.wikipedia.org/wiki/OSI_model">OSI model</a>. HTTP requests examines complete HTTP requests from end users that reach websites served by Cloudflare's <a href="https://www.cloudflare.com/en-gb/learning/cdn/what-is-a-cdn/">CDN</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11555.md")
</aside>
<p>Most of the charts in the <a href="https://radar.cloudflare.com/adoption-and-usage">Adoption and Usage</a> section on Radar come from this data source.</p>
<p>These endpoints can be broadly split into:</p>
<ul>
<li><code>timeseries</code>: A time series of a group of metrics. For example, when looking at IP version, displays an IPv4 time series and an IPv6 time series.</li>
<li><code>summary</code>: Displays a summary of a group of metrics over the specified time range. For example, IPv4 traffic percentage out of the total HTTP traffic during that time period.</li>
<li><code>top</code>: A list of the top locations or <a href="https://www.cloudflare.com/en-gb/learning/network-layer/what-is-an-autonomous-system/">Autonomous Systems</a> (ASes) ranked by adoption of a specific metric. For example, top locations by mobile device traffic (like which locations have a higher percentage of mobile traffic out of the total traffic for that location).</li>
</ul>
<h2 id="list-of-endpoints">List of endpoints</h2>
<h3 id="timeseries">Timeseries</h3>
<h4 id="example-hourly-breakdown-by-device-type">Example: hourly breakdown by device type</h4>
<p>In this example, we will request traffic by device type globally, with and without <a href="/radar/concepts/bot-classes/">bot traffic</a>. Parameters for the <code>human</code> series are <code>name=human&amp;botClass=LIKELY_HUMAN&amp;dateRange=1d</code>. For the <code>bot</code> series, the parameters are <code>name=bot&amp;botClass=LIKELY_AUTOMATED&amp;dateRange=1d</code>:</p>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/radar/http/timeseries/device_type?name=human&amp;botClass=LIKELY_HUMAN&amp;dateRange=1d&amp;name=bot&amp;botClass=LIKELY_AUTOMATED&amp;dateRange=1d&amp;format=json&amp;aggInterval=1h&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<p>Here is the abbreviated response:</p>
<pre><code class="language-json">{&#10;  &quot;success&quot;: true,&#10;  &quot;errors&quot;: [],&#10;  &quot;result&quot;: {&#10;    &quot;human&quot;: {&#10;      &quot;timestamps&quot;: [&quot;2022-11-03T13:00:00Z&quot;, &quot;2022-11-03T14:00:00Z&quot;, &quot;..&quot;],&#10;      &quot;mobile&quot;: [&quot;52.5532&quot;, &quot;52.146628&quot;, &quot;..&quot;],&#10;      &quot;desktop&quot;: [&quot;47.394791&quot;, &quot;47.800731&quot;, &quot;..&quot;],&#10;      &quot;other&quot;: [&quot;0.052009&quot;, &quot;0.052642&quot;, &quot;..&quot;]&#10;    },&#10;    &quot;bot&quot;: {&#10;      &quot;timestamps&quot;: [&quot;2022-11-03T13:00:00Z&quot;, &quot;2022-11-03T14:00:00Z&quot;, &quot;..&quot;],&#10;      &quot;desktop&quot;: [&quot;83.833892&quot;, &quot;84.017711&quot;, &quot;..&quot;],&#10;      &quot;mobile&quot;: [&quot;16.156748&quot;, &quot;15.969936&quot;, &quot;..&quot;],&#10;      &quot;other&quot;: [&quot;0.00936&quot;, &quot;0.012353&quot;, &quot;..&quot;]&#10;    },&#10;    &quot;meta&quot;: {&#10;      &quot;dateRange&quot;: {&#10;        &quot;startTime&quot;: &quot;2022-11-03T13:00:00Z&quot;,&#10;        &quot;endTime&quot;: &quot;2022-11-04T13:00:00Z&quot;&#10;      },&#10;      &quot;normalization&quot;: &quot;PERCENTAGE&quot;&#10;    }&#10;  }&#10;}&#10;</code></pre>
<p>Mobile devices tend to be considerably more present when examining human generated traffic versus bot generated traffic.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11554.md")
</aside>
<p>For more information refer to <a href="/api/resources/radar/subresources/http/subresources/timeseries_groups/methods/device_type/">Get device types time series</a>.</p>
<h3 id="summary">Summary</h3>
<h4 id="example-overall-breakdown-by-device-type-and-human-bot-traffic">Example: overall breakdown by device type and human/bot traffic</h4>
<p>We can also look at the same information asking for a summary of the device type breakdown over the entire period, instead of a per hour breakdown like in the example before.</p>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/radar/http/summary/device_type?name=human&amp;botClass=LIKELY_HUMAN&amp;dateRange=1d&amp;name=bot&amp;botClass=LIKELY_AUTOMATED&amp;dateRange=1d&amp;format=json&amp;aggInterval=1h&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<p>Here is the abbreviated response:</p>
<pre><code class="language-json">{&#10;  &quot;success&quot;: true,&#10;  &quot;errors&quot;: [],&#10;  &quot;result&quot;: {&#10;		&quot;human&quot;: {&#10;			&quot;mobile&quot;: &quot;54.967243&quot;,&#10;			&quot;desktop&quot;: &quot;44.974006&quot;,&#10;			&quot;other&quot;: &quot;0.058751&quot;&#10;		},&#10;		&quot;bot&quot;: {&#10;			&quot;desktop&quot;: &quot;83.275452&quot;,&#10;			&quot;mobile&quot;: &quot;16.707455&quot;,&#10;			&quot;other&quot;: &quot;0.017093&quot;&#10;		}&#10;  }&#10;}&#10;</code></pre>
<p>For more information refer to the <a href="/api/resources/radar/subresources/http/subresources/summary/methods/device_type/">API reference</a> for this endpoint.</p>
<h4 id="example-breakdown-by-ip-version-and-human-bot-traffic">Example: breakdown by IP version and human/bot traffic</h4>
<p>In the following example, we will examine global breakdown of traffic by IP version, with and without bots:</p>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/radar/http/summary/ip_version?name=human&amp;botClass=LIKELY_HUMAN&amp;dateRange=1d&amp;name=bot&amp;botClass=LIKELY_AUTOMATED&amp;dateRange=1d&amp;format=json&amp;aggInterval=1h&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<p>This returns the following:</p>
<pre><code class="language-json">{&#10;  &quot;success&quot;: true,&#10;  &quot;errors&quot;: [],&#10;  &quot;result&quot;: {&#10;		&quot;human&quot;: {&#10;			&quot;IPv4&quot;: &quot;76.213647&quot;,&#10;			&quot;IPv6&quot;: &quot;23.786353&quot;&#10;		},&#10;		&quot;bot&quot;: {&#10;			&quot;IPv4&quot;: &quot;91.492032&quot;,&#10;			&quot;IPv6&quot;: &quot;8.507968&quot;&#10;		}&#10;  }&#10;}&#10;</code></pre>
<p>Bots tend to use more IPv4 addresses.</p>
<p>It is also interesting to know how your ISP fares in IPv6 adoption. If you know your ISP’s autonomous system number (ASN), you can use the <code>asn</code> parameter to query for this information. Refer to the <a href="/api/resources/radar/subresources/http/subresources/summary/methods/ip_version/">API reference</a> for other parameters.</p>
<p>If you do not know your ISP’s ASN, you can use <a href="https://radar.cloudflare.com/ip">Radar</a> to find what it is.</p>
<h3 id="top">Top</h3>
<h4 id="example-top-locations-by-ipv6-traffic">Example: top locations by IPv6 traffic</h4>
<p>In the following example, we will find which locations had a higher adoption of <a href="https://en.wikipedia.org/wiki/IPv6">IPv6</a> in the last 28 days.</p>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/radar/http/top/locations/ip_version/IPv6?name=ipv6&amp;botClass=LIKELY_HUMAN&amp;dateRange=28d&amp;format=json&amp;limit=5&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<pre><code class="language-json">{&#10;  &quot;success&quot;: true,&#10;  &quot;errors&quot;: [],&#10;  &quot;result&quot;: {&#10;		&quot;ipv6&quot;: [&#10;			{&#10;				&quot;clientCountryAlpha2&quot;: &quot;IN&quot;,&#10;				&quot;clientCountryName&quot;: &quot;India&quot;,&#10;				&quot;value&quot;: &quot;50.612747&quot;&#10;			},&#10;			{&#10;				&quot;clientCountryAlpha2&quot;: &quot;MY&quot;,&#10;				&quot;clientCountryName&quot;: &quot;Malaysia&quot;,&#10;				&quot;value&quot;: &quot;46.233654&quot;&#10;			},&#10;			{&#10;				&quot;clientCountryAlpha2&quot;: &quot;UY&quot;,&#10;				&quot;clientCountryName&quot;: &quot;Uruguay&quot;,&#10;				&quot;value&quot;: &quot;39.796762&quot;&#10;			},&#10;			{&#10;				&quot;clientCountryAlpha2&quot;: &quot;LK&quot;,&#10;				&quot;clientCountryName&quot;: &quot;Sri Lanka&quot;,&#10;				&quot;value&quot;: &quot;39.709355&quot;&#10;			},&#10;			{&#10;				&quot;clientCountryAlpha2&quot;: &quot;VN&quot;,&#10;				&quot;clientCountryName&quot;: &quot;Vietnam&quot;,&#10;				&quot;value&quot;: &quot;39.1514&quot;&#10;			}&#10;		]&#10;  }&#10;}&#10;</code></pre>
<p>According to the returned data, India is leading in IPv6 adoption.</p>
<p>For more information refer to the <a href="/api/resources/radar/subresources/http/subresources/locations/subresources/ip_version/methods/get/">API reference</a> for this endpoint.</p>
<h2 id="next-steps">Next steps</h2>
<p>Refer to <a href="/radar/investigate/application-layer-attacks/">Application layer attacks</a> to learn more about mitigfated HTTP requests.</p>
