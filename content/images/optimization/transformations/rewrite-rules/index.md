<p>You can use Transform Rules to rewrite URLs for every image that you transform through Images.</p>
<p>This page covers examples for the following scenarios:</p>
<ul>
<li>Serve images from custom paths</li>
<li>Modify existing URLs to be compatible with transformations in Images</li>
<li>Transform every image requested on your zone with Images</li>
</ul>
<p>To create a rule:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Rules Overview</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Create rule</strong> next to <strong>URL Rewrite Rules</strong>.</li>
</ol>
<h2 id="before-you-start">Before you start</h2>
<p>Every rule runs before and after the transformation request.</p>
<p>If the path for the request matches the path where the original images are stored on your server, this may cause the request to fetch the original image to loop.</p>
<p>To direct the request to the origin server, you can check for the string <code>image-resizing</code> in the <code>Via</code> header:</p>
<p><code>...and (not (any(http.request.headers[&quot;via&quot;][*] contains &quot;image-resizing&quot;)))</code></p>
<h2 id="serve-images-from-custom-paths">Serve images from custom paths</h2>
<p>By default, requests to transform images through Images are served from the <code>/cdn-cgi/image/</code> path.
You can use Transform Rules to rewrite URLs.</p>
<h3 id="basic-version">Basic version</h3>
<p>Free and Pro plans support string matching rules (including wildcard operations) that do not require regular expressions.</p>
<p>This example lets you rewrite a request from <code>example.com/images</code> to <code>example.com/cdn-cgi/image/</code>:</p>
<pre><code class="language-txt">(starts_with(http.request.uri.path, &quot;/images&quot;)) and (not (any(http.request.headers[&quot;via&quot;][*] contains &quot;image-resizing&quot;)))&#10;</code></pre>
<pre><code class="language-txt">concat(&quot;/cdn-cgi/image&quot;, substring(http.request.uri.path, 7))&#10;</code></pre>
<h3 id="advanced-version">Advanced version</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9461.md")
</aside>
<p>There is an advanced version of Transform Rules supporting regular expressions.</p>
<p>This example lets you rewrite a request from <code>example.com/images</code> to <code>example.com/cdn-cgi/image/</code>:</p>
<pre><code class="language-txt">(http.request.uri.path matches &quot;^/images/.*$&quot;) and (not (any(http.request.headers[&quot;via&quot;][*] contains &quot;image-resizing&quot;)))&#10;</code></pre>
<pre><code class="language-txt">regex_replace(http.request.uri.path, &quot;^/images/&quot;, &quot;/cdn-cgi/image/&quot;)&#10;</code></pre>
<h2 id="modify-existing-urls-to-be-compatible-with-transformations-in-images">Modify existing URLs to be compatible with transformations in Images</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9460.md")
</aside>
<p>This example lets you rewrite your URL parameters to be compatible with Images:</p>
<pre><code class="language-txt">(http.request.uri matches &quot;^/(.*)\\?width=([0-9]+)&amp;height=([0-9]+)$&quot;)&#10;</code></pre>
<pre><code class="language-txt">regex_replace(&#10;  http.request.uri,&#10;  &quot;^/(.*)\\?width=([0-9]+)&amp;height=([0-9]+)$&quot;,&#10;  &quot;/cdn-cgi/image/width=${2},height=${3}/${1}&quot;&#10;)&#10;</code></pre>
<p>Leave the <strong>Query</strong> &gt; <strong>Rewrite to</strong> &gt; <em>Static</em> field empty.</p>
<h2 id="pass-every-image-requested-on-your-zone-through-images">Pass every image requested on your zone through Images</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9459.md")
</aside>
<p>This example lets you transform every image that is requested on your zone with the <code>format=auto</code> option:</p>
<pre><code class="language-txt">(http.request.uri.path.extension matches &quot;(jpg)|(jpeg)|(png)|(gif)&quot;) and (not (any(http.request.headers[&quot;via&quot;][*] contains &quot;image-resizing&quot;)))&#10;</code></pre>
<pre><code class="language-txt">regex_replace(http.request.uri.path, &quot;/(.*)&quot;, &quot;/cdn-cgi/image/format=auto/${1}&quot;)&#10;</code></pre>
