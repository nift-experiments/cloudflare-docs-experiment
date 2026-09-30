<p>Image delivery is supported from all customer domains under the same Cloudflare account. To serve images through custom domains, an image URL should be adjusted to the following format:</p>
<pre><code class="language-txt">https://example.com/cdn-cgi/imagedelivery/&lt;ACCOUNT_HASH&gt;/&lt;IMAGE_ID&gt;/&lt;VARIANT_NAME&gt;&#10;</code></pre>
<p>Example with a custom domain:</p>
<pre><code class="language-txt">https://example.com/cdn-cgi/imagedelivery/ZWd9g1K7eljCn_KDTu_MWA/083eb7b2-5392-4565-b69e-aff66acddd00/public&#10;</code></pre>
<p>In this example, <code>&lt;ACCOUNT_HASH&gt;</code>, <code>&lt;IMAGE_ID&gt;</code> and <code>&lt;VARIANT_NAME&gt;</code> are the same, but the hostname and prefix path is different:</p>
<ul>
<li><code>example.com</code>: Cloudflare proxied domain under the same account as the Cloudflare Images.</li>
<li><code>/cdn-cgi/imagedelivery</code>: Path to trigger <code>cdn-cgi</code> image proxy.</li>
<li><code>ZWd9g1K7eljCn_KDTu_MWA</code>: The Images account hash. This can be found in the Cloudflare Images Dashboard.</li>
<li><code>083eb7b2-5392-4565-b69e-aff66acddd00</code>: The image ID.</li>
<li><code>public</code>: The variant name.</li>
</ul>
<h2 id="custom-paths">Custom paths</h2>
<p>By default, Images are served from the <code>/cdn-cgi/imagedelivery/</code> path. You can use <a href="/rules/transform/">Transform Rules</a> to rewrite URLs and serve images from custom paths.</p>
<h3 id="basic-version">Basic version</h3>
<p>Free and Pro plans support string matching rules (including wildcard operations) that do not require regular expressions.</p>
<p>This example lets you rewrite a request from <code>example.com/images</code> to <code>example.com/cdn-cgi/imagedelivery/&lt;ACCOUNT_HASH&gt;</code>.</p>
<p>To create a rule:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Rules Overview</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Next to <strong>URL Rewrite Rules</strong>, select <strong>Create rule</strong>.</li>
<li>Under <strong>If incoming requests match</strong>, select <strong>Wildcard pattern</strong> and enter the following <strong>Request URL</strong> (update with your own domain):</li>
</ol>
<pre><code class="language-txt">https://example.com/images/*&#10;</code></pre>
<ol start="4">
<li>
<p>Under <strong>Then rewrite the path and/or query</strong> &gt; <strong>Path</strong>, enter the following values (using your account hash):</p>
<ul>
<li><strong>Target path</strong>: [<code>/</code>] <code>images/*</code></li>
<li><strong>Rewrite to</strong>: [<code>/</code>] <code>cdn-cgi/imagedelivery/&lt;ACCOUNT_HASH&gt;/${1}</code></li>
</ul>
</li>
<li>
<p>Select <strong>Deploy</strong> when you are done.</p>
</li>
</ol>
<h3 id="advanced-version">Advanced version</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9469.md")
</aside>
<p>This example lets you rewrite a request from <code>example.com/images/some-image-id/w100,h300</code> to <code>example.com/cdn-cgi/imagedelivery/&lt;ACCOUNT_HASH&gt;/some-image-id/width=100,height=300</code> and assumes Flexible variants feature is turned on.</p>
<p>To create a rule:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Rules Overview</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Next to <strong>URL Rewrite Rules</strong>, select <strong>Create rule</strong>.</li>
<li>Under <strong>If incoming requests match</strong>, select <strong>Custom filter expression</strong> and then select <strong>Edit expression</strong>.</li>
<li>In the text field, enter <code>(http.request.uri.path matches &quot;^/images/.*$&quot;)</code>.</li>
<li>Under <strong>Path</strong>, select <strong>Rewrite to</strong>.</li>
<li>Select <em>Dynamic</em> and enter the following in the text field.</li>
</ol>
<pre><code class="language-txt">regex_replace(&#10;  http.request.uri.path,&#10;  &quot;^/images/(.*)\\?w([0-9]+)&amp;h([0-9]+)$&quot;,&#10;  &quot;/cdn-cgi/imagedelivery/&lt;ACCOUNT_HASH&gt;/${1}/width=${2},height=${3}&quot;&#10;)&#10;</code></pre>
<h2 id="limitations">Limitations</h2>
<p>When using a custom domain, it is not possible to directly set up WAF rules that act on requests hitting the <code>/cdn-cgi/imagedelivery/</code> path. If you need to set up WAF rules, you can use a Cloudflare Worker to access your images and a Route using your domain to execute the worker. For an example worker, refer to <a href="/images/optimization/hosted-images/serve-private-images/">Serve private images using signed URL tokens</a>.</p>
