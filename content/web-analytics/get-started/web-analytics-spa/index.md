<p>Cloudflare Web Analytics automatically tracks user interactions on Single Page Applications (SPAs) via one of the following three methods, depending on which is supported:</p>
<ol>
<li>Using the <a href="https://developer.chrome.com/docs/web-platform/soft-navigations">Soft Navigations API</a></li>
<li>Listening on <code>navigate</code> events via the <a href="https://developer.mozilla.org/en-US/docs/Web/API/Navigation_API">Navigation API</a></li>
<li>By patching the <a href="https://developer.mozilla.org/en-US/docs/Web/API/History_API">History API</a>'s <code>pushState</code> function and listening to the <code>onpopstate</code> event</li>
</ol>
<h2 id="disable-spa-measurement">Disable SPA measurement</h2>
<p>If you want to disable the automatic tracking for SPAs, you can do so by adding the <code>spa</code> option with a value of <code>false</code> in the data attribute of the script tag, as shown below:</p>
<pre><code class="language-html">&lt;script&#10;  type=&quot;module&quot;&#10;  src=&quot;https://static.cloudflareinsights.com/beacon.min.js&quot;&#10;  data-cf-beacon=&#x27;{&quot;token&quot;: &quot;...&quot;, &quot;spa&quot;: false}&#x27;&#10;&gt;&lt;/script&gt;&#10;</code></pre>
<p>Note: this requires using <a href="/web-analytics/get-started/#sites-not-proxied-through-cloudflare">the manual embedding approach</a>.</p>
<h3 id="google-tag-manager-gtm">Google Tag Manager (GTM)</h3>
<p>If you are using Google Tag Manager (GTM), you can disable SPA tracking by passing the <code>spa=false</code> option via the query string in the script URL:</p>
<pre><code class="language-html">&lt;script&#10;  type=&quot;module&quot;&#10;  src=&quot;https://static.cloudflareinsights.com/beacon.min.js?token=...&amp;spa=false&quot;&#10;&gt;&lt;/script&gt;&#10;</code></pre>
