<p>Cloudflare Gateway gives you multiple ways to safely handle your employees' personally identifiable information (PII) in activity logs:</p>
<ul>
<li><strong>Redact PII</strong> (default) — PII is stored in logs but hidden from view. Only the Super Administrator and users with the <a href="/cloudflare-one/roles-permissions/#cloudflare-zero-trust-pii">Cloudflare Zero Trust PII role</a> can view redacted PII. The underlying data is preserved — redaction only controls who can see it.</li>
<li><strong><a href="#exclude-pii">Exclude PII</a></strong> — PII is not stored in logs at all. No user, including the Super Administrator, can retrieve it.</li>
</ul>
<p>Only the Super Administrator can assign roles and determine who has permission to view PII. To add or remove the Cloudflare Zero Trust PII role for a user in your organization, refer to <a href="/fundamentals/manage-members/roles/">Roles</a>.</p>
<h2 id="types-of-pii">Types of PII</h2>
<p>Cloudflare Gateway can log the following types of PII:</p>
<ul>
<li>Source IP</li>
<li>User email</li>
<li>User ID</li>
<li>Device ID</li>
<li>URL</li>
<li>Referer</li>
<li>User agent</li>
</ul>
<h2 id="exclude-pii">Exclude PII</h2>
<p>When you exclude PII, Gateway logs activity without storing any employee PII. This differs from the default redaction behavior — excluded PII is not stored and cannot be retrieved by any role, including the Super Administrator.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/4987.md")
</aside>
<p>Changes to this setting do not affect PII already stored in previous logs.</p>
<p>To turn on the setting to exclude PII:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Traffic policies</strong> &gt; <strong>Traffic settings</strong>.</li>
<li>In <strong>Traffic logging</strong>, turn on <strong>Exclude personally identifiable information (PII) from logs</strong>.</li>
</ol>
