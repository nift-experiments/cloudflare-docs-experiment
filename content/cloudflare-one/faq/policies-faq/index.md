<p><a href="/cloudflare-one/faq/">❮ Back to FAQ</a></p>
<h2 id="what-is-the-order-of-policy-enforcement">What is the order of policy enforcement?</h2>
<p>Gateway and Access policies generally trigger from top to bottom based on their position in the policy table in the UI. Exceptions include Bypass and Service Auth policies, which Access evaluates first. Similarly, for Gateway HTTP policies, Do Not Inspect and Isolate policies take precedence over all Allow or Block policies. To learn more about order of enforcement, refer to our documentation for <a href="/cloudflare-one/access-controls/policies/#order-of-execution">Access policies</a> and <a href="/cloudflare-one/traffic-policies/order-of-enforcement/">Gateway policies</a>.</p>
<h2 id="how-can-i-bypass-the-l7-firewall-for-a-website"><strong>How can I bypass the L7 firewall for a website?</strong></h2>
<p>Cloudflare Gateway uses the hostname in the HTTP <code>CONNECT</code> header to identify the destination of the request. Administrators who wish to bypass a site must create a <a href="/cloudflare-one/traffic-policies/http-policies/#do-not-inspect">Do Not Inspect</a> policy in order to prevent HTTP inspection from occurring on both encrypted and plaintext traffic.</p>
<p>Bypassing the L7 firewall results in no HTTP traffic inspection, and logging is disabled for that HTTP session.</p>
<h2 id="can-i-secure-applications-with-a-second-level-subdomain-url">Can I secure applications with a second-level subdomain URL?</h2>
<p>Yes. Ensure that your SSL certificates cover the first- and second-level subdomain. Most certificates only cover the first-level subdomain and not the second. This is true for most Cloudflare certificates. To cover a second-level subdomain with a CF certificate, create an <a href="/ssl/edge-certificates/advanced-certificate-manager/manage-certificates/">advanced certificate</a>.</p>
<p>Wildcard-based policies in Cloudflare Access only cover the level where they are applied. Add the wildcard policy to the left-most subdomain to be covered.</p>
<h2 id="how-do-isolation-policies-work-together-with-http-policies">How do isolation policies work together with HTTP policies?</h2>
<p>Isolation policies, like all HTTP policies, are evaluated in stages. When a user makes a request which evaluates an Isolation policy, the request will be rerouted to an isolated browser and re-evaluated for HTTP policies. This makes it possible for an isolated browser to remotely render a block page, or have malicious content within the isolated browser blocked by HTTP policies.</p>
<h2 id="why-is-api-or-cli-traffic-not-isolated">Why is API or CLI traffic not isolated?</h2>
<p>Isolation policies are applied to requests that include <code>Accept: text/html*</code>. This allows Browser Isolation policies to co-exist with API and command line requests.</p>
<h2 id="can-access-enforce-policies-on-a-specific-nonstandard-port">Can Access enforce policies on a specific nonstandard port?</h2>
<p>No. Cloudflare Access cannot enforce a policy that would contain a port appended to the URL. However, you can use Cloudflare Tunnel to point traffic to non-standard ports. For example, if Jira is available at port <code>8443</code> on your origin, you can proxy traffic to that port via Cloudflare Tunnel.</p>
<h2 id="why-can-i-still-reach-domains-blocked-by-a-gateway-policy">Why can I still reach domains blocked by a Gateway policy?</h2>
<p>If the domain is blocked by a DNS, network, or HTTP policy, it may be because:</p>
<ul>
<li><strong>Your policy is still being updated.</strong> After you edit or create a policy, Cloudflare updates the new setting across all of our data centers around the world. It takes about 60 seconds for the change to propagate.</li>
</ul>
<p>If the domain is only blocked by a DNS policy, it may be because:</p>
<ul>
<li>
<p><strong>Your device is using another DNS resolver.</strong> If you have other DNS resolvers in your DNS settings, your device could be using IP addresses for resolvers that are not part of Gateway. As a result, the domain you are trying to block is still accessible from your device. Make sure to remove all other IP addresses from your DNS settings and only include Gateway's DNS resolver IP addresses.</p>
</li>
<li>
<p><strong>Your policy is not assigned to a DNS location.</strong> If your policy is not assigned to a DNS location and you send a DNS query from that location, Gateway will not apply that policy. Assign a policy to a DNS location to make sure the desired policy is applied when you send a DNS query from that location.</p>
</li>
<li>
<p><strong>Your DoH endpoint is not a Gateway DNS location</strong>. Browsers can be configured to use any DoH endpoint. If you chose to configure DoH directly in your browser, make sure that the DoH endpoint is a Gateway DNS location.</p>
</li>
</ul>
<p>If the domain is only blocked by a network policy, it may be because:</p>
<ul>
<li><strong>Your browser is reusing an existing connection</strong>. Network policies only apply when a connection is opened. If a browser is connected to a domain to be blocked by a network policy, Gateway will not block requests until the connection is closed. To block the domain, close any related tabs or restart your browser.</li>
</ul>
<h2 id="when-does-access-return-a-forbidden-status-page-versus-a-login-page">When does Access return a Forbidden status page versus a login page?</h2>
<p>Access returns a Forbidden page with status codes <code>401</code>/<code>403</code> when it determines there is no way a user can pass a <a href="/cloudflare-one/access-controls/policies/">policy</a>. If Cloudflare can make a full policy determination that a user will not be able to log in, Access will return a Forbidden page instead of a <a href="/cloudflare-one/reusable-components/custom-pages/access-login-page/">login page</a>.</p>
<p>For example, your application has a policy that requires a user to be in a <a href="/cloudflare-one/access-controls/policies/#allow">specific geolocation</a> to log in.</p>
<p>As admin, you could define this geolocation policy by using <a href="/cloudflare-one/access-controls/policies/#include">Include</a> rules, meaning the user could log in to the application from Country A or Country B.</p>
<p>Or you could define this geolocation policy using a <a href="/cloudflare-one/access-controls/policies/#require">Require</a> rule, meaning the user must be in Country A to log in.</p>
<p>If a user from country C attempts to access the application, in both the Include and Require scenarios, the user will receive the Forbidden page. This is because Country C was not defined in either scenario. Therefore, Cloudflare has determined that this user cannot meet policy requirements and will receive the Forbidden status page.</p>
