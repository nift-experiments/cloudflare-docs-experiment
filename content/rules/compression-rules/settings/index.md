<p>Compression Rules support the configuration settings covered in the following sections.</p>
<h2 id="dashboard-configuration-settings">Dashboard configuration settings</h2>
<h3 id="enable-zstandard-zstd-compression">Enable Zstandard (Zstd) compression <span class="nb-badge">Beta</span></h3>
<p>Sets Zstandard as the preferred compression algorithm. If it is not supported, will automatically fall back to Brotli, Gzip, or uncompressed data.</p>
<h3 id="enable-brotli-and-gzip-compression">Enable Brotli and Gzip compression</h3>
<p>Enables Cloudflare's default compression setting. Brotli is the preferred compression algorithm. It will automatically fall back to Gzip or to uncompressed data.</p>
<h3 id="disable-compression">Disable compression</h3>
<p>Disables compression for matching requests. Also disables Cloudflare's <a href="/speed/optimization/content/compression/">default compression behavior</a>.</p>
<h3 id="custom">Custom</h3>
<p>Defines a custom order for compression algorithms.</p>
<p>Allowed values are the following:</p>
<ul>
<li><strong>Gzip</strong>: Use the Gzip compression algorithm, if supported by the website visitor.</li>
<li><strong>Brotli</strong>: Use the Brotli compression algorithm, if supported by the website visitor.</li>
<li><strong>Zstandard</strong>: Use the Zstandard (Zstd) compression algorithm, if supported by the website visitor.</li>
<li><strong>Auto</strong>: Compress the response according to the algorithms supported by the website visitor (if any). Cloudflare will define the order of preference for the compression algorithms, which may change in the future. Has the same behavior of the <strong>Enable compression</strong> option.</li>
<li><strong>Default</strong>: Use Cloudflare's <a href="/speed/optimization/content/compression/">default compression behavior</a>, which depends on the response content type.</li>
</ul>
<p>If you specify only <em>Gzip</em>, <em>Brotli</em>, or <em>Zstandard</em> and no algorithm matches, the response will have no compression. To configure a fallback compression mechanism, add <em>Auto</em> to the list.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13026.md")
</aside>
<hr />
<h2 id="api-configuration-settings">API configuration settings</h2>
<p>The configuration object supported by the <code>compress_response</code> action has the following format:</p>
<pre><code class="language-json">&quot;action_parameters&quot;: {&#10;  &quot;algorithms&quot;: [&#10;    { &quot;name&quot;: &quot;&lt;VALUE1&gt;&quot; },&#10;    { &quot;name&quot;: &quot;&lt;VALUE2&gt;&quot; },&#10;    // ...&#10;  ]&#10;}&#10;</code></pre>
<p>The <code>algorithms</code> list must contain at least one item.</p>
<p>The supported algorithm values are:</p>
<ul>
<li><code>gzip</code>: Use the Gzip compression algorithm, if supported by the website visitor.</li>
<li><code>brotli</code>: Use the Brotli compression algorithm, if supported by the website visitor.</li>
<li><code>zstd</code>: Use the Zstandard compression algorithm, if supported by the website visitor.</li>
<li><code>none</code>: Do not use any compression algorithm.</li>
<li><code>auto</code>: Compress the response according to the algorithms supported by the website visitor (if any). Cloudflare will define the order of preference for the compression algorithms, which may change in the future.</li>
<li><code>default</code>: Use Cloudflare's <a href="/speed/optimization/content/compression/#compression-between-cloudflare-and-website-visitors">default compression behavior</a>, which depends on the response content type.</li>
</ul>
<p>If you include <code>none</code>, <code>default</code>, or <code>auto</code> in the list, it must be the last value in the list.</p>
<p>When you specify only the <code>gzip</code>, <code>brotli</code>, or <code>zstd</code> algorithms, if no algorithm matches then the response will have no compression. To configure a fallback compression mechanism, add <code>auto</code> to the list.</p>
<p>For API examples, refer to the <a href="/rules/compression-rules/examples/">Examples gallery</a>.</p>
