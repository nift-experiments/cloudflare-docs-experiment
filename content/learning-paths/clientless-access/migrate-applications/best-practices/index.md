<p>Most customers have a heterogeneous private application portfolio; some are home-built, some are internal managed services, some have SSO integrations available, and some rely on HTML or other forms of authentication. With that in mind, we recommend that you mix-and-match <a href="/learning-paths/clientless-access/migrate-applications/integrated-sso/#potential-solutions">onboarding solutions</a> to fit the needs of each individual application. As shown in the table below, you can bucket applications into a series of stack-ranked categories that prioritize ease of implementation and total organizational impact.</p>
<table>
<thead>
<tr>
<th>Application type</th>
<th>Recommendation</th>
<th>Outcome</th>
</tr>
</thead>
<tbody>
<tr>
<td>Private web apps without integrated SSO</td>
<td><a href="/learning-paths/clientless-access/migrate-applications/integrated-sso/#recommended-solution">Present applications exclusively on Cloudflare domains.</a></td>
<td>Users access applications on new domains delegated to Cloudflare and instantly apply SSO through Cloudflare integration.</td>
</tr>
<tr>
<td>Private web apps with integrated SSO</td>
<td><strong>If SSO configuration is possible:</strong> <a href="/learning-paths/clientless-access/migrate-applications/integrated-sso/#recommended-solution">Present applications exclusively on Cloudflare domains.</a> <br/> <strong>If SSO configuration is not possible:</strong> Present applications on existing internal domains with identical external domains delegated to Cloudflare</td>
<td>Users access internal web services on the same or new domains from Cloudflare. If configured, the SSO provider transparently redirects users from internal domains to Cloudflare authoritative external domains.</td>
</tr>
<tr>
<td>New critical internal applications being developed</td>
<td><a href="/learning-paths/clientless-access/migrate-applications/integrated-sso/#recommended-solution">Present applications exclusively on Cloudflare domains.</a></td>
<td>Developers can programmatically generate (or be given) new public hostnames on Cloudflare to represent the redirects for their application in SAML or OIDC integrations.</td>
</tr>
<tr>
<td>New microservices being developed</td>
<td><a href="/learning-paths/clientless-access/migrate-applications/integrated-sso/#recommended-solution">Present applications exclusively on Cloudflare domains.</a> <br/> Optionally, <a href="/learning-paths/clientless-access/migrate-applications/consume-jwt/#consume-the-cloudflare-jwt">consume the Access JWT</a> as authentication in internal applications.</td>
<td>Developers can inject the JWT authorization mechanism directly into the codebase of their application and <a href="/learning-paths/clientless-access/terraform/">use Terraform</a> to automatically build Cloudflare hostnames and policies for their applications.</td>
</tr>
<tr>
<td>Internal API endpoints (including internal applications with dependencies on external/internal APIs)</td>
<td>Present internal APIs on Cloudflare domains, and build Access policies that accept <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/">service tokens</a> alongside user-oriented policies.</td>
<td>Automated systems can authenticate via a <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/#connect-your-service-to-access">service token in the request header</a>, while end users continue to login through their IdP.</td>
</tr>
</tbody>
</table>
