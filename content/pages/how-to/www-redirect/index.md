<p>Learn how to redirect a <code>www</code> subdomain to your apex domain (<code>example.com</code>).</p>
<p>This setup assumes that you already have a <a href="/pages/configuration/custom-domains/">custom domain</a> attached to your Pages project.</p>
<h2 id="setup">Setup</h2>
<p>To redirect your <code>www</code> subdomain to your domain apex:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Bulk Redirects</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. [Create a bulk redirect list](/rules/url-forwarding/bulk-redirects/create-dashboard/#1-create-a-bulk-redirect-list) modeled after the following (but replacing the values as appropriate):
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@input("content/.markup/bodies/10884.md")
</div>
<ol start="4">
<li><a href="/rules/url-forwarding/bulk-redirects/create-dashboard/#2-create-a-bulk-redirect-rule">Create a bulk redirect rule</a> using the list you just created.</li>
<li>Go to <strong>DNS</strong>.</li>
<li><a href="/dns/manage-dns-records/how-to/create-dns-records/#create-dns-records">Create a DNS record</a> for the <code>www</code> subdomain using the following values:</li>
</ol>
<div class="nb-example"><h3 class="nb-component-title" id="example-1">Example</h3>
@input("content/.markup/bodies/10885.md")
</div>
<p>It may take a moment for this DNS change to propagate, but once complete, you can run the following command in your terminal.</p>
<pre><code class="language-sh">curl --head -i https://www.example.com/&#10;</code></pre>
<p>Then, inspect the output to verify that the <code>location</code> header and status code are being set as configured.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/pages/how-to/redirect-to-custom-domain/">Redirect <code>*.pages.dev</code> to a custom domain</a></li>
<li><a href="/rules/url-forwarding/bulk-redirects/">Handle redirects with Bulk Redirects</a></li>
</ul>
