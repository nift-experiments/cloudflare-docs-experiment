<p>If you are using reCAPTCHA today, you can switch seamlessly to Cloudflare Turnstile by following the step-by-step guide below to assist with the upgrade process.</p>
<p>To complete the migration, you must obtain the <a href="/turnstile/get-started/widget-management/">sitekey and secret key</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15001.md")
</aside>
<h2 id="client-side-integration">Client-side integration</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15002.md")
</div>
<h2 id="server-side-integration">Server-side integration</h2>
<p>Update the server-side integration by replacing the Siteverify URL.</p>
<p>Replace <code>https://www.google.com/recaptcha/api/siteverify</code> with the following:</p>
<pre><code class="language-txt">https://challenges.cloudflare.com/turnstile/v0/siteverify&#10;</code></pre>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="differences-to-recaptcha-s-siteverify">Differences to reCAPTCHA's Siteverify</h3>
@markup("md", "content/.markup/bodies/14998.md")
</aside>
