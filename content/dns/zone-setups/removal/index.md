<p>If domains on Free zones remain in the <a href="/dns/zone-setups/reference/domain-status/#pending">Pending</a> or <a href="/dns/zone-setups/reference/domain-status/#moved">Moved</a> status for too long, Cloudflare automatically removes them from your account and the Cloudflare network. Refer to <a href="/dns/zone-setups/reference/domain-status/">zone statuses</a> for more details.</p>
<p>You can also <a href="/fundamentals/manage-domains/remove-domain/">manually remove a domain</a> from Cloudflare.</p>
<p>If you need to re-add a domain to your account, follow the <a href="/fundamentals/manage-domains/add-site/">regular onboarding flow</a>. Cloudflare will assign a new nameserver pair when you re-add the domain, so you must <a href="/dns/nameservers/update-nameservers/">update your registrar</a> with the new nameservers. Refer to <a href="/dns/nameservers/nameserver-options/#assignment-method">nameserver assignment</a> for details.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="purged-zones">Purged zones</h3>
@markup("md", "content/.markup/bodies/7551.md")
</aside>
