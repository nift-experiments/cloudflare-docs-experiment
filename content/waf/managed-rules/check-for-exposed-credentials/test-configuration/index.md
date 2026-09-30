<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="deprecation-notice">Deprecation notice</h3>
@markup("md", "content/.markup/bodies/15645.md")
</aside>
<p>After enabling and configuring exposed credentials checks, you may want to test if the checks are working properly.</p>
<p>Cloudflare provides a special set of case-sensitive credentials for this purpose:</p>
<ul>
<li>Login: <code>CF_EXPOSED_USERNAME</code> or <code>CF_EXPOSED_USERNAME@example.com</code></li>
<li>Password: <code>CF_EXPOSED_PASSWORD</code></li>
</ul>
<p>The WAF always considers these specific credentials as having been previously exposed. Use them to force an &quot;exposed credentials&quot; event, which allows you to check the behavior of your current configuration.</p>
