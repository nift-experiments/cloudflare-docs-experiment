<p>When enabled, <a href="/waf/tools/scrape-shield/hotlink-protection/">Cloudflare Hotlink Protection</a> blocks all HTTP referrers that are not part of your domain or zone. That presents a problem if you allow partners to use inline links to your assets.</p>
<h2 id="allow-requests-from-partners-using-custom-rules">Allow requests from partners using custom rules</h2>
<p>You can use custom rules to protect against hotlinking while allowing inline links from your partners. In this case, you will need to disable <a href="/waf/tools/scrape-shield/hotlink-protection/">Hotlink Protection</a> so that partner referrals are not blocked by that feature.</p>
<p>This example <a href="/waf/custom-rules/create-dashboard/">custom rule</a> uses the <a href="/ruleset-engine/rules-language/fields/reference/http.referer/"><code>http.referer</code></a> field to target HTTP referrals from partner sites.</p>
<p>The <code>not</code> operator matches HTTP referrals that are not from partner sites, and the action blocks them:</p>
<ul>
<li>
<p><strong>When incoming requests match</strong>:</p>
<p>Use the expression editor:<br/>
<code>not (http.referer contains &quot;example.com&quot; or http.referer eq &quot;www.example.net&quot; or http.referer eq &quot;www.cloudflare.com&quot;)</code></p>
</li>
<li>
<p><strong>Then take action</strong>: <em>Block</em></p>
</li>
</ul>
<h2 id="allow-requests-from-partners-using-configuration-rules">Allow requests from partners using Configuration Rules</h2>
<p>Alternatively, you can <a href="/rules/configuration-rules/create-dashboard/">create a configuration rule</a> to exclude HTTP referrals from partner sites from Hotlink Protection. In this case, you would keep the Hotlink Protection feature enabled.</p>
