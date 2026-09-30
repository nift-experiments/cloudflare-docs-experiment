<p>Many organizations in the past few years have recognized the importance of source-of-truth identity and have directly integrated their SSO provider with their internal applications. The SSO provider is only aware of the internal domain on which the application exists (via the configured ACS URL), which means the user must be connected to the local network in order to access the application. This security architecture makes sense for a traditional network perimeter, but it presents challenges for Zero Trust adoption. In the clientless access model, the user's device has no concept of an internal corporate network, only the specific, scoped applications to which they have access. The problem is summarized in the following diagram:</p>
<pre><code class="language-mermaid">flowchart LR&#10;accTitle: Authorization flow with integrated SSO&#10;A(&quot;User goes to&#10;app.public.com&quot;)--&gt;B(&quot;Cloudflare Tunnel&#10;routes public hostname (app.public.com)&#10;to internal domain (app.internal.com)&quot;)--&gt;C(&quot;app.internal.com redirects&#10;to integrated SSO&quot;)--&gt;D(&quot;SSO ACS URL returns&#10;app.internal.com&quot;)--&gt;E(&quot;404 error&#10;Device cannot resolve&#10;app.internal.com&quot;)&#10;</code></pre>
<h2 id="potential-solutions">Potential solutions</h2>
<p>If your applications use integrated SSO, there are a number of different paths you can take to onboard your applications to Cloudflare Access.</p>
<table>
<thead>
<tr>
<th>Solution</th>
<th>Steps required</th>
<th>Pros</th>
<th>Cons</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="#recommended-solution">Present applications exclusively on Cloudflare domains</a></td>
<td>Change SSO ACS URL to the Cloudflare Tunnel public hostname</td>
<td><li> Increased security posture </li> <li> No changes to application code</li> <li> No changes to internal DNS design </li></td>
<td>Hard cutover event when ACS URL changes from internal to external domain</td>
</tr>
<tr>
<td>Present applications on existing internal domains with identical external domains delegated to Cloudflare</td>
<td>Add domains to Cloudflare that match internal domains</td>
<td><li> No changes to SSO ACS URL </li> <li> No change for end users </li></td>
<td><li> Requires careful management of internal and external domains </li> <li> Requires changing internal DNS design </li></td>
</tr>
<tr>
<td><a href="/learning-paths/clientless-access/migrate-applications/consume-jwt/">Consume the Cloudflare JWT in internal applications</a></td>
<td><li> Remove integrated SSO </li> <li> Update application to accept the Cloudflare JWT for user authorization </li></td>
<td><li> Reduced authentication burden for end users </li> <li> No changes to internal DNS design </li> <li> Instantly secure applications without direct SSO integration </li></td>
<td><li> Requires changing application code </li> <li> Hard cutover event when application updates </li></td>
</tr>
<tr>
<td>Use Cloudflare as the direct SSO integration, which then calls your IdP of choice (Okta, OneLogin, etc.)</td>
<td>Swap existing SSO provider for <a href="/cloudflare-one/access-controls/applications/http-apps/saas-apps/">Access for SaaS</a></td>
<td><li> Increased flexibility for changing IdPs </li> <li> Ability to use multiple IdPs simultaneously </li></td>
<td><li> Hard cutover event for IdP changes </li> <li> No SCIM provisioning for application </li></td>
</tr>
</tbody>
</table>
<h2 id="recommended-solution">Recommended solution</h2>
<p>If you are able to configure your SSO provider, we recommend presenting all internal web services exclusively on Cloudflare domains. This is the model that Cloudflare takes for web application access internally and the most common method of resolution for customers in this scenario.</p>
<p>With this approach, you do not need to make any changes to your existing DNS infrastructure. Cloudflare Tunnel in your network will manage the translation from external (Cloudflare public) DNS to internal DNS, which is how the system is designed to function. After you update the ACS URL in your SSO provider to the Cloudflare public hostname, the outcome will look like this:</p>
<pre><code class="language-mermaid">flowchart LR&#10;accTitle: Authorization flow with updated SSO ACS URL&#10;A(&quot;User goes to&#10;app.public.com&quot;)--&gt;B(&quot;Cloudflare Tunnel&#10;routes public hostname (app.public.com)&#10;to internal domain (app.internal.com)&quot;)--&gt;C(&quot;app.internal.com redirects&#10;to integrated SSO&quot;)--&gt;D(&quot;SSO ACS URL returns&#10;app.public.com&quot;)--&gt;E(&quot;Browser displays app.public.com&quot;)&#10;</code></pre>
<p>All users - whether in the office, remote, using or not using the VPN client - will always route through the Cloudflare Access authentication flow at <code>app.public.com</code> to access a private application. This provides a single control plane for policy application and security audits, and no additional user training is necessary.</p>
