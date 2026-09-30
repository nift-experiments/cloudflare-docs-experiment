<p>Use import and export to have more control over your DNS records and make processes like migrating a domain or bulk editing <a href="/dns/manage-dns-records/reference/record-attributes/">record comments</a> easier.</p>
<h2 id="import-records">Import records</h2>
<h3 id="limits">Limits</h3>
<ul>
<li></li>
</ul>
<p>The zone file size limit is 256 KiB (262144 bytes).</p>
<ul>
<li>The API rate limit is three requests per minute per user.</li>
</ul>
<h3 id="format-your-zone-file">Format your zone file</h3>
<p>Create a <a href="https://en.wikipedia.org/wiki/Zone_file">BIND zone file</a> for your domain. If you need help, use a <a href="https://pgl.yoyo.org/as/bind-zone-file-creator.php">third-party tool</a>.</p>
<p>If you are using certain record types — for example, <code>CNAME</code>, <code>DNAME</code>, <code>MX</code>, <code>NS</code>, <code>PTR</code>, or <code>SRV</code> records — make sure that the <strong>content</strong> of those records contains fully qualified domain names ending in a trailing period (as in <code>example.com.</code>). For more details, refer to <a href="https://www.rfc-editor.org/rfc/rfc1035#section-5.1">RFC 1035</a> or this <a href="https://superuser.com/questions/348282/fqdn-format-in-bind-zone#348284">post on Stack Exchange</a>.</p>
<h3 id="import-zone-file-to-cloudflare">Import zone file to Cloudflare</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7823.md")
</div></div>
<hr />
<h2 id="export-records">Export records</h2>
<p>You can also bulk export records from Cloudflare.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7826.md")
</div></div>
<hr />
<h2 id="dns-record-attributes">DNS record attributes</h2>
<p>When exporting or importing a zone file, Cloudflare formats <a href="/dns/manage-dns-records/reference/record-attributes/">comments and tags</a> using the following structure, appending the attributes as inline comment using the <code>;</code> character after each record in accordance with <a href="https://datatracker.ietf.org/doc/html/rfc1035#section-5-1">RFC 1035 section 5</a>:</p>
<table>
<thead>
<tr>
<th>Combination</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Only tags</strong></td>
<td>Tag names contain a <a href="/dns/manage-dns-records/reference/record-attributes/#tags">small set</a> of characters.<br/><br/>Additionally, tag values must be contained by a double quote (<code>&quot;</code>) if they contain <code>&quot;</code>, <code>=</code>, <code>,</code>, or <code>\</code>. When enclosed within double quotes (<code>&quot;</code>), tag values are represented as JSON strings, so other quotes within the value can be escaped as <code>\&quot;</code>.<br/><br/>A tag with an empty value can be represented either as <code>my-tag-name:&quot;&quot;</code>, <code>my-tag-name:</code>, or <code>my-tag-name</code>.</td>
</tr>
<tr>
<td><strong>Only a comment</strong></td>
<td>Comments have <a href="/dns/manage-dns-records/reference/record-attributes/#comments">fewer limitations</a> on characters, meaning that the comment is included verbatim.<br/><br/>If the comment includes the string <code>cf_tags=</code>, you need to include an additional <code> cf_tags=</code> at the end of the line.</td>
</tr>
<tr>
<td><strong>Comment and tags</strong></td>
<td>The zone file comment would be of the form ; <code>&lt;comment&gt;</code> cf_tags=<code>&lt;tags&gt;</code>, as described above. Note the added space character before <code>cf_tags=</code>.</td>
</tr>
<tr>
<td><strong>Neither attribute</strong></td>
<td>The comment in the zone file may be empty or omitted entirely. Comments in the zone file that do not immediately follow a record are also ignored.</td>
</tr>
</tbody>
</table>
<pre><code class="language-txt">; Only tags&#10;a.example.com.  60  IN  A   1.1.1.1 ;   cf_tags=awesome&#10;b.example.com.  60  IN  A   1.1.1.1 ;   cf_tags=tag1,tag2:value2,tag3:&quot;value,with,commas&quot;,tag4:&quot;value with \&quot;escaped\&quot; quotation marks&quot;&#10;&#10;; Only a comment&#10;c.example.com.  60  IN  A   1.1.1.1 ; just a comment without tags&#10;d.example.com.  60  IN  A   1.1.1.1 ; this comment contains cf_tags= as text cf_tags=&#10;&#10;; Comments and tags&#10;e.example.com.  60  IN  A   1.1.1.1 ; simple example cf_tags=important,ticket:THIS-12345&#10;f.example.com.  60  IN  A   1.1.1.1 ; this is the comment cf_tags=tag1:value1,tag2:value2,tag-without-value,another-tag-without-value,tag-with-quoted-value:&quot;because of the comma, quotes are needed&quot;&#10;&#10;; Neither attribute&#10;g.example.com.  60  IN  A   1.1.1.1&#10;</code></pre>
<h3 id="reserved-cf-tags">Reserved cf- tags</h3>
<p>When exporting and importing, special tags starting by <code>cf-</code> allow you to control specific Cloudflare configurations. On export, these tags are automatically added to reflect the current configuration for each record on your zone.</p>
<pre><code class="language-txt">;; CNAME Records&#10;a.cloudflaredocs.com.	1	IN	CNAME	example.com. ; cf_tags=test:1,cf-flatten-cname&#10;b.cloudflaredocs.com.	1	IN	CNAME	example.com. ; cf_tags=cf-proxied:false&#10;c.cloudflaredocs.com.	1	IN	CNAME	example.com. ; cf_tags=tag-without-value,cf-proxied:true&#10;</code></pre>
<h4 id="cf-proxied">cf-proxied</h4>
<p>On export, <a href="/dns/proxy-status/">proxied DNS records</a> will present a tag <code>cf-proxied:true</code> while DNS-only records will have this tag set to <code>cf-proxied:false</code>.</p>
<p>When importing zone files, the value in the <code>cf-proxied</code> tag will take precedence in determining whether a record should be proxied. This means that:</p>
<ul>
<li>If the tag is present, its value will be considered for the respective record regardless of the <strong>Proxy imported DNS records</strong> option being selected (via dashboard), or the <code>proxied</code> parameter being generally set to <code>true</code> or <code>false</code> (via API).</li>
<li>If the tag is absent, the proxied status will fall back to the general import option, meaning <strong>Proxy imported DNS records</strong> selected or not (via dashboard) or the <code>proxied</code> parameter set to <code>true</code> or <code>false</code> (via API).</li>
</ul>
<h4 id="cf-flatten-cname">cf-flatten-cname</h4>
<p>If you are on a paid zone and want to use <a href="/dns/cname-flattening/set-up-cname-flattening/#per-record">Per-record CNAME flattening</a>, use the tag <code>cf-flatten-cname</code> next to each flattened CNAME record in your zone file. On export, this tag is automatically added to reflect the record configuration that you have on your zone.</p>
<h2 id="dns-zone-file-directives">DNS zone file directives</h2>
<p>A DNS zone file can be constructed using directives in addition to resource records (RRs). Directives start with <code>$</code> and are standardized - <code>$ORIGIN</code> and <code>$INCLUDE</code> are defined in <a href="https://www.rfc-editor.org/rfc/rfc1035#section-5.1">RFC 1035</a>, and <code>$TTL</code> is defined in <a href="https://www.rfc-editor.org/rfc/rfc2308">RFC 2308</a>. Additionally, BIND provides the <a href="https://bind9.readthedocs.io/en/latest/chapter3.html#bind-primary-file-extension-the-generate-directive">non-standard</a> <code>$GENERATE</code> directive.</p>
<p>Cloudflare supports <code>$ORIGIN</code>, <code>$TTL</code>, and <code>$GENERATE</code> directives.</p>
<p><code>$INCLUDE</code> is not supported. When a zone file contains a <code>$INCLUDE</code> directive, Cloudflare responds with a parsing error <code>$INCLUDE directive not allowed</code>.</p>
