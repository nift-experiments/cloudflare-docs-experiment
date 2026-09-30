<p>In the old Cloudflare dashboard, security level has the value <em>Always protected</em> and you cannot change this setting. To turn <a href="/fundamentals/reference/under-attack-mode/">Under Attack mode</a> on or off, use the separate toggle.</p>
<p>In the new security dashboard, the Cloudflare API, and in Terraform, use security level to turn Under Attack mode on or off.</p>
<p>Cloudflare's <a href="/fundamentals/reference/under-attack-mode/">Under Attack mode</a> performs additional security checks to help mitigate layer 7 DDoS attacks. When you enable Under Attack mode, Cloudflare will present a Managed Challenge page.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/15337.md")
</aside>
<h2 id="threat-score">Threat score</h2>
<p>Previously, a threat score represented a Cloudflare threat score from 0–100, where 0 indicates low risk. Now, the threat score is always <code>0</code> (zero).</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="recommendation">Recommendation</h3>
@markup("md", "content/.markup/bodies/15336.md")
</aside>
