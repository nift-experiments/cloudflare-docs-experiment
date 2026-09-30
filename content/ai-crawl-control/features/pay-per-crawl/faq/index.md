<h2 id="frequently-asked-questions-for-site-owners">Frequently asked questions for site owners</h2>
<h3 id="can-i-set-different-prices-for-different-ai-crawlers">Can I set different prices for different AI crawlers?</h3>
<p>No. Pay per crawl allows you to configure different actions (Block, Charge, or Allow) for each crawler, but you can only set a single price that applies to all crawlers configured with the &quot;Charge&quot; option.</p>
<h2 id="frequently-asked-questions-for-ai-bot-operators">Frequently asked questions for AI bot operators</h2>
<h3 id="will-i-be-charged-for-re-crawling-the-same-page">Will I be charged for re-crawling the same page?</h3>
<p>Yes. Every time your AI crawler accesses content on a website protected with pay per crawl, it will incur the cost set by the site owner. You should implement mechanisms within your crawler to track expenditure and enforce any spending limits you want to set.</p>
<p>Some paths are always free to crawl. These paths are: <code>/robots.txt</code>, <code>/sitemap.xml</code>, <code>/security.txt</code>, <code>/.well-known/security.txt</code>, <code>/crawlers.json</code>.</p>
<h3 id="am-i-charged-for-error-responses">Am I charged for error responses?</h3>
<p>No. Charging events are only triggered for successful HTTP response codes. Error responses are not billed, even if you have sent the <code>crawler-exact-price</code> or <code>crawler-max-price</code> headers.</p>
<h3 id="what-user-agent-should-i-use">What user agent should I use?</h3>
<p>Use the standard user agents associated with your AI crawler that you have onboarded to Cloudflare and identified through Web Bot Auth.</p>
