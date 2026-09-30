<p>When you set your encryption mode to <strong>Full</strong>, Cloudflare allows HTTPS connections between your visitor and Cloudflare and makes connections to the origin using the scheme requested by the visitor. If your visitor uses <code>http</code>, then Cloudflare connects to the origin using plaintext HTTP and vice versa.</p>
<div class="video-frame"><img class="video-poster" src="https://imagedelivery.net/xDOJvHcv1KwTQn6S-BGFIw/c0c41f09-2d73-4ee5-8b71-dbb271ed1800/public" alt="Configure Full encryption mode"><iframe src="https://customer-1mwganm1ma0xgnmj.cloudflarestream.com/a1e79096a2b042e0525a8543c232279a/iframe?preload=true&amp;letterboxColor=transparent" title="Configure Full encryption mode" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>
<h2 id="use-when">Use when</h2>
<p>Choose <strong>Full</strong> mode when your origin can support an SSL certification, but — for various reasons — it cannot support a valid, publicly trusted certificate.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14259.md")
</aside>
<h2 id="required-setup">Required setup</h2>
<h3 id="prerequisites">Prerequisites</h3>
<p>Before enabling <strong>Full</strong> mode, make sure your origin allows HTTPS connections on port 443 and presents a certificate (self-signed, <a href="/ssl/origin-configuration/origin-ca/">Cloudflare Origin CA</a>, or purchased from a Certificate Authority). Otherwise, your visitors may experience a <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-525/">525 error</a>.</p>
<p>Depending on your origin configuration, you may have to adjust settings to avoid <a href="/ssl/troubleshooting/mixed-content-errors/">Mixed Content errors</a> or <a href="/ssl/troubleshooting/too-many-redirects/">redirect loops</a>.</p>
<h3 id="process">Process</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14262.md")
</div></div>
<h2 id="limitations">Limitations</h2>
<p>The certificate presented by the origin will <strong>not be validated in any way</strong>. It can be expired, self-signed, or not even have a matching CN/SAN entry for the hostname requested.</p>
<p>Without using <a href="/ssl/origin-configuration/ssl-modes/full-strict/"><strong>Full (strict)</strong></a>, a malicious party could technically hijack the connection and present their own certificate.</p>
