<p>Cloudflare Pages includes a number of defaults for serving your Pages sites. This page details some of those decisions, so you can understand how Pages works, and how you might want to override some of the default behaviors.</p>
<h2 id="route-matching">Route matching</h2>
<p>If an HTML file is found with a matching path to the current route requested, Pages will serve it. Pages will also redirect HTML pages to their extension-less counterparts: for instance, <code>/contact.html</code> will be redirected to <code>/contact</code>, and <code>/about/index.html</code> will be redirected to <code>/about/</code>.</p>
<h2 id="not-found-behavior">Not Found behavior</h2>
<p>You can define a custom page to be displayed when Pages cannot find a requested file by creating a <code>404.html</code> file. Pages will then attempt to find the closest 404 page. If one is not found in the same directory as the route you are currently requesting, it will continue to look up the directory tree for a matching <code>404.html</code> file, ending in <code>/404.html</code>. This means that you can define custom 404 paths for situations like <code>/blog/404.html</code> and <code>/404.html</code>, and Pages will automatically render the correct one depending on the situation.</p>
<h2 id="single-page-application-spa-rendering">Single-page application (SPA) rendering</h2>
<p>If your project does not include a top-level <code>404.html</code> file, Pages assumes that you are deploying a single-page application. This includes frameworks like React, Vue, and Angular. Pages' default single-page application behavior matches all incoming paths to the root (<code>/</code>), allowing you to capture URLs like <code>/about</code> or <code>/help</code> and respond to them from within your SPA.</p>
<h2 id="caching-and-performance">Caching and performance</h2>
<h3 id="recommendations">Recommendations</h3>
<p>In most situations, you should avoid setting up any custom caching on your site. Pages comes with built in caching defaults that are optimized for caching as much as possible, while providing the most up to date content. Every time you deploy an asset to Pages, the asset remains cached on the Cloudflare CDN until your next deployment.</p>
<p>Therefore, if you add caching to your <a href="/pages/configuration/custom-domains/">custom domain</a>, it may lead to stale assets being served after a deployment.</p>
<p>In addition, adding caching to your custom domain may cause issues with <a href="/pages/configuration/redirects/">Pages redirects</a> or <a href="/pages/functions/">Pages functions</a>. These issues can occur because the cached response might get served to your end user before Pages can act on the request.</p>
<p>However, there are some situations where <a href="/cache/how-to/cache-rules/">Cache Rules</a> on your custom domain does make sense. For example, you may have easily cacheable locations for immutable assets, such as CSS or JS files with content hashes in their file names. Custom caching can help in this case, speeding up the user experience until the file (and associated filename) changes. Just make sure that your caching does not interfere with any redirects or Functions.</p>
<p>Note that when you use Cloudflare Pages, the static assets that you upload as part of your Pages project are automatically served from <a href="/cache/how-to/tiered-cache/">Tiered Cache</a>. You do not need to separately enable Tiered Cache for the custom domain that your Pages project runs on.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="purging-the-cache">Purging the cache</h3>
@markup("md", "content/.markup/bodies/11057.md")
</aside>
<h3 id="behavior">Behavior</h3>
<p>For browser caching, Pages always sends <code>Etag</code> headers for <code>200 OK</code> responses, which the browser then returns in an <code>If-None-Match</code> header on subsequent requests for that asset. Pages compares the <code>If-None-Match</code> header from the request with the <code>Etag</code> it's planning to send, and if they match, Pages instead responds with a <code>304 Not Modified</code> that tells the browser it's safe to use what is stored in local cache.</p>
<p>Pages currently returns <code>200</code> responses for HTTP range requests; however, the team is working on adding spec-compliant <code>206</code> partial responses.</p>
<p>Pages will also serve Gzip and Brotli responses whenever possible.</p>
<h2 id="asset-retention">Asset retention</h2>
<p>We will insert assets into the cache on a per-data center basis. Assets have a time-to-live (TTL) of one week but can also disappear at any time. If you do a new deploy, the assets could exist in that data center up to one week.</p>
<h2 id="headers">Headers</h2>
<p>By default, Pages automatically adds several <a href="https://developer.mozilla.org/en-US/docs/Glossary/Response_header">HTTP response headers</a> when serving assets, including:</p>
<pre><code class="language-txt">Access-Control-Allow-Origin: *&#10;Cf-Ray: $CLOUDFLARE_RAY_ID&#10;Referrer-Policy: strict-origin-when-cross-origin&#10;Etag: $ETAG&#10;Content-Type: $CONTENT_TYPE&#10;X-Content-Type-Options: nosniff&#10;Server: cloudflare&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11056.md")
</aside>
<pre><code class="language-txt">// if the asset has been encoded&#10;Cache-Control: no-transform&#10;Content-Encoding: $CONTENT_ENCODING&#10;&#10;// if the asset is cacheable (the request does not have an `Authorization` or `Range` header)&#10;Cache-Control: public, max-age=0, must-revalidate&#10;&#10;// if requesting the asset over a preview URL&#10;X-Robots-Tag: noindex&#10;</code></pre>
<p>To modify the headers added by Cloudflare Pages - perhaps to add <a href="/pages/configuration/early-hints/">Early Hints</a> - update the <a href="/pages/configuration/headers/">_headers file</a> in your project.</p>
