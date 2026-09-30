<p>This tutorial will instruct you how to configure an origin rule and a DNS record to point to a Pages deployment with a custom domain.</p>
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
<td><code>mycustomerexample.com/blog/*</code></td>
</tr>
<tr>
<td align="right">Zone domain</td>
<td><code>mycustomerexample.com</code></td>
</tr>
<tr>
<td align="right">Cloudflare Pages subdomain</td>
<td><code>myblog.pages.dev</code></td>
</tr>
<tr>
<td align="right">Cloudflare Pages custom domain</td>
<td><code>blogmirror.example.com</code></td>
</tr>
</tbody>
</table>
<p>When configuring your Pages custom domain, use a custom domain that you do not plan to use in production (<code>blogmirror.example.com</code> in this example).</p>
<h2 id="1-configure-custom-domain-in-your-pages-project"><ol>
<li>Configure custom domain in your Pages project</li>
</ol></h2>
<p>To add the custom domain to your Pages deployment:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/13072.md")
</div>
<p>When you add the custom domain to your Pages deployment, Cloudflare automatically creates a <code>CNAME</code> DNS record for the custom domain.</p>
<h2 id="2-create-origin-rule-to-rewrite-host-header-and-override-dns-record"><ol start="2">
<li>Create origin rule to rewrite host header and override DNS record</li>
</ol></h2>
<p>In your <code>mycustomerexample.com</code> zone, create an origin rule with the following configuration:</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/13073.md")
</div>
<h2 id="3-optional-configure-url-rewrite"><ol start="3">
<li>(Optional) Configure URL rewrite</li>
</ol></h2>
<p>In this example, the URL that website visitors will access starts with <code>/blog</code>. However, the Pages deployment does not have this initial URL segment.</p>
<p>Use a URL rewrite to remove the <code>/blog</code> segment from the URL path.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/13074.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13071.md")
</aside>
<h2 id="more-resources">More resources</h2>
<ul>
<li><a href="/rules/origin-rules/tutorials/change-uri-path-and-host-header/">Tutorial: Change URI Path and Host Header</a></li>
<li><a href="/pages/configuration/custom-domains/">Cloudflare Pages: Custom domains</a></li>
<li><a href="/dns/manage-dns-records/">DNS records</a></li>
</ul>
