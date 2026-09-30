<p>The following Cloudflare Access policies are commonly used to secure applications.</p>
<p>Refer to the <a href="/cloudflare-one/access-controls/policies/">Access policies page</a> for a comprehensive list of available actions, rule types, and selectors. To learn how to create and manage policies, refer to <a href="/cloudflare-one/access-controls/policies/policy-management/">Manage Access policies</a>.</p>
<h2 id="allow-employees-by-email-domain">Allow employees by email domain</h2>
<p>The most basic Access policy grants access to anyone who authenticates with an email address belonging to your organization. This is a good starting point when you first protect an application with Access and want to restrict it to employees using your corporate <a href="/cloudflare-one/integrations/identity-providers/">identity provider</a>.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4608.md")
</div></div>
<p>You can add multiple email domains to the Include rule if your organization uses more than one domain (for example, <code>@example.com</code> and <code>@example.co.uk</code>).</p>
<h2 id="allow-employees-from-specific-countries">Allow employees from specific countries</h2>
<p>Organizations that operate in specific regions or need to comply with data residency requirements can restrict application access to users in approved countries. This policy is useful when you want to limit where employees can connect from, while still allowing exceptions for individual users such as traveling executives.</p>
<p>Because Require rules use AND logic, you cannot add multiple countries directly to a single Require rule — that would require the user to be in all countries simultaneously. Instead, first create a <a href="/cloudflare-one/access-controls/policies/groups/">rule group</a> that lists the approved countries:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4613.md")
</div></div>
<p>Then reference the rule group in your Access policy:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4618.md")
</div></div>
<h2 id="require-device-posture-for-sensitive-applications">Require device posture for sensitive applications</h2>
<p>For applications that contain sensitive data, you can verify that users connect from managed devices that meet your organization's security baseline. The following example combines identity verification with <a href="/cloudflare-one/reusable-components/posture-checks/">device posture checks</a> to ensure that the device is running a supported <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/os-version/">OS version</a> and is connected through the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a>, which is enforced by the <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/require-gateway/">Require Gateway check</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4603.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4623.md")
</div></div>
<p>To reuse these device requirements across multiple applications, create a <a href="/cloudflare-one/access-controls/policies/groups/">rule group</a> called &quot;Corporate device requirements&quot; that contains the posture checks. You can then reference this rule group in the Require field of any policy.</p>
<h2 id="require-mfa-for-high-security-applications">Require MFA for high-security applications</h2>
<p>For applications that handle financial data, production infrastructure, or other high-value resources, you can require that users authenticate with multi-factor authentication (MFA) in addition to their identity provider credentials. This ensures that a compromised password alone is not sufficient to gain access.</p>
<p>Access supports two approaches to enforcing MFA:</p>
<h3 id="identity-provider-based-mfa">Identity provider-based MFA</h3>
<p>If your identity provider reports the authentication method used during login, you can add an <strong>Authentication method</strong> selector to require a specific MFA method such as a hardware security key.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4628.md")
</div></div>
<h3 id="independent-mfa">Independent MFA</h3>
<p>If you want to enforce MFA directly in Access without relying on your IdP, you can use <a href="/cloudflare-one/access-controls/access-settings/independent-mfa/">independent MFA</a>. Independent MFA is not configured through policy selectors. Instead, you first <a href="/cloudflare-one/access-controls/access-settings/independent-mfa/#turn-on-independent-mfa">turn on independent MFA</a> at the organization level, then enable it for specific applications or policies through a settings panel. Access will prompt users for a second factor (such as a security key, authenticator app, or biometrics) after they authenticate with your IdP.</p>
<p>For the full details on both approaches, refer to <a href="/cloudflare-one/access-controls/policies/mfa-requirements/">Enforce MFA</a>.</p>
<h2 id="allow-contractor-access-with-email-based-authentication">Allow contractor access with email-based authentication</h2>
<p>When you collaborate with external contractors or partners who are not part of your corporate identity provider, you can grant them access using a <a href="/cloudflare-one/integrations/identity-providers/one-time-pin/">one-time PIN (OTP)</a>. OTP sends a short-lived code to the contractor's email address, allowing them to authenticate without needing an account in your IdP.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4602.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4633.md")
</div></div>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/4601.md")
</aside>
<h2 id="isolate-contractor-access-to-internal-applications">Isolate contractor access to internal applications</h2>
<p>When contractors or other external users need to view internal applications but should not be able to download, copy, or transfer data to their unmanaged devices, you can serve the application in a <a href="/cloudflare-one/remote-browser-isolation/">remote browser</a>. This gives external users read-only visibility into the application while keeping sensitive data from leaving your environment.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4600.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4639.md")
</div></div>
<p>To restrict what users can do inside the isolated session, create a companion <a href="/cloudflare-one/traffic-policies/http-policies/">Gateway HTTP policy</a> that matches traffic to the application domain. Set the action to <strong>Isolate</strong> and disable interactive controls in the <a href="/cloudflare-one/remote-browser-isolation/isolation-policies/#policy-settings">policy settings</a>.</p>
<details class="nb-details"><summary>Example Gateway HTTP policy</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/4640.md")
</div></details>
<p>For more information, refer to <a href="/cloudflare-one/access-controls/policies/isolate-application/">Isolate self-hosted application</a>.</p>
<h2 id="block-requests-from-high-risk-countries">Block requests from high-risk countries</h2>
<p>If your organization restricts access from certain countries due to internal policy or regulatory requirements such as <a href="https://orpa.princeton.edu/export-controls/sanctioned-countries">OFAC sanctions</a> or <a href="https://www.tradecompliance.pitt.edu/embargoed-and-sanctioned-countries">ITAR regulations</a>, you can create a Block policy that denies access from those regions. Adding a corporate IP allowlist as an Exclude rule ensures that employees connecting through trusted office networks are not inadvertently blocked.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4599.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4645.md")
</div></div>
<p>Block policies are best used together with <a href="#allow-employees-by-email-domain">Allow policies</a> to carve out exceptions. Because Access denies all requests by default, users who do not match a Block policy are still denied unless they match an Allow policy.</p>
<h2 id="exclude-high-risk-users">Exclude high-risk users</h2>
<p>If your organization uses <a href="/cloudflare-one/team-and-resources/users/risk-score/">Cloudflare User Risk Scores</a> to flag users with anomalous behavior, you can exclude high-risk users from accessing sensitive applications. This is useful as a dynamic safeguard that automatically restricts access when a user's behavior triggers a risk level change, without requiring manual intervention.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4650.md")
</div></div>
<p>In this example, any user scored as high risk is excluded even if they match the Include rule. To learn how risk scores are calculated and how to configure risk behaviors, refer to <a href="/cloudflare-one/team-and-resources/users/risk-score/">User risk score</a>.</p>
<h2 id="authenticate-a-service-using-a-service-token">Authenticate a service using a service token</h2>
<p>Automated services such as CI/CD pipelines, monitoring systems, and backend APIs need to access protected applications without an interactive login. Service Auth policies allow machine-to-machine communication by authenticating requests that present valid <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/">service token</a> headers. For additional security, you can restrict the token to requests from specific IP ranges, ensuring the token can only be used from known infrastructure.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4598.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4655.md")
</div></div>
<h2 id="authenticate-a-service-using-mutual-tls">Authenticate a service using mutual TLS</h2>
<p>For environments that require certificate-based authentication, you can use <a href="/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/">mutual TLS (mTLS)</a> to verify that a connecting client presents a valid certificate with an expected identity. mTLS is useful for authenticating automated systems and IoT devices that do not use an identity provider, or as an additional authentication factor for team members who also log in through an IdP.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4597.md")
</aside>
<p>To restrict access to a specific client, use the <strong>Common Name</strong> selector to match the identity in the client certificate:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4660.md")
</div></div>
<p>To allow any client presenting a valid certificate signed by your CA, use the <strong>Valid Certificate</strong> selector. This selector is useful when you trust all certificates issued by your CA and do not need to check a specific Common Name.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4665.md")
</div></div>
<h2 id="require-purpose-justification-for-sensitive-applications">Require purpose justification for sensitive applications</h2>
<p>For applications such as database admin tools, production consoles, or HR systems, you can require users to provide a written reason each time they access the application. This creates an audit trail that helps security teams understand why access was requested. The justification prompt appears after the user authenticates and before they reach the application. For more information, refer to <a href="/cloudflare-one/access-controls/policies/require-purpose-justification/">Require purpose justification</a>.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4670.md")
</div></div>
<p>You can combine purpose justification with <a href="/cloudflare-one/access-controls/policies/temporary-auth/">temporary authentication</a> to additionally require approval from a designated reviewer before granting access.</p>
<h2 id="bypass-a-public-endpoint">Bypass a public endpoint</h2>
<p>Some applications have endpoints that must be publicly reachable, such as OAuth callback URLs, webhook receivers, or health check paths. You can create a Bypass policy scoped to a specific <a href="/cloudflare-one/access-controls/policies/app-paths/">application path</a> to disable Access enforcement for that endpoint only. For example, if your application is <code>app.example.com</code>, you could create a separate Access application for <code>app.example.com/oauth/callback</code> and apply the following Bypass policy:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4675.md")
</div></div>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/4596.md")
</aside>
