<p>API tokens can be restricted at runtime in two ways:</p>
<ul>
<li><a href="#client-ip-address-range-filtering">Client IP address range filtering</a></li>
<li><a href="#time-to-live-ttl-constraints">Time To Live (TTL) constraints</a></li>
</ul>
<h2 id="client-ip-address-range-filtering">Client IP address range filtering</h2>
<p>Client IP address restrictions control which IP addresses can make API requests with this token. By default, if no filtering is applied, all IP addresses can use the token. Once an <code>Is in</code> rule is applied, the token can only be used from the defined IP addresses. Define ranges with <a href="https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation">CIDR notation</a>. To allow an IP range with exceptions, define <code>Is not in</code> to exempt specific IPs or smaller ranges.</p>
<p><img src="/assets/upstream/images/fundamentals/api/ip-filter.png" alt="IP Address filtering options" /></p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8978.md")
</aside>
<h2 id="time-to-live-ttl-constraints">Time to live (TTL) constraints</h2>
<p>By default, tokens do not expire and are long lived. Defining a TTL sets when a token starts being valid and when a token is no longer valid. This is often referred to as <code>notBefore</code> and <code>notAfter</code>. Setting these timestamps limits the lifetime of the token to the defined period. Not setting the start date or <code>notBefore</code> means the token is active as soon as it is created. Not setting the end date or <code>notAfter</code> means the token does not expire.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8977.md")
</aside>
<p><img src="/assets/upstream/images/fundamentals/api/ttl.png" alt="Time to Live selection calendar" /></p>
