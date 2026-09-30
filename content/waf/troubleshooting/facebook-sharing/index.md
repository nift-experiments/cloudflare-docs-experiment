<p>Cloudflare does not block or challenge requests from Facebook by default. However, a post of a website to Facebook returns an <em>Attention Required</em> error in the following situations:</p>
<ul>
<li>You have globally <a href="/fundamentals/reference/under-attack-mode/">enabled Under Attack mode</a>.</li>
<li>There is a <a href="/rules/configuration-rules/">configuration rule</a> or <a href="/rules/page-rules/">page rule</a> setting turning on Under Attack mode.</li>
<li>There is a <a href="/waf/custom-rules/">custom rule</a> with a challenge or block action that includes a Facebook IP address.</li>
</ul>
<p>A country challenge can block a Facebook IP address. Facebook is known to crawl from both the US and Ireland.</p>
<h2 id="resolution">Resolution</h2>
<p>To resolve issues sharing to Facebook, do one of the following:</p>
<ul>
<li>Remove the corresponding IP, ASN, or country custom rule that challenges or blocks Facebook IPs.</li>
<li>Create a <a href="/waf/custom-rules/skip/">skip rule</a> for <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></li>
</ul>
@markup("md", "content/.markup/bodies/15319.md")
</div> `AS32934` and `AS63293` (use the _Skip_ action and configure the rule to skip **Security Level**).
- Review existing configuration rules and Page Rules and make sure they are not affecting requests from Facebook IPs.
<p>If you experience issues with Facebook sharing, you can re-scrape pages via the <strong>Fetch New Scrape Information</strong> option on Facebook's Object Debugger. Facebook <a href="https://developers.facebook.com/docs/sharing/opengraph/using-objects">provides an API</a> to help update a large number of resources.</p>
<p>If you continue to have issues, you can <a href="/support/contacting-cloudflare-support/">contact Cloudflare Support</a> with the URLs of your website that cannot share to Facebook, and confirming that you have re-scraped the URLs.</p>
