<p>Microsoft <a href="https://www.bing.com/webmaster/tools">Bing Webmaster Tools</a> provides a Site Scan feature that crawls your website searching for possible SEO improvements.</p>
<p>Site Scan does not use the same IP address range as Bingbot (Bing's website crawler). Additionally, the <a href="https://www.bing.com/toolbox/verify-bingbot">Verify Bingbot</a> tool does not recognize Site Scan's IP addresses as Bingbot. Due to this reason, the WAF managed rule that blocks fake Bingbot requests may trigger for Site Scan requests. This is a known issue of Bing Webmaster Tools.</p>
<p>To allow Site Scan to run on your website, Cloudflare recommends that you temporarily skip the triggered WAF managed rule by creating an <a href="/waf/managed-rules/waf-exceptions/">exception</a>. After the scan finishes successfully, delete the exception to start blocking fake Bingbot requests again.</p>
<p>The rule you should temporarily skip is the following:</p>
<table>
<thead>
<tr>
<th></th>
<th>Name</th>
<th>ID</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Managed Ruleset</strong></td>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="efb7b8c949ac4650a09736fc376e9aee">376e9aee</code></td>
</tr>
<tr>
<td><strong>Rule</strong></td>
<td>Anomaly:Header:User-Agent - Fake Bing or MSN Bot</td>
<td><code class="nb-rule-id" title="ae20608d93b94e97988db1bbc12cf9c8">c12cf9c8</code></td>
</tr>
</tbody>
</table>
<p>The exception, shown as a rule with a <strong>Skip</strong> action, must appear in the rules list before the rule executing the Cloudflare Managed Ruleset, or else nothing will be skipped.</p>
<p>To check the rule order, use one of the following methods:</p>
<ul>
<li>When using the old Cloudflare dashboard, the rules listed in <strong>Security</strong> &gt; <strong>WAF</strong> &gt; <strong>Managed rules</strong> run in order.</li>
<li>When using the new security dashboard, the rules listed in <strong>Security</strong> &gt; <strong>Security rules</strong> run in order.</li>
<li>When using the Cloudflare API, the rules in the <code>rules</code> object obtained using the <a href="/api/resources/rulesets/subresources/phases/methods/get/">Get a zone entry point ruleset</a> operation (for your zone and for the <code>http_request_firewall_managed</code> phase) run in order.</li>
</ul>
<p>For more information on creating exceptions, refer to <a href="/waf/managed-rules/waf-exceptions/">Create exceptions</a>.</p>
