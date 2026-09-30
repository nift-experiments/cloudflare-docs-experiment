<div class="nb-description">
@markup("md", "content/.markup/bodies/237.md")
</div>
<p>Turnstile can be embedded into any website without sending traffic through Cloudflare and works without showing visitors a CAPTCHA.</p>
<div class="video-frame"><img class="video-poster" src="https://imagedelivery.net/xDOJvHcv1KwTQn6S-BGFIw/5b75f329-b7fe-4122-cae4-9bee54c35100/public" alt="Get started with Cloudflare Turnstile"><iframe src="https://customer-1mwganm1ma0xgnmj.cloudflarestream.com/7f1104dc5895d96c1957a4db5fdf496a/iframe?preload=true&amp;letterboxColor=transparent" title="Get started with Cloudflare Turnstile" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>
<p>Cloudflare issues challenges through the <a href="/cloudflare-challenges/">Challenge Platform</a>, which is the same underlying technology powering <a href="/turnstile/">Turnstile</a>.</p>
<p>In contrast to our Challenge page offerings, Turnstile allows you to run challenges anywhere on your site in a less-intrusive way without requiring the use of Cloudflare's CDN.</p>
<h2 id="how-turnstile-works">How Turnstile works</h2>
<p><img src="/assets/upstream/images/turnstile/turnstile-overview.png" alt="Turnstile Overview" /></p>
<p>Turnstile adapts the challenge outcome to the individual visitor or browser. First, we run a series of small non-interactive JavaScript challenges to gather signals about the visitor or browser environment.</p>
<p>These challenges include proof-of-work (computational puzzles), proof-of-space, probing for web APIs, and various other challenges for detecting browser-quirks and human behavior. As a result, we can fine-tune the difficulty of the challenge to the specific request and avoid showing a visual or interactive puzzle to a user.</p>
<p>Turnstile performs client-side security challenges on behalf of the website operator to distinguish human visitors from automated traffic. To do so, Turnstile processes only the data strictly necessary to provide this security function. Turnstile does not access, store, or transmit user communications, form entries, or other page inputs.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/236.md")
</aside>
<h3 id="widget-types">Widget types</h3>
<p>Turnstile <a href="/turnstile/concepts/widget/">widget types</a> include:</p>
<ul>
<li><strong>Managed</strong> (recommended): Automatically decides whether to show a checkbox based on visitor risk level.</li>
<li><strong>Non-interactive</strong>: Visitors never need to interact with the widget.</li>
<li><strong>Invisible</strong>: The widget is completely hidden from the visitor.</li>
</ul>
<hr />
<h2 id="accessibility">Accessibility</h2>
<p>Turnstile is WCAG 2.2 AA compliant.</p>
<hr />
<h2 id="features">Features</h2>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/238.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/239.md")
</div>
<hr />
<h2 id="related-products">Related products</h2>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/240.md")
</div>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/241.md")
</div>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/242.md")
</div>
<hr />
<h2 id="more-resources">More resources</h2>
<div class="nb-card-grid">
@input("content/.markup/bodies/244.md")
</div>
