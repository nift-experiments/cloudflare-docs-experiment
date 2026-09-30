<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 15, 2026</time><h2 id="post-title">WAF Release - 2026-05-15 - Emergency</h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This emergency release introduces two new rules to detect nginx heap buffer overflow and heap spray exploitation attempts targeting the rewrite module's <code>is_args</code> stale-state bug (CVE-2026-42945).</p>
<p><strong>Key Findings</strong></p>
<p>CVE-2026-42945: nginx Heap Buffer Overflow via Stale <code>is_args</code> in Rewrite Module</p>
<p>Successful exploitation allows remote attackers to trigger a heap buffer overflow in nginx's rewrite module by sending crafted URIs containing escapable characters. A length/copy pass mismatch in <code>ngx_http_script_copy_capture_code()</code> causes the copy pass to write escaped data into an undersized buffer, leading to heap corruption. This enables denial of service (worker process crash) and, with heap feng shui techniques, potential remote code execution.</p>
<p>We strongly recommend upgrading to nginx 1.30.1 (or later) immediately to address the underlying vulnerability. If you cannot upgrade immediately, avoid <code>rewrite</code> directives with <code>?</code> in the replacement string followed by <code>set</code> or <code>if</code> referencing capture groups.</p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="2013e3e58efe4b79a26e214f7e52be73">7e52be73</code>
</td>
<td>N/A</td>
<td>nginx - Remote Code Execution - Buffer Overread - CVE:CVE-2026-42945</td>
<td>N/A</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="68226e83a4d14ee9a9c878469df0ee6c">9df0ee6c</code>
</td>
<td>N/A</td>
<td>nginx - Remote Code Execution - Heap Spray - CVE:CVE-2026-42945</td>
<td>N/A</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
</tbody>
</table>
</div></article></div>
