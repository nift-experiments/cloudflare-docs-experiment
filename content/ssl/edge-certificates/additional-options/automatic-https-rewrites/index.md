<p>Automatic HTTPS Rewrites prevents end users from seeing &quot;mixed content&quot; errors by rewriting URLs from <code>http</code> to <code>https</code> for resources or links on your web site that can be served with HTTPS.</p>
<h2 id="availability">Availability</h2>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Availability</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<h2 id="additional-details">Additional details</h2>
<p>If your site contains links or references to HTTP URLs that are also available securely via HTTPS, Automatic HTTPS Rewrites can help. If you connect to your site over HTTPS and the lock icon is not present, or has a yellow warning triangle on it, your site may contain references to HTTP assets (“mixed content”).</p>
<p>Mixed content is often due to factors not under the website owner’s control such as embedded third-party content or complex content management systems. By rewriting URLs from “http” to “https”, Automatic HTTPS Rewrites simplifies the task of making your entire website available over HTTPS, helping to eliminate mixed content errors and ensuring that all data loaded by your website is protected from eavesdropping and tampering.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14147.md")
</aside>
<h2 id="enable-automatic-https-rewrites">Enable Automatic HTTPS Rewrites</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14150.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14146.md")
</aside>
<h2 id="limitations">Limitations</h2>
<p>Before a rewrite is applied, Cloudflare checks the HTTP resources to ensure they are accessible via HTTPS. If they are not available over HTTPS, Cloudflare cannot rewrite the URL.</p>
<p>Some resources are loaded by JavaScript or CSS via HTTP when the site is loaded in a browser. You will see mixed content warnings in those situations. To determine which URLs do not have HTTPS support, Cloudflare uses data from <a href="https://www.eff.org/https-everywhere/faq#how-do-i-add-my-own-site-to-https-everywhere">EFF’s HTTPS Everywhere</a> and <a href="https://hstspreload.org">Chrome’s HSTS preload list</a>. If your zone is not on one of these lists, only active content will be rewritten. Passive content (such as images) will not be rewritten and will still cause mixed content errors.</p>
<p>If a third-party domain supports HTTPS and is not rewritten automatically, you can manually change those links to relative links or HTTPS links. Alternatively, you can ask the third-party domain owner to submit their site for inclusion in the HTTPS Everywhere rulesets, which <a href="https://github.com/EFForg/https-everywhere/">accept pull requests on GitHub</a>. For more information on how to fix mixed content errors, refer to <a href="/ssl/troubleshooting/mixed-content-errors/">Troubleshooting mixed content errors</a>.</p>
