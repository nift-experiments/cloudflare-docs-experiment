<p>Browser TTL controls how long an image stays in a browser's cache and specifically configures the <code>cache-control</code> response header.</p>
<h3 id="default-ttl">Default TTL</h3>
<p>By default, an image's TTL is set to two days to meet user needs, such as re-uploading an image under the same <a href="/images/storage/upload-images/upload-custom-path/">Custom ID</a>.</p>
<h2 id="custom-setting">Custom setting</h2>
<p>You can use two custom settings to control the Browser TTL, an account or a named variant. To adjust how long a browser should keep an image in the cache, set the TTL in seconds, similar to how the <code>max-age</code> header is set. The value should be an interval between one hour to one year.</p>
<h3 id="browser-ttl-for-an-account">Browser TTL for an account</h3>
<p>Setting the Browser TTL per account overrides the default TTL.</p>
<pre><code class="language-bash">curl --request PATCH &#x27;https://api.cloudflare.com/client/v4/accounts/{account_id}/images/v1/config&#x27; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;browser_ttl&quot;: 31536000&#10;}&#x27;&#10;</code></pre>
<p>When the Browser TTL is set to one year for all images, the response for the <code>cache-control</code> header is essentially <code>public</code>, <code>max-age=31536000</code>, <code>stale-while-revalidate=7200</code>.</p>
<h3 id="browser-ttl-for-a-named-variant">Browser TTL for a named variant</h3>
<p>Setting the Browser TTL for a named variant is a more granular option that overrides all of the above when creating or updating an image variant, specifically the <code>browser_ttl</code> option in seconds.</p>
<pre><code class="language-bash">curl &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_TAG&gt;/images/v1/variants&#x27; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;id&quot;:&quot;avatar&quot;,&#10;  &quot;options&quot;: {&#10;    &quot;width&quot;:100,&#10;    &quot;browser_ttl&quot;: 86400&#10;  }&#10;}&#x27;&#10;</code></pre>
<p>When the Browser TTL is set to one day for images requested with this variant, the response for the <code>cache-control</code> header is essentially <code>public</code>, <code>max-age=86400</code>, <code>stale-while-revalidate=7200</code>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9473.md")
</aside>
