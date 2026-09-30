<h2 id="renew-custom-certificates">Renew custom certificates</h2>
<p>Since Cloudflare cannot renew uploaded certificates, you should ensure that you replace or <a href="/ssl/edge-certificates/custom-certificates/uploading/#update-or-renew-an-existing-custom-certificate">update</a> an expiring custom certificate before it expires, otherwise your visitors may not be able to connect.</p>
<p>Cloudflare automatically sends email notifications 30 and 14 days before your custom certificate expires. The email is sent to users who have the SSL/TLS, Administrator, or Super Administrator <a href="/fundamentals/manage-members/roles/">roles</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14089.md")
</aside>
<h2 id="expired-certificates">Expired certificates</h2>
<p>If a valid replacement - covering some or all of the <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/14090.md")
</div> in the expiring custom certificate - is already available, Cloudflare will remove the expiring custom certificate in the 24 hours before expiration. There is no expected downtime due to certificate transition.
<p>If no valid replacement is available, Cloudflare will remove the custom certificate after it expires.</p>
<p>Affected domains and subdomains will fall back to any other active certificate covering the hostnames on the expiring certificate.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/14088.md")
</aside>
<h2 id="migrate-to-other-certificate-types">Migrate to other certificate types</h2>
<p>If you no longer want to use your custom certificate but still want your website or application to be covered with SSL/TLS, you can do the following:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Edge Certificates</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Make sure there is already an active <a href="/ssl/edge-certificates/universal-ssl/">universal</a> or <a href="/ssl/edge-certificates/advanced-certificate-manager/">advanced</a> certificate covering the same hostnames.</li>
<li>Delete your custom certificate.</li>
</ol>
