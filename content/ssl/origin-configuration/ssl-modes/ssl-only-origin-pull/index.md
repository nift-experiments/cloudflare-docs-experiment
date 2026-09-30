<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14246.md")
</aside>
<p>When you set your encryption mode to <strong>Strict (SSL-Only Origin Pull)</strong>, connections to the origin will always be made using SSL/TLS, regardless of the scheme requested by the visitor.</p>
<p>The certificate presented by the origin will be validated the same as with <a href="/ssl/origin-configuration/ssl-modes/full-strict/">Full (strict) mode</a>.</p>
<div class="video-frame"><iframe src="https://customer-1mwganm1ma0xgnmj.cloudflarestream.com/f407072cb5b4837c8c3a58a69cde90b5/iframe?preload=true&amp;letterboxColor=transparent&amp;poster=https%3A%2F%2Fimagedelivery.net%2FxDOJvHcv1KwTQn6S-BGFIw%2F28f00d39-6aee-4a42-c688-e37021bcb000%2Fpublic" title="Configure Strict encryption mode" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>
<h2 id="use-when">Use when</h2>
<p>You want the most secure configuration available for your origin, you are an Enterprise customer, and you meet the requirements for <a href="/ssl/origin-configuration/ssl-modes/full-strict/"><strong>Full (strict)</strong> mode</a>.</p>
<h2 id="required-setup">Required setup</h2>
<p>The setup is generally the same as <a href="/ssl/origin-configuration/ssl-modes/full-strict/"><strong>Full (strict)</strong> mode</a>, but you select <strong>Strict (SSL-Only Origin Pull)</strong> for your encryption mode.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14245.md")
</aside>
<h3 id="process">Process</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14249.md")
</div></div>
<h2 id="limitations">Limitations</h2>
<p>Depending on your origin configuration, you may have to adjust settings to avoid <a href="/ssl/troubleshooting/mixed-content-errors/">Mixed Content errors</a> or <a href="/ssl/troubleshooting/too-many-redirects/">redirect loops</a>.</p>
