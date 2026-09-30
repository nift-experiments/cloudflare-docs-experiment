<p>When a visitor solves a <a href="/cloudflare-challenges/">Cloudflare Challenge</a> - as part of a <a href="/waf/custom-rules/">WAF custom rule</a> or <a href="/waf/tools/ip-access-rules/">IP Access rule</a> - you can set the <strong>Challenge Passage</strong> to prevent them from having to solve future Challenges for a specified period of time.</p>
<h3 id="how-it-works">How it works</h3>
<p>When a visitor successfully solves a challenge, Cloudflare sets a <a href="/fundamentals/reference/policies-compliances/cloudflare-cookies/#additional-cookies-used-by-the-challenge-platform"><code>cf_clearance</code> cookie</a> in their browser. This cookie specifies the duration your website is accessible to that visitor.</p>
<p>When that visitor tries to access other parts of your website, Cloudflare evaluates the cookie before presenting another challenge. If the cookie is still valid, no challenges will be shown.</p>
<p>When Cloudflare evaluates a <code>cf_clearance</code> cookie, a few extra minutes are included to account for clock skew. For XmlHTTP requests, an extra hour is added to the validation time to prevent breaking XmlHTTP requests for pages that set short lifetimes.</p>
<h3 id="customize-the-challenge-passage">Customize the Challenge Passage</h3>
<p>By default, the <code>cf_clearance</code> cookie has a lifetime of 30 minutes. Cloudflare recommends a setting between 15 and 45 minutes.</p>
<p>To update the Challenge Passage (and the value of the <code>cf_clearance</code> cookie):</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/4050.md")
</div>
<h3 id="limitations">Limitations</h3>
<p>The Challenge Passage does not apply to rate limiting rules.</p>
