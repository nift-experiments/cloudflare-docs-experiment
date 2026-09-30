<p><a href="/cloudflare-one/faq/">❮ Back to FAQ</a></p>
<h2 id="what-is-the-difference-between-cloudflare-gateway-and-1-1-1-1">What is the difference between Cloudflare Gateway and 1.1.1.1?</h2>
<p>1.1.1.1 does not block any DNS query. When a browser requests for example.com, 1.1.1.1 simply looks up the answer either in cache or by performing a full recursive DNS query.</p>
<p>Cloudflare Gateway's DNS resolver introduces security into this flow. Instead of allowing all DNS queries, Gateway first checks the hostname being queried against the intelligence Cloudflare has about threats on the Internet. If that query matches a known threat, or is requesting a blocked domain configured by an administrator as part of a Gateway policy, Gateway stops it before the site could load for the user - and potentially execute code or phish that team member.</p>
<h2 id="is-multi-factor-authentication-supported">Is multi-factor authentication supported?</h2>
<p>Access supports two methods of enforcing MFA:</p>
<ul>
<li><strong>Independent MFA</strong> — Access prompts users for a second factor directly, without relying on your identity provider. You can configure MFA requirements per organization, application, or policy. For more information, refer to <a href="/cloudflare-one/access-controls/policies/mfa-requirements/#independent-mfa">Enforce independent MFA</a>.</li>
<li><strong>Identity provider-based MFA</strong> — Access respects the <a href="/cloudflare-one/access-controls/policies/mfa-requirements/#identity-provider-based-mfa">MFA policies</a> set in your identity provider. For example, if your users are logging into an Access protected app through Okta, Okta would enforce an MFA check before sending the valid authentication confirmation back to Cloudflare Access.</li>
</ul>
<h2 id="which-browsers-are-supported">Which browsers are supported?</h2>
<p>These browsers are supported:</p>
<ul>
<li>Internet Explorer 11</li>
<li>Edge (current release, last release)</li>
<li>Firefox (current release, last release)</li>
<li>Chrome (current release, last release)</li>
<li>Safari (current release, last release)</li>
</ul>
<h2 id="what-languages-does-the-cloudflare-dashboard-support">What languages does the Cloudflare dashboard support?</h2>
<p>The Cloudflare dashboard is available in the following languages:</p>
<ul>
<li>Deutsch (German)</li>
<li>English</li>
<li>Español (Spanish)</li>
<li>Français (French)</li>
<li>Italiano (Italian)</li>
<li>日本語 (Japanese)</li>
<li>한국어 (Korean)</li>
<li>Português (Portuguese)</li>
<li>简体中文 (Mandarin Chinese, Simplified)</li>
<li>繁體中文 (Mandarin Chinese, Traditional)</li>
</ul>
<p>To change your dashboard language, refer to <a href="/fundamentals/user-profiles/customize-account/#language">Profile settings</a>.</p>
<h2 id="what-data-localization-services-are-supported">What data localization services are supported?</h2>
<p>Cloudflare Zero Trust can be used with the Data Localization Suite to ensure that traffic is only inspected in the regions you choose. For more information refer to <a href="/data-localization/how-to/zero-trust/">Use Zero Trust with Data Localization Suite</a>.</p>
