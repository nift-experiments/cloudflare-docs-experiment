<p>A zone stays in <strong>Pending Nameserver Update</strong> when Cloudflare cannot confirm that your domain is delegated to the Cloudflare nameservers assigned to it.</p>
<p>The most common reasons are that the nameserver change was not fully published at the registrar, that the domain is not using the exact nameservers assigned to it, or that stale DNSSEC records at the registrar are blocking the delegation.</p>
<p>The rest of this page walks through what to check, in order, and shows how to verify each item independently of your registrar's control panel.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="partial-cname-setup">Partial (CNAME) setup</h3>
@markup("md", "content/.markup/bodies/7896.md")
</aside>
<p>For details on how zone status is evaluated, refer to <a href="/dns/zone-setups/reference/domain-status/">Zone status</a>.</p>
<h2 id="1-confirm-the-assigned-cloudflare-nameservers"><ol>
<li>Confirm the assigned Cloudflare nameservers</li>
</ol></h2>
<p>In the Cloudflare dashboard, open the domain and go to the <strong>Overview</strong> page. Copy the full list of nameservers Cloudflare has assigned to this zone. The number of nameservers and their hostname format depend on your setup:</p>
<table>
<thead>
<tr>
<th>Setup</th>
<th>Number of nameservers</th>
<th>Nameserver name format</th>
</tr>
</thead>
<tbody>
<tr>
<td>Standard <a href="/dns/zone-setups/full-setup/">full setup</a></td>
<td>2</td>
<td><code>&lt;proper_name&gt;.ns.cloudflare.com</code></td>
</tr>
<tr>
<td><a href="/dns/foundation-dns/">Foundation DNS</a> with <a href="/dns/foundation-dns/advanced-nameservers/#nameservers-hosting-and-assignment">advanced nameservers</a></td>
<td>3</td>
<td>One nameserver in each of <code>&lt;color&gt;.foundationdns.com</code>, <code>&lt;color&gt;.foundationdns.net</code>, and <code>&lt;color&gt;.foundationdns.org</code> — all three must be set at the registrar.</td>
</tr>
<tr>
<td><a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/">Cloudflare as Secondary DNS</a></td>
<td>2</td>
<td><code>&lt;proper_name&gt;.secondary.cloudflare.com</code></td>
</tr>
<tr>
<td><a href="/dns/nameservers/custom-nameservers/">Custom nameservers</a></td>
<td>Varies</td>
<td>Your own branded names</td>
</tr>
</tbody>
</table>
<p>Whichever format applies, the exact values shown in your dashboard are the ones the parent zone must publish. Do not assume the assignment is the same as one you have used before on another domain or in another account. For details, refer to <a href="/dns/nameservers/nameserver-options/#assignment-method">Nameserver assignments</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7895.md")
</aside>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7894.md")
</aside>
<h2 id="2-check-what-the-parent-zone-actually-publishes"><ol start="2">
<li>Check what the parent zone actually publishes</li>
</ol></h2>
<p>The registrar control panel shows what you <em>asked</em> the registrar to publish. It does not show what the parent zone (the TLD) is actually returning to the Internet. These can differ when a change was not saved, not yet propagated, applied to a different domain, or applied in a different registrar account.</p>
<p>Use one of the following methods to query the parent zone directly.</p>
<h3 id="option-a-dig-trace">Option A - <code>dig +trace</code></h3>
<p><code>dig +trace</code> follows the delegation from the root zone down. Adding <code>+noall +authority +nodnssec</code> trims the output to just the delegation section from each level, which is what you care about when checking where the parent zone points your domain. In a terminal, run:</p>
<pre><code class="language-sh">dig +trace example.com NS +noall +authority +nodnssec&#10;</code></pre>
<ul>
<li><code>+trace</code> — follows the delegation step by step, from the root nameservers down to your domain, instead of asking a single recursive resolver.</li>
<li><code>+noall +authority</code> — hides everything except the <strong>AUTHORITY</strong> section returned at each hop, which is where each parent zone lists the nameservers it delegates to. The last hop shown before your domain is the parent zone (<code>com.</code>, <code>co.uk.</code>, etc.), and its authority section is what actually delegates your zone.</li>
<li><code>+nodnssec</code> — hides DNSSEC-related records (<code>RRSIG</code>, <code>NSEC</code>, <code>NSEC3</code>, and DNSKEYs) so the output is easier to scan.</li>
</ul>
<p>The last non-empty section of the output should return <strong>only</strong> the Cloudflare nameservers assigned to your zone (or, if you use <a href="/dns/nameservers/nameserver-options/#multi-provider-dns">multi-provider DNS</a>, it should include them alongside your other provider's nameservers).</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7893.md")
</aside>
<h3 id="option-b-nslookup">Option B - <code>nslookup</code></h3>
<p>If you are on Windows or prefer <code>nslookup</code>, query the <code>NS</code> records for your domain. Add the <code>-debug</code> flag to see the full response, including the authority section. In a terminal, run:</p>
<pre><code class="language-sh">nslookup -type=ns -debug example.com&#10;</code></pre>
<p>By default, <code>nslookup</code> queries your system's configured resolver, which may return a cached answer. For a definitive check against the parent zone (equivalent to <code>dig +trace</code>), query a TLD nameserver directly by adding it as the last argument. For a <code>.com</code> domain, this looks like:</p>
<pre><code class="language-sh">nslookup -type=ns -debug example.com a.gtld-servers.net&#10;</code></pre>
<p>For other TLDs, refer to <a href="https://www.iana.org/domains/root/db">IANA's root zone database</a> to find the authoritative nameservers for your TLD.</p>
<p>If the output shows nameservers other than the ones assigned to your Cloudflare zone, the delegation is not yet correct.</p>
<h3 id="option-c-web-based-lookup">Option C - web-based lookup</h3>
<p>If you do not have <code>dig</code> or <code>nslookup</code> locally, use a public lookup tool:</p>
<ul>
<li><a href="https://www.digwebinterface.com/">digwebinterface.com</a> - enable the <strong>Trace</strong> option to follow the delegation from the root zone down, which is the equivalent of <code>dig +trace</code>.</li>
<li><a href="https://www.whatsmydns.net/">whatsmydns.net</a> - useful to see the <code>NS</code> record as observed from resolvers in multiple regions.</li>
</ul>
<p>Query the <code>NS</code> record for your domain. The result must match the nameservers assigned in your Cloudflare dashboard.</p>
<h3 id="what-to-do-based-on-the-result">What to do based on the result</h3>
<p>Use the following table to decide the next step based on what your lookup returns:</p>
<table>
<thead>
<tr>
<th>Result at the parent zone</th>
<th>What it means and what to do</th>
</tr>
</thead>
<tbody>
<tr>
<td>Exactly the Cloudflare nameservers assigned to this zone.</td>
<td>Delegation is correct. If the dashboard still shows Pending, wait for Cloudflare's next activation check or <a href="/api/resources/zones/subresources/activation_check/methods/trigger/">trigger one via API</a>. Then continue at Step 4 to check DNSSEC.</td>
</tr>
<tr>
<td>Cloudflare nameservers, but different names than the ones assigned.</td>
<td>The domain is likely added to a different Cloudflare account, or you set your registrar to nameservers you had previously used. Set the registrar to the exact values displayed on this zone's Overview page. For Foundation DNS advanced nameservers, all three values must be set.</td>
</tr>
<tr>
<td>Nameservers from a different provider.</td>
<td>The registrar has not published your change. Continue at Step 3.</td>
</tr>
<tr>
<td>No nameservers returned.</td>
<td>The domain is not yet delegated. If it was just registered, wait for the parent TLD to propagate (up to 24 hours), then retest.</td>
</tr>
<tr>
<td>Cloudflare and other-provider nameservers together.</td>
<td>Only valid if your setup uses <a href="/dns/nameservers/nameserver-options/#multi-provider-dns">multi-provider DNS</a>. Otherwise, remove the non-Cloudflare records at the registrar.</td>
</tr>
</tbody>
</table>
<h2 id="3-verify-the-change-was-actually-saved-at-the-registrar"><ol start="3">
<li>Verify the change was actually saved at the registrar</li>
</ol></h2>
<p>If the parent zone does not return the correct Cloudflare nameservers, the registrar has not published your change. Common patterns:</p>
<ul>
<li>The nameserver change was entered in the registrar UI but not saved or submitted.</li>
<li>The change was made on a different domain, on a subdomain, or in a different registrar account.</li>
<li>The domain is under a <strong>Transfer</strong>, <strong>Registrar Lock</strong>, or <strong>Redemption</strong> state that prevents nameserver changes. Complete or cancel the pending state first.</li>
<li>The registrar requires an additional confirmation step (email confirmation, admin approval, two-factor prompt).</li>
<li>The registrar publishes changes on a delay. Ask your registrar's support for their expected propagation window.</li>
<li>Your domain is at a reseller and the nameserver setting must be changed one level up. Refer to <a href="/dns/nameservers/update-nameservers/#specific-processes">Update your nameservers at your registrar</a>.</li>
</ul>
<p>After fixing the change at the registrar, re-run the check from Step 2.</p>
<h2 id="4-check-for-stale-dnssec-ds-records"><ol start="4">
<li>Check for stale DNSSEC DS records</li>
</ol></h2>
<p>If Step 2 shows the correct Cloudflare nameservers at the parent zone but the zone is still Pending, check whether DNSSEC is still enabled from a previous DNS provider.</p>
<p>DS records live at the registrar, not at the DNS provider, and they must be removed or updated when you move DNS providers. If they are not, the DNSSEC chain of trust breaks and resolvers return SERVFAIL for your domain.</p>
<p>To check for DS records:</p>
<pre><code class="language-sh">dig DS example.com&#10;</code></pre>
<p>If DS records are returned and you did not intentionally configure DNSSEC on Cloudflare, they are stale from your previous provider and will block activation.</p>
<p>To remove them:</p>
<ol>
<li>Sign in to your registrar's control panel.</li>
<li>Find DNSSEC settings (often under <strong>Advanced DNS</strong> or <strong>Security</strong>).</li>
<li>Remove all existing DS records.</li>
<li>Wait up to 24 hours for the removal to propagate through DNS caches.</li>
</ol>
<p>After the stale DS records are removed and expire from cache, your Cloudflare zone will activate automatically. You can then <a href="/dns/dnssec/">enable DNSSEC in Cloudflare</a> if you want to.</p>
<p>For more information on DNSSEC configuration, refer to <a href="/dns/dnssec/">Configure DNSSEC</a> and <a href="/dns/dnssec/troubleshooting/">Troubleshoot DNSSEC</a>.</p>
<h2 id="5-if-the-zone-is-still-pending"><ol start="5">
<li>If the zone is still Pending</li>
</ol></h2>
<p>If Steps 1-4 all check out, and the parent zone returns the correct Cloudflare nameservers, wait for Cloudflare's next activation check. Checks happen on an increasing interval.</p>
<p>You can request an earlier check from the <strong>Overview</strong> page or by <a href="/api/resources/zones/subresources/activation_check/methods/trigger/">triggering one via API</a>. This endpoint is rate-limited and may return an error if you have requested a check recently. A successful request does not activate the zone immediately — it places your zone in a prioritized queue, and activation can take a few minutes to a few hours, depending both on when the recheck runs and on whether the nameserver change at your registrar has taken effect by then.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7892.md")
</aside>
<p>If the parent zone matches, DS records are clean, and the zone still does not activate after several rechecks, <a href="/support/contacting-cloudflare-support/">contact Cloudflare Support</a> and include:</p>
<ul>
<li>Your domain name.</li>
<li>The Cloudflare nameservers assigned in the dashboard.</li>
<li>The output of <code>dig +trace &lt;YOUR_DOMAIN&gt; NS</code>.</li>
<li>The output of <code>dig DS &lt;YOUR_DOMAIN&gt;</code>.</li>
<li>The registrar you use.</li>
</ul>
