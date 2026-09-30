<div class="nb-description">
@markup("md", "content/.markup/bodies/1530.md")
</div>
<div class="nb-plan">
<p>Enterprise-only paid add-on</p>
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1529.md")
</aside>
<h2 id="why-care-about-api-security">Why care about API security?</h2>
<p>APIs have become the <a href="https://blog.postman.com/intro-to-apis-history-of-apis/">backbone of popular web services</a>, helping the Internet become more accessible and useful.</p>
<p>As APIs have become more prevalent, however, so have their problems:</p>
<ul>
<li>Many companies have <a href="/api-shield/security/api-discovery/">thousands of APIs</a>, including ones they do not even know about.</li>
<li>To support a large base of users, many APIs are protected by a negative security model that makes them vulnerable to credential-stuffing attacks and automated scanning tools.</li>
<li>With so many endpoints and users, it is difficult to recognize brute-force attacks against <a href="/api-shield/security/volumetric-abuse-detection/">specific endpoints</a>.</li>
<li>Sophisticated attacks are even harder to recognize, often because even development teams are unaware of common and uncommon <a href="/api-shield/security/sequence-analytics/">usage patterns</a>.</li>
</ul>
<p>Refer to the <a href="/api-shield/get-started/">Get started</a> guide to set up API Shield.</p>
<h2 id="features">Features</h2>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/1531.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/1532.md")
</div>
<h2 id="use-schema-profiles">Use Schema Profiles</h2>
<p><a href="/waf/detections/application-profiles/">Application Profiles</a> provides a shared detection, analytics, and mitigation model. Schema Profile is its only current profile type.</p>
<p>API Shield provides two Schema Profile sources. <a href="/api-shield/management-and-monitoring/endpoint-management/schema-learning/">Schema Learning</a> learns from traffic, while <a href="/api-shield/security/schema-validation/">Schema Validation</a> uses uploaded OpenAPI schemas.</p>
<p>Use API Shield for API inventory, OpenAPI governance, profile export, automation, and higher-scale API workflows. Use the WAF Application Profiles pages for Profile Analysis and Custom Rule enforcement.</p>
<h2 id="availability">Availability</h2>
<p>Cloudflare API Security products are available to Enterprise customers only. Anyone can set up <a href="/api-shield/security/mtls/">Mutual TLS</a> with a Cloudflare-managed certificate authority.</p>
<p>The full API Shield security suite is available as an Enterprise paid add-on. Refer to <a href="/api-shield/plans/">API Shield plans</a> for feature-specific availability.</p>
<p>Customers with API Security already have access to Schema Profiles through Schema Learning and Schema Validation. Cloudflare is opening a closed beta to invited Enterprise customers without API Security. Interested customers can contact their account team to express interest. Closed beta access does not imply future plan availability or pricing.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1528.md")
</aside>
<h2 id="related-products">Related products</h2>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/1533.md")
</div>
