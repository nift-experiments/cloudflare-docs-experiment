<p>An IP Access rule can perform one of the following actions:</p>
<ul>
<li>
<p><strong>Block</strong>: Prevents a visitor from visiting your site.</p>
</li>
<li>
<p><strong>Allow</strong>: Excludes visitors from all security checks, including <a href="/waf/tools/browser-integrity-check/">Browser Integrity Check</a>, <a href="/fundamentals/reference/under-attack-mode/">Under Attack mode</a>, and the WAF. Use this option when a trusted visitor is being blocked by Cloudflare's default security features. The <em>Allow</em> action takes precedence over the <em>Block</em> action.<br/>Allowing a given country code will not bypass WAF managed rules (previous and new versions). Refer to <a href="/waf/tools/ip-access-rules/#important-remarks-about-allowingblocking-by-country">Important remarks about allowing/blocking by country</a> for more information.</p>
</li>
<li>
<p><strong>Managed Challenge</strong>: Depending on the characteristics of a request, Cloudflare will dynamically choose the appropriate type of challenge from a list of possible actions. For more information, refer to <a href="/cloudflare-challenges/challenge-types/challenge-pages/#managed-challenge">Interstitial Challenge Pages</a>.</p>
</li>
<li>
<p><strong>Non-Interactive Challenge</strong>: Presents a non-interactive challenge page to visitors. Prevents bots from accessing the site.</p>
</li>
<li>
<p><strong>Interactive Challenge</strong>: Requires the visitor to complete an interactive challenge before visiting your site. Prevents bots from accessing the site.</p>
</li>
</ul>
