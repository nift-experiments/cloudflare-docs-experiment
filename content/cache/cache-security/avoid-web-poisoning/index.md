<p>A cache poisoning attack uses an HTTP request to trick an origin web server into responding with a harmful resource that has the same cache key as a clean request. As a result, the poisoned resource gets cached and served to other users.</p>
<p>A Content Delivery Network (CDN) like Cloudflare relies on cache keys to compare new requests against cached resources. The CDN then determines whether the resource should be served from the cache or requested directly from the origin web server.</p>
<h2 id="learn-about-cache-poisoning">Learn about Cache Poisoning</h2>
<p>To deepen your understanding of the risks and vulnerabilities associated with cache poisoning, consult the following resources:</p>
<ul>
<li><a href="https://portswigger.net/blog/practical-web-cache-poisoning">Practical Web Cache Poisoning</a></li>
<li><a href="https://blog.cloudflare.com/cache-poisoning-protection/">How Cloudflare protects customers from cache poisoning</a></li>
</ul>
<h2 id="only-cache-files-that-are-truly-static">Only cache files that are truly static</h2>
<p>Review the caching configuration for your origin web server and ensure you are caching files that are static and do not depend on user input in any way. To learn more about Cloudflare caching, review:</p>
<ul>
<li><a href="/cache/concepts/default-cache-behavior/">Which file extensions does Cloudflare cache for static content?</a></li>
<li><a href="/cache/how-to/cache-rules/">How Do I Tell Cloudflare What to Cache?</a></li>
</ul>
<h2 id="do-not-trust-data-in-http-headers">Do not trust data in HTTP headers</h2>
<p>Attackers can exploit HTTP headers to inject malicious content into cached responses. For example, if your application reflects an untrusted header value in the response body, an attacker could use this to perform cross-site scripting (XSS) through the cache. To reduce this risk:</p>
<ul>
<li>Do not rely on values in HTTP headers if they are not part of your <a href="/cache/how-to/cache-keys/">cache key</a>.</li>
<li>Do not include untrusted header values in your response body.</li>
</ul>
<h2 id="do-not-trust-get-request-bodies">Do not trust GET request bodies</h2>
<p>Cloudflare caches contents of GET request bodies, but they are not included in the cache key. GET request bodies should be considered untrusted and should not modify the contents of a response. If a GET body can change the contents of a response, consider bypassing cache or using a POST request.</p>
<h2 id="monitor-web-security-advisories">Monitor web security advisories</h2>
<p>To keep informed about Internet security threats, Cloudflare recommends that you monitor web security advisories on a regular basis. Some of the more popular advisories include:</p>
<ul>
<li><a href="https://www.drupal.org/security">Drupal Security Advisories</a></li>
<li><a href="https://symfony.com/blog/category/security-advisories">Symfony Security Advisories</a></li>
<li><a href="https://getlaminas.org/security/advisories">Laminas Security Advisories</a></li>
</ul>
