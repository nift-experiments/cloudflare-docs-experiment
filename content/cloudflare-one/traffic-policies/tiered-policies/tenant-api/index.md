<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6402.md")
</aside>
<p>Gateway supports the <a href="/tenant/">Cloudflare Tenant API</a>, which allows Cloudflare-partnered managed service providers (MSPs) to set up and manage Cloudflare accounts and services for their customers. With the Tenant API, MSPs can create Zero Trust deployments with global Gateway policy control. Policies can be customized or overridden at a group or individual account level.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/6401.md")
</aside>
<p>For more information, refer to the <a href="https://blog.cloudflare.com/gateway-managed-service-provider/">Cloudflare Zero Trust for managed service providers</a> blog post.</p>
<h2 id="get-started">Get started</h2>
<p>To set up the Tenant API, refer to <a href="/tenant/get-started/">Get started</a>. Once you have provisioned and configured your customer's Cloudflare accounts, you can create <a href="/cloudflare-one/traffic-policies/dns-policies/">DNS policies</a>.</p>
<h2 id="account-types">Account types</h2>
<p>The Gateway Tenant platform supports tiered and siloed account configurations.</p>
<h3 id="tiered-accounts">Tiered accounts</h3>
<p>In a tiered account configuration, a top-level parent account enforces global security policies that apply to all of its child accounts. Child accounts can override or add policies as needed while still being managed by the parent account. MSPs can also configure child accounts independently from the parent account for the following Gateway features:</p>
<ul>
<li><strong><a href="/cloudflare-one/reusable-components/custom-pages/gateway-block-page/">Custom block page</a></strong>: Child accounts will use the block page setting used by the parent account unless you configure separate block settings for the child account. This applies to both redirects and custom block pages. The block page uses the account certificate for each child account.</li>
<li><strong><a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/">Root certificates</a></strong>: If Gateway cannot attribute an incoming DNS query to a child account, it will use the parent account's certificate. This happens when the source IP address of the DNS query does not match a child account or if a custom DNS resolver endpoint is not configured.</li>
<li><strong><a href="/cloudflare-one/networks/resolvers-and-proxies/dns/locations/">DNS locations</a></strong></li>
<li><strong><a href="/cloudflare-one/reusable-components/lists/">Lists</a></strong></li>
</ul>
<p>Each child account is subject to the default Zero Trust <a href="/cloudflare-one/account-limits/">account limits</a>.</p>
<p>Gateway evaluates parent account policies before any child account policies. To allow a child account to override a specific parent account policy, you can use the <a href="/api/resources/zero_trust/subresources/gateway/subresources/rules/methods/update/">Update a Zero Trust Gateway rule</a> endpoint to set the policy's <code>allow_child_bypass</code> rule setting to <code>true</code>.</p>
<pre><code class="language-mermaid">flowchart TD&#10;%% Accessibility&#10; accTitle: How Gateway policies work in a tiered account configuration&#10; accDescr: Flowchart describing the order of precedence Gateway applies policies in a tiered account configuration.&#10;&#10;%% Flowchart&#10; subgraph s1[&quot;Parent account&quot;]&#10;        n1[&quot;Block malware&quot;]&#10;        n2[&quot;Block DNS tunnel&quot;]&#10;        n3[&quot;Block spyware&quot;]&#10;  end&#10; subgraph s2[&quot;Child account A&quot;]&#10;        n4[&quot;Block social media&quot;]&#10;  end&#10; subgraph s3[&quot;Child account B&quot;]&#10;        n5[&quot;Block instant messaging&quot;]&#10;  end&#10;    n1 ~~~ n2&#10;    n2 ~~~ n3&#10;    A[&quot;Tenant&quot;] --Administers--&gt; s1&#10;    s1 -- &quot;Applies policies to&quot; --&gt; s2 &amp; s3&#10;&#10;    n1@{ shape: lean-l}&#10;    n2@{ shape: lean-l}&#10;    n3@{ shape: lean-l}&#10;    n4@{ shape: lean-l}&#10;    n5@{ shape: lean-l}&#10;</code></pre>
<h3 id="siloed-accounts">Siloed accounts</h3>
<p>In a siloed account configuration, each account operates independently within the same tenant. MSPs manage each account's own security policies, resources, and configurations separately.</p>
<pre><code class="language-mermaid">flowchart TD&#10;%% Accessibility&#10; accTitle: How Gateway policies work in a siloed account configuration&#10; accDescr: Flowchart describing the order of precedence Gateway applies policies in a siloed account configuration.&#10;&#10;%% Flowchart&#10; subgraph s1[&quot;Siloed account A&quot;]&#10;        n1[&quot;Block social media&quot;]&#10;  end&#10; subgraph s2[&quot;Siloed account C&quot;]&#10;        n2[&quot;Block instant messaging&quot;]&#10;  end&#10; subgraph s3[&quot;Siloed account B&quot;]&#10;        n3[&quot;Block news&quot;]&#10;  end&#10;    A[&quot;Tenant&quot;] -- Administers --&gt; s1 &amp; s3 &amp; s2&#10;&#10;    n1@{ shape: lean-l}&#10;    n2@{ shape: lean-l}&#10;    n3@{ shape: lean-l}&#10;</code></pre>
