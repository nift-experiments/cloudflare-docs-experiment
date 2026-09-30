<p>Cloudflare's Browser Integrity Check (BIC) looks for common HTTP headers abused most commonly by spammers and denies access to your page.</p>
<p>It also challenges visitors without a user agent or with a non-standard user agent such as commonly used by abusive bots, crawlers, or visitors.</p>
<p>Browser Integrity Check is enabled by default.</p>
<h2 id="disable-browser-integrity-check">Disable Browser Integrity Check</h2>
<h3 id="disable-globally">Disable globally</h3>
<p>To disable BIC globally for your zone:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15344.md")
</div>
<h3 id="disable-selectively">Disable selectively</h3>
<p>To disable BIC selectively, you can skip Browser Integrity Check using a <a href="/waf/custom-rules/skip/">custom rule with a skip action</a>.</p>
<p>Also, use a <a href="/rules/configuration-rules/">configuration rule</a> to selectively enable or disable this feature for certain sections of your website using a filter expression (such as a matching hostname or request URL path).</p>
