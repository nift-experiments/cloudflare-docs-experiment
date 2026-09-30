<aside class="nb-aside note">
<h3 class="nb-aside-title" id="availability">Availability</h3>
@markup("md", "content/.markup/bodies/8024.md")
</aside>
<p><a href="/dns/zone-setups/subdomain-setup/">Subdomain setup</a> relies on a process known as delegation. When, in a parent domain such as <code>example.com</code>, an <a href="https://www.cloudflare.com/learning/dns/dns-records/dns-ns-record/">NS record</a> is created for a subdomain <code>blog.example.com</code>, this means that DNS management for the subdomain can be done separately, in its own <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/8025.md")
</div>.
<pre><code class="language-mermaid">    flowchart TD&#10;      accTitle: Example of parent zone and subdomains&#10;      A[&lt;code&gt;example.com&lt;/code&gt;] --&gt; B[&lt;code&gt;docs.example.com&lt;/code&gt;]&#10;      A[&lt;code&gt;example.com&lt;/code&gt;] --&gt; C[&lt;code&gt;blog.example.com&lt;/code&gt;]&#10;      subgraph Parent domain&#10;        A&#10;      end&#10;      subgraph Subdomains&#10;        B&#10;        C&#10;      end&#10;</code></pre>
<hr />
<h2 id="available-setups">Available setups</h2>
<p>When configuring a subdomain setup, its availability will depend on both the parent zone setup and the setup used for the child zone. A child zone holds DNS management for a delegated subdomain.</p>
<table>
<thead>
<tr>
<th>Parent zone</th>
<th>Child zone</th>
<th>Available</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/dns/zone-setups/full-setup/">Full</a> or <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/">Secondary</a></td>
<td><a href="/dns/zone-setups/full-setup/">Full</a></td>
<td>Yes</td>
</tr>
<tr>
<td><a href="/dns/zone-setups/full-setup/">Full</a> or <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/">Secondary</a></td>
<td><a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/">Secondary</a></td>
<td>Yes</td>
</tr>
<tr>
<td><a href="/dns/zone-setups/full-setup/">Full</a> or <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/">Secondary</a></td>
<td><a href="/dns/zone-setups/partial-setup/">Partial</a></td>
<td>No</td>
</tr>
<tr>
<td><a href="/dns/zone-setups/partial-setup/">Partial</a></td>
<td><a href="/dns/zone-setups/full-setup/">Full</a></td>
<td>Yes</td>
</tr>
<tr>
<td><a href="/dns/zone-setups/partial-setup/">Partial</a></td>
<td><a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/">Secondary</a></td>
<td>Yes</td>
</tr>
<tr>
<td><a href="/dns/zone-setups/partial-setup/">Partial</a></td>
<td><a href="/dns/zone-setups/partial-setup/">Partial</a></td>
<td>Yes</td>
</tr>
</tbody>
</table>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="subdomain-zones-in-partial-setup-are-not-delegated">Subdomain zones in partial setup are not delegated</h3>
@markup("md", "content/.markup/bodies/8023.md")
</aside>
<p>This table assumes zones that are in an <a href="/dns/zone-setups/reference/domain-status/">active status</a>. For example, if you need to add the parent zone to Cloudflare when its child zone already exists in a CNAME setup (partial), you can <a href="/dns/zone-setups/partial-setup/setup/#1-convert-your-zone-and-review-dns-records">convert the parent zone to a CNAME setup (partial)</a> while it is still in pending status.</p>
<hr />
<h2 id="how-to">How to</h2>
<p>Refer to the following guides to learn how to configure a subdomain setup depending on the setup used for the parent zone:</p>
<ul class="directory-listing"><li><a href="/dns/zone-setups/subdomain-setup/setup/parent-on-full/">Parent zone on full setup</a></li><li><a href="/dns/zone-setups/subdomain-setup/setup/parent-on-partial/">Parent zone on partial setup</a></li></ul>
<p>Although the how-to guides in this documentation are focused on both parent domains and subdomains existing in Cloudflare, it is also possible to achieve a subdomain setup in Cloudflare while the parent domain exists in a different DNS provider.</p>
<hr />
<h2 id="ssl-tls-certificates">SSL/TLS certificates</h2>
<p>When using subdomain setup, you should consider possible interactions between parent zone and child zone configurations that could impact <a href="/ssl/">SSL/TLS certificates</a> provisioning.</p>
<p>If a certificate is already active on the child zone for a specific hostname (<code>subdomain.example.com</code>), any certificate pack containing that exact hostname in the parent zone (<code>example.com</code>) will fail validation.</p>
<h2 id="access-applications">Access applications</h2>
<p>To use subdomain setups with <a href="/cloudflare-one/access-controls/policies/">Cloudflare Access</a>, note that:</p>
<ul>
<li>
<p>If the child zone is in a pending state when you create the Access application, your configuration will not automatically apply when you activate the zone. You must also re-save the Access application once your subdomain setup is active.</p>
</li>
<li>
<p>If you split out a subdomain which already has an Access application, you will also need to re-save the Access application to associate it with the new child zone.</p>
</li>
</ul>
