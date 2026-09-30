<p>Learn how to use <a href="/rules/url-forwarding/bulk-redirects/">Bulk Redirects</a> to redirect your <code>*.pages.dev</code> subdomain to your <a href="/pages/configuration/custom-domains/">custom domain</a>.</p>
<p>You may want to do this to ensure that your site's content is served only on the custom domain, and not the <code>&lt;project&gt;.pages.dev</code> site automatically generated on your first Pages deployment.</p>
<h2 id="setup">Setup</h2>
<p>To redirect a <code>&lt;project&gt;.pages.dev</code> subdomain to your custom domain:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select your Pages project.
3. Go to **Custom domains** and make sure that your custom domain is listed. If it is not, add it by clicking **Set up a custom domain**.
4. Go **Bulk Redirects**.
5. [Create a bulk redirect list](/rules/url-forwarding/bulk-redirects/create-dashboard/#1-create-a-bulk-redirect-list) modeled after the following (but replacing the values as appropriate):
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@input("content/.markup/bodies/10891.md")
</div>
<ol start="6">
<li><a href="/rules/url-forwarding/bulk-redirects/create-dashboard/#2-create-a-bulk-redirect-rule">Create a bulk redirect rule</a> using the list you just created.</li>
</ol>
<p>To test that your redirect worked, go to your <code>&lt;project&gt;.pages.dev</code> domain. If the URL is now set to your custom domain, then the rule has propagated.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/pages/how-to/www-redirect/">Redirect www to domain apex</a></li>
<li><a href="/rules/url-forwarding/bulk-redirects/">Handle redirects with Bulk Redirects</a></li>
</ul>
