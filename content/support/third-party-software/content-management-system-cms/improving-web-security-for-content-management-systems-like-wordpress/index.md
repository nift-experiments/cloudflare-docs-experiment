<p>Content Management Systems make it easy to create, update, and manage content. However, they can also introduce vulnerabilities that may lead to server compromise and data theft.</p>
<p>There are many Cloudflare features that can be used for preventing such attacks, but they can also disrupt normal administrative processes such as logging in or uploading images. With proper configuration, you can protect your site from attacks without losing important functionality.</p>
<hr />
<h2 id="stage-one-improve-site-security">Stage One: Improve Site Security</h2>
<p>In this stage, you are reinforcing the zone’s security features, which may cause additional disruption to admin features until exceptions can be applied. For that reason, it’s recommended to make these changes with expected administrative downtime.</p>
<p>The following should be considered an overview of some recommended security actions, and not a comprehensive guide. Refer to the developer documentation for specific products or features for more information.</p>
<h3 id="cloudflare-managed-rulesets">Cloudflare Managed Rulesets</h3>
<p>The <a href="/waf/managed-rules/">WAF Managed Rulesets</a> are pre-configured rulesets that provide immediate protection against a variety of attacks, and are regularly updated. Many rules are turned on by default, but not all. It is recommended that you browse the Cloudflare Managed Ruleset to find any additional rules tagged for your content management system not enabled, and enable them:</p>
<p><img src="/assets/upstream/images/support/Wordpress-configure-deployment.png" alt="Dashboard screenshot filtering for WordPress" /></p>
<h3 id="managed-rulesets-on-the-free-plan">Managed Rulesets on the Free Plan</h3>
<p>While the feature to customize these managed rulesets required a paid plan, the <a href="https://blog.cloudflare.com/waf-for-everyone/#the-free-cloudflare-managed-ruleset">Free Cloudflare Managed Ruleset</a> is automatically deployed on any new Cloudflare zone. This ruleset is specially designed to reduce false positives to a minimum across a very broad range of traffic types. As of today, the ruleset contains the following rules:</p>
<ul>
<li>Log4J rules matching payloads in the URI and HTTP headers;</li>
<li>Shellshock rules;</li>
<li>Rules matching very common WordPress exploits;</li>
</ul>
<p>Additionally, you can configure many aspects of the <a href="/waf/managed-rules/reference/owasp-core-ruleset/">OWASP Core Ruleset</a>, including the anomaly threshold, paranoia level, and individual rules. One good practice is to ensure any rules related to XSS and SQL injection are enabled.</p>
<hr />
<h2 id="stage-two-restore-administrative-functions">Stage Two: Restore Administrative Functions</h2>
<p>Using the principle of least privilege, you can run some test actions from the admin panel to audit what is blocked and what is allowed. With this information, you can create precise exceptions. If the behavior doesn’t match your expectations, make sure to check that:</p>
<ol>
<li>The DNS record is proxied</li>
<li>You don’t have any Rules that would interfere with the WAF (like a Page Rule that is set to Disable Security)</li>
</ol>
<p>After generating enough requests to have a good sample logged in your Firewall Events, observe the actions that were taken in the Managed rules section:</p>
<p><img src="/assets/upstream/images/support/Screenshot_2022-12-23_at_16.40.29.png" alt="" /></p>
<p>Next, you can use this information to create a Skip Rule that excludes only the rules that prevent administrative actions:</p>
<p><img src="/assets/upstream/images/support/Screenshot_2022-12-22_at_13.49.18.png" alt="" /></p>
<h3 id="when-incoming-requests-match">When incoming requests match…</h3>
<p>It is recommended to make this rule as tightly defined as possible, particularly without the additional protections listed below. While the exact content will be site-specific, some possible fields to use are:</p>
<ul>
<li>IP Source Address</li>
<li>AS Num</li>
<li>Cookie</li>
<li>User Agent</li>
</ul>
<p>Make sure to apply the rule <em>only</em> to the admin portion of your CMS. With WordPress for example, you can set a condition like '<em>URI Path contains /wp-admin/</em>'.</p>
<p>Any of these fields can be spoofed, so this is not a security measure on its own. The purpose is to restore administrative functions only to conditions that may need them, while using other tools and features (including strong passwords on your CMS logins!) to secure access.</p>
<h3 id="skip-specific-rules-from-a-managed-ruleset">Skip specific rules from a Managed Ruleset</h3>
<p>Next, you want to use the information from your Firewall logs to select which rules to skip by <a href="/waf/custom-rules/skip/">adding an exception</a>. For WordPress, I’ve chosen the following:</p>
<p><img src="/assets/upstream/images/support/Screenshot_2022-12-23_at_17.08.37.png" alt="" /></p>
<p>After this is complete, you will want to create a similar rule for any rulesets that prevent you from logging in. In my use case, I only needed to skip “OWASP Core Ruleset 949110.”</p>
<p><strong>Note:</strong> You may also want to consider adding a rule to skip the CMS-specific rules you enabled for non-CMS sections of your site if they cause any issues. Just follow the steps above, and set it to skip any of the Cloudflare Managed Ruleset rules that were enabled above. You can set this based on hostname, URI, or cookie, using the operators <strong>does not equal, does not match,</strong> or <strong>does not contain</strong>.</p>
<p>Make sure to set your Skip rules to be at a higher priority than the Execute rules.</p>
<hr />
<h2 id="stage-three-restrict-access">Stage Three: Restrict Access</h2>
<p>Now that you’ve elevated your security to protect the publicly accessible parts of your site against attacks and restored necessary administrative capabilities, you can further restrict who can access your admin panel in case of weak or exposed login credentials.</p>
<h3 id="zero-trust">Zero Trust</h3>
<p><a href="https://www.cloudflare.com/plans/zero-trust-services/">Zero Trust</a> Web Applications is the best way to limit access to your admin panel. You can restrict access based on user instead of device, and it allows for very granular control. Setup of a Self-hosted web application is very easy, for more information refer to the <a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">Self-hosted applications</a> section of the Zero Trust developer documentation.</p>
<p>After configuring a web application, users will be required to authenticate in some way before they can access the restricted content. The default method is through email multifactor authentication:</p>
<p><img src="/assets/upstream/images/support/Screenshot_2022-12-22_at_14.39.21.png" alt="" /></p>
<h3 id="waf-custom-rules-with-mtls">WAF custom rules with mTLS</h3>
<p>While designed for authenticating appliances that cannot perform a login, you can use mTLS as another method of multifactor authentication (what you know and what you have) to authenticate based on device certificate.</p>
<p>Do the following:</p>
<ol>
<li><a href="/ssl/client-certificates/create-a-client-certificate/">Create a client certificate</a> and save both the certificate and key to your device.</li>
<li>Import the certificate to your computer’s key storage. With macOS Keychain, you can use the steps listed in <a href="/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/#test-in-the-browser">Test in the browser</a>.</li>
<li><a href="/ssl/client-certificates/enable-mtls/">Enable mTLS</a> by adding the correct host.</li>
<li>In <strong>SSL/TLS</strong> &gt; <strong>Client Certificates</strong>, select <strong>Create mTLS Rule</strong>.</li>
<li>Under <strong>When incoming requests match</strong>, enter a value for the <strong>URI Path</strong> field to narrow the rule scope to the admin section, otherwise you will block your visitors from accessing the public content.</li>
<li>Set the rule to <em>Block</em> any requests made to your admin panel if the client certificate is not verified.</li>
<li>Select <strong>Deploy</strong>. This creates a WAF custom rule that checks all requests to the admin section for a valid client certificate.</li>
</ol>
<p><strong>Note:</strong> If you have issues getting your certificate to verify, try accessing the page in a private window. If it works, the previous successful TLS state may be cached in your browser.</p>
<h3 id="rate-limiting">Rate Limiting</h3>
<p>Rate limiting rules can help protect your login page from an attacker trying to guess your account password with a <a href="https://www.cloudflare.com/learning/bots/brute-force-attack/">brute force attack</a>. You can define rate limits for requests matching an expression, as well as the action to perform when those rate limits are reached.</p>
<p>Rate Limiting Rules are now available unmetered, on all plans. For more information, refer to the <a href="/waf/rate-limiting-rules/">developer documentation</a>.</p>
<hr />
<h2 id="resources">Resources</h2>
<ul>
<li><a href="/waf/managed-rules/">WAF Managed Rules</a></li>
<li><a href="/waf/managed-rules/reference/owasp-core-ruleset/">Cloudflare OWASP Core Ruleset</a></li>
<li><a href="/waf/custom-rules/skip/">Configure a custom rule with the Skip action</a></li>
<li><a href="https://www.cloudflare.com/plans/zero-trust-services/">Zero Trust Services</a></li>
<li><a href="/ssl/client-certificates/">Client certificates</a></li>
<li><a href="/waf/rate-limiting-rules/">Rate limiting rules</a></li>
</ul>
