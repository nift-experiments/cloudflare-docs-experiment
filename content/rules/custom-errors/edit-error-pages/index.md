<p>You can define custom <a href="/rules/custom-errors/#error-pages">Error Pages</a> for the following errors and challenges:</p>
<ul>
<li>WAF block</li>
<li>IP/Country block</li>
<li>IP/Country challenge</li>
<li>500 class errors</li>
<li>1000 class errors</li>
<li>Managed challenge / I'm Under Attack Mode</li>
<li>Rate limiting block</li>
</ul>
<p>For more information on the different types of Error Pages, refer to <a href="/rules/custom-errors/reference/error-page-types/">Error page types</a>.</p>
<p>To return custom error responses for requests that match specific conditions, use <a href="/rules/custom-errors/#custom-error-rules">Custom Error Rules</a> instead.</p>
<h2 id="1-design-your-custom-error-page"><ol>
<li>Design your custom error page</li>
</ol></h2>
<p>Before defining a custom error page in your Cloudflare account, you will need to design and code that page. It can be hosted on your own web server or using a Cloudflare product like <a href="/rules/snippets/">Snippets</a>.</p>
<p>When designing your custom error page, you can include page-specific <a href="/rules/custom-errors/reference/error-tokens/">custom error tokens</a>. Each custom error token provides diagnostic information that appears on the error page.</p>
<p>To display a custom page for each error, create a separate page per error. For example, to create a custom error page for both <strong>IP/Country Block</strong> and <strong>WAF block</strong>, you must design and publish two separate pages.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="notes">Notes</h3>
@markup("md", "content/.markup/bodies/12991.md")
</aside>
<p>You can use the following template to start building your error page:</p>
<pre><code class="language-html">&lt;html&gt;&#10;	&lt;head&gt;&lt;/head&gt;&#10;	&lt;body&gt;&#10;		::[REPLACE WITH CUSTOM ERROR TOKEN NAME]::&#10;	&lt;/body&gt;&#10;&lt;/html&gt;&#10;</code></pre>
<details class="nb-details"><summary>Example error page for 5XX errors</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/12992.md")
</div></details>
<hr />
<h2 id="2-update-an-error-page-in-the-dashboard"><ol start="2">
<li>Update an error page in the dashboard</li>
</ol></h2>
<p>You can define an error page at the zone level or for your entire account. Zone-level error pages have priority over account-level error pages.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/12997.md")
</div></div>
<h2 id="fetch-custom-error-page-again">Fetch custom error page again</h2>
<p>After successfully setting the content of the custom error page in <strong>Error Pages</strong>, you can remove the page from your origin server.</p>
<p>If in the future, you need to update your custom error page, you must fetch the page again, even if the page URL remains unchanged. In this case, next to the page type you want to update, select the three dots &gt; <strong>Fetch custom page again</strong>.</p>
