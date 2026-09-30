<p>This tutorial will instruct you how to configure an origin rule and a DNS record to point to an R2 bucket configured with a custom domain.</p>
<p>The procedure will use the following example values:</p>
<table>
<thead>
<tr>
<th align="right"></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td align="right">URL that website visitors will access</td>
<td><code>mycustomerexample.com/images/*</code></td>
</tr>
<tr>
<td align="right">R2 bucket custom domain</td>
<td><code>imagesbucket.example.com</code></td>
</tr>
</tbody>
</table>
<p>When configuring your R2 bucket's custom domain, use a custom domain that you do not plan to use in production (<code>imagesbucket.example.com</code> in this example).</p>
<h2 id="1-configure-custom-domain-in-your-pages-project"><ol>
<li>Configure custom domain in your Pages project</li>
</ol></h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/13068.md")
</div>
<p>Your domain is now connected. The status takes a few minutes to change from <strong>Initializing</strong> to <strong>Active</strong>, and you may need to refresh to review the status update. If the status has not changed, select the <strong>...</strong> next to your bucket and select <strong>Retry connection</strong>.</p>
<p>To view the added DNS record, select <strong>...</strong> next to the connected domain and select <strong>Manage DNS</strong>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13067.md")
</aside>
<h2 id="2-create-origin-rule-to-rewrite-host-header-and-override-dns-record"><ol start="2">
<li>Create origin rule to rewrite host header and override DNS record</li>
</ol></h2>
<p>In your <code>mycustomerexample.com</code> zone, create an origin rule with the following configuration:</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/13069.md")
</div>
<h2 id="3-optional-configure-url-rewrite"><ol start="3">
<li>(Optional) Configure URL rewrite</li>
</ol></h2>
<p>In our example, the URL that website visitors will access starts with <code>/images</code>. However, images stored in the example R2 bucket do not have this initial URL segment.</p>
<p>Use a URL rewrite to remove the <code>/images</code> segment from the URL path. Cloudflare provides a rule template in the dashboard called <strong>Rewrite Path for Object Storage Bucket</strong> that you can use to configure the required rewrite.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/13070.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13066.md")
</aside>
<h2 id="more-resources">More resources</h2>
<ul>
<li><a href="/rules/origin-rules/tutorials/change-uri-path-and-host-header/">Tutorial: Change URI Path and Host Header</a></li>
<li><a href="/r2/buckets/public-buckets/">Cloudflare R2: Public buckets</a></li>
<li><a href="/dns/manage-dns-records/">DNS records</a></li>
</ul>
