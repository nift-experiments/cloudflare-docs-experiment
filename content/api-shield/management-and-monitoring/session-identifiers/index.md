<p>While not strictly required, it is recommended that you configure your <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/3214.md")
</div> when getting started with API Shield. When Cloudflare inspects your API traffic for individual sessions, we can offer more tools for visibility, management, and control.
<p>If you are unsure of the session identifiers that your API uses, consult with your development team.</p>
<p>Session identifiers should uniquely identify API clients. A common session identifier for API traffic is the <code>Authorization</code> header. When a <a href="/api-shield/security/jwt-validation/">JSON Web Token (JWT)</a> is used by the API for client authentication, its value may change over time. You can use a claim value inside the JWT such as <code>sub</code> or <code>email</code> as a session ID to uniquely identify the session over time.</p>
<p>If your API uses the <code>Authorization</code> header on more than 1% of successful requests to your zone, Cloudflare will automatically set it as the API Shield session identifier.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3213.md")
</aside>
<h2 id="to-set-up-session-identifiers">To set up session identifiers</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3215.md")
</div>
<p>After setting up session identifiers and allowing some time for Cloudflare to learn your traffic patterns, you can view your per endpoint and per session rate limiting recommendations, as well as enforce per endpoint and per session rate limits by creating new rules. Session identifiers will allow you to view API Discovery results from session ID-based discovery and session traffic patterns in Sequence Analytics.</p>
