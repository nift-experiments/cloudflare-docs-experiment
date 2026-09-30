<h2 id="web-cache-deception-attacks">Web Cache Deception attacks</h2>
<p>A Web Cache Deception attack tricks a user into visiting a URL that appears to point to a static asset but actually returns dynamic, personalized content from the origin.</p>
<p>This attack works when an origin treats requests to non-existent paths as equivalent to a parent path — for example, when <code>http://www.example.com/newsfeed</code> is a dynamic page that returns different content for each authenticated user, and the origin also serves that same response for <code>/newsfeed/foo.jpg</code>. Because the path ends in <code>.jpg</code>, Cloudflare caches the response by default. The attacker then visits the same URL and receives the cached copy of the user's personalized content.</p>
<h2 id="cache-deception-armor-protects-against-attacks">Cache Deception Armor protects against attacks</h2>
<p>You can protect users from Web Cache Deception attacks by <a href="/cache/cache-security/cache-deception-armor/#enable-cache-deception-armor">creating a cache rule</a>. With this rule, you can continue to cache static assets, but the rule will verify a URL's extension matches the returned <code>Content-Type</code>.</p>
<p>In the newsfeed example above, if <code>http://www.example.com/newsfeed</code> is a script that outputs a webpage, the <code>Content-Type</code> is <code>text/html</code>. On the other hand, <code>http://www.example.com/newsfeed/foo.jpg</code> is expected to have <code>image/jpeg</code> as <code>Content-Type</code>. When a mismatch that could result in a Web Cache Deception attack is found, Cloudflare does not cache the response.</p>
<h3 id="exceptions">Exceptions</h3>
<ul>
<li>If the returned <code>Content-Type</code> is <code>application/octet-stream</code>, the extension does not matter because that is typically a signal to instruct the browser to save the asset instead of to display it.</li>
<li>Cloudflare allows <code>.jpg</code> to be served as <code>image/webp</code> or <code>.gif</code> as <code>video/webm</code> and other cases that are unlikely to be attacks.</li>
<li>Keep in mind that Cache Deception Armor depends upon <a href="/cache/concepts/cache-control/">Origin Cache Control</a>. A <code>Cache-Control</code> header from the origin, or an <a href="/cache/how-to/cache-rules/settings/#edge-ttl">Edge Cache TTL Cache Rule</a> may override the protection.</li>
</ul>
<h2 id="enable-cache-deception-armor">Enable Cache Deception Armor</h2>
<p>To enable Cache Deception Armor, you need to start by creating a <a href="/cache/how-to/cache-rules/">cache rule</a>. Follow the steps below for guidance:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Cache Rules</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Create rule</strong>.</li>
<li>Under <strong>When incoming requests match</strong>, define the <a href="/ruleset-engine/rules-language/expressions/edit-expressions/#expression-builder">rule expression</a>.</li>
<li>Under <strong>Then</strong>, in the <strong>Cache eligibility</strong> section, select <strong>Eligible for cache</strong>.</li>
<li>Add the <strong>Cache Key</strong> setting to the rule and turn on <strong>Cache deception armor</strong>.</li>
<li>To save and deploy your rule, select <strong>Deploy</strong>. If you are not ready to deploy your rule, select <strong>Save as Draft</strong>.</li>
</ol>
