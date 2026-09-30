<p><a href="/cloudflare-one/access-controls/applications/http-apps/saas-apps/">Access for SaaS</a> functions as an identity proxy to add an additional authentication layer to your SaaS apps.</p>
<p>Access for SaaS integrates directly with your SaaS app using standard protocols (such as SAML) to become the primary enforcement point for user access. Access calls your identity provider (IdP) of choice and uses additional security signals about your users and devices to make policy decisions. Benefits of Access for SaaS include:</p>
<ul>
<li>A streamlined experience for users on both managed and unmanaged devices.</li>
<li>Application of baseline policies requiring specific concepts such as device posture and endpoint control.</li>
<li>Distinct access methodology for contractors.</li>
<li>Flexibility to configure multiple SSO vendors simultaneously, freely switch between SSO vendors, and reduce reliance on a single vendor.</li>
</ul>
<h3 id="sso-integrations">SSO integrations</h3>
<p>You can pair Access for SaaS with the <a href="/cloudflare-one/access-controls/access-settings/app-launcher/">App Launcher</a> to provide a full replacement to your organization's front door.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="scim-provisioning-limitation">SCIM provisioning limitation</h3>
@markup("md", "content/.markup/bodies/10037.md")
</aside>
<h2 id="configure-your-sso-provider">Configure your SSO provider</h2>
<p>If you cannot use Access for SaaS for some or all of your SaaS apps, you can accomplish most of the same outcomes through a combination of strong security controls on your managed devices and your <a href="/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/">Clientless Web Isolation</a> implementation. You can use your existing SSO provider to enforce a strong relationship between Cloudflare and your SaaS applications.</p>
<h3 id="policies-based-on-dedicated-egress-ips">Policies based on dedicated egress IPs</h3>
<p>With <a href="/cloudflare-one/traffic-policies/egress-policies/dedicated-egress-ips/">dedicated egress IPs</a>, you can set explicit egress locations globally and share these IPs with your SSO provider. With this Zero Trust security approach, your users must meet all of your Cloudflare requirements (such as being enrolled in the Cloudflare One Client or Browser Isolation) when they authenticate to your SSO provider. Using your dedicated egress IPs as a control mechanism within your SSO means you can set policies on the basis of which users are subject to security policy and inspection because they are guaranteed to be proxied through Cloudflare.</p>
<h3 id="generic-idp-multi-factor-authentication">Generic IdP multi-factor authentication</h3>
<p>Similar to the dedicated egress IP option, many IdPs support a generic multi-factor authentication (MFA) method. You can use your IdP's generic MFA in conjunction with Cloudflare security policies to make your second factor a Cloudflare Access policy. This policy can check all of the security signals available in Access for SaaS. This method delivers user traffic data to Cloudflare and ensures that users cannot access SaaS applications without first being subject to granular security policy.</p>
