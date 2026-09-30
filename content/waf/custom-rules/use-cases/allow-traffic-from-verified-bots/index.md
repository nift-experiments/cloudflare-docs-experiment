<p>This example <a href="/waf/custom-rules/create-dashboard/">custom rule</a> challenges requests from a list of countries, but allows traffic from search engine bots — such as Googlebot and Bingbot — and from other <a href="/bots/concepts/bot/verified-bots/">verified bots</a>.</p>
<p>The rule expression uses the <a href="/ruleset-engine/rules-language/fields/reference/cf.client.bot/"><code>cf.client.bot</code></a> field to determine if the request originated from a known good bot or crawler.</p>
<ul>
<li><strong>When incoming requests match</strong>:</li>
</ul>
<table>
<thead>
<tr>
<th>Field</th>
<th>Operator</th>
<th>Value</th>
<th>Logic</th>
</tr>
</thead>
<tbody>
<tr>
<td>Country</td>
<td>is in</td>
<td><code>Mexico</code>, <code>United States</code></td>
<td>And</td>
</tr>
<tr>
<td>Known Bots</td>
<td>equals</td>
<td><code>false</code></td>
<td></td>
</tr>
</tbody>
</table>
<p>If you are using the expression editor:<br/>
<code>(ip.src.country in {&quot;US&quot; &quot;MX&quot;} and not cf.client.bot)</code></p>
<ul>
<li><strong>Then take action</strong>: <em>Managed Challenge</em></li>
</ul>
<h2 id="other-resources">Other resources</h2>
<ul>
<li><a href="/waf/custom-rules/use-cases/challenge-bad-bots/">Use case: Challenge bad bots</a></li>
<li><a href="/bots/">Cloudflare bot solutions</a></li>
<li><a href="/waf/troubleshooting/blocked-bing-site-scans/">Troubleshooting: Bing's Site Scan blocked by a WAF managed rule</a></li>
<li><a href="https://www.cloudflare.com/learning/bots/what-is-a-web-crawler/">Learning Center: What is a web crawler?</a></li>
</ul>
