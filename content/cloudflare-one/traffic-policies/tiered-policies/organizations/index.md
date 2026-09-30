<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6406.md")
</aside>
<p>Gateway supports using <a href="/fundamentals/organizations/">Cloudflare Organizations</a> to share configurations between and apply specific policies to accounts within an Organization. Tiered Gateway policies with Organizations support <a href="/cloudflare-one/traffic-policies/dns-policies/">DNS</a>, <a href="/cloudflare-one/traffic-policies/network-policies/">network</a>, <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP</a>, and <a href="/cloudflare-one/traffic-policies/resolver-policies/">resolver</a> policies.</p>
<p>For a DNS-only deployment using the Tenant API, refer to <a href="/cloudflare-one/traffic-policies/tiered-policies/tenant-api/">Tenant API</a>.</p>
<h2 id="get-started">Get started</h2>
<p>To set up Cloudflare Organizations, refer to <a href="/fundamentals/organizations/#create-an-organization">Create an Organization</a>. Once you have provisioned and configured your Organization's accounts, you can create <a href="/cloudflare-one/traffic-policies/">Gateway policies</a>.</p>
<h2 id="account-types">Account types</h2>
<p>Zero Trust accounts in Cloudflare Organizations include source accounts and recipient accounts.</p>
<p>In a tiered policy configuration, a top-level source account can share Gateway policies with its recipient accounts. Recipient accounts can add policies as needed while still being managed by the source account. Organization owners can also configure a <a href="/cloudflare-one/reusable-components/custom-pages/gateway-block-page/">custom block page</a> for recipient accounts independently from the source account. Gateway will automatically <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/#generate-a-cloudflare-root-certificate">generate a unique root CA</a> for each recipient account in an Organization.</p>
<p>Each recipient account is subject to the default Zero Trust <a href="/cloudflare-one/account-limits/">account limits</a>.</p>
<p>Gateway evaluates source account policies before any recipient account policies. Shared policies always take priority in recipient accounts — recipient accounts cannot bypass, modify, or reorder shared policies, and cannot move any of their own policies above shared ones. If you update the relative priority of shared policies in the source account, the change will be reflected in recipient accounts within approximately two minutes.</p>
<p>All traffic and corresponding policies, logs, and configurations for a recipient account will be contained to that recipient account. Organization owners can view logs for recipient accounts on a per-account basis, and <a href="/logs/logpush/">Logpush jobs</a> must be configured separately. When using DLP policies with <a href="/cloudflare-one/data-loss-prevention/dlp-policies/logging-options/#log-the-payload-of-matched-rules">payload logging</a>, each recipient account must configure its own <a href="/cloudflare-one/data-loss-prevention/dlp-policies/logging-options/#set-a-dlp-payload-encryption-public-key">encryption public key</a>.</p>
<pre><code class="language-mermaid">flowchart TD&#10;%% Accessibility&#10; accTitle: How Gateway policies work in a tiered account configuration&#10; accDescr: Flowchart describing the order of precedence Gateway applies policies in a tiered account configuration using Cloudflare Organizations.&#10;&#10;%% Flowchart&#10; subgraph s1[&quot;Source account&quot;]&#10;        n1[&quot;Block malware&quot;]&#10;        n2[&quot;Block spyware&quot;]&#10;        n3[&quot;Block DNS tunnel&quot;]&#10;  end&#10; subgraph s2[&quot;Recipient account A&quot;]&#10;        n5[&quot;Block malware&quot;]&#10;        n6[&quot;Block spyware&quot;]&#10;        n4[&quot;Block social media&quot;]&#10;  end&#10; subgraph s3[&quot;Recipient account B&quot;]&#10;        n8[&quot;Block malware&quot;]&#10;        n9[&quot;Block spyware&quot;]&#10;        n10[&quot;Block DNS tunnel&quot;]&#10;        n7[&quot;Block instant messaging&quot;]&#10;  end&#10;    n1 ~~~ n2&#10;    n2 ~~~ n3&#10;    s1 -- Share policies with --&gt; s2 &amp; s3&#10;&#10;    n1@{ shape: rect}&#10;    n2@{ shape: rect}&#10;    n3@{ shape: rect}&#10;    n4@{ shape: rect}&#10;    n5@{ shape: rect}&#10;    n6@{ shape: rect}&#10;    n7@{ shape: rect}&#10;    n8@{ shape: rect}&#10;    n9@{ shape: rect}&#10;    n10@{ shape: rect}&#10;     n1:::Sky&#10;     n2:::Sky&#10;     n3:::Peach&#10;     n4:::Forest&#10;     n5:::Sky&#10;     n6:::Sky&#10;     n7:::Forest&#10;     n8:::Sky&#10;     n9:::Sky&#10;     n10:::Peach&#10;    classDef Sky stroke-width:1px, stroke-dasharray:none, stroke:#374D7C, fill:#E2EBFF, color:#374D7C&#10;    classDef Peach stroke-width:1px, stroke-dasharray:none, stroke:#FBB35A, fill:#FFEFDB, color:#8F632D&#10;    classDef Forest stroke-width:1px, stroke-dasharray:none, stroke:#2D6A4F, fill:#D8F3DC, color:#2D6A4F&#10;</code></pre>
<p>In the diagram above:</p>
<ul>
<li>Blue policies (<strong>Block malware</strong> and <strong>Block spyware</strong>) are shared from the source account.</li>
<li>Orange policies (<strong>Block DNS tunnel</strong>) are not shared.</li>
<li>Green policies (<strong>Block social media</strong> and <strong>Block instant messaging</strong>) are created locally in recipient accounts.</li>
</ul>
<h2 id="limitations">Limitations</h2>
<p>Tiered policies with Organizations have the following limitations:</p>
<ul>
<li><a href="/cloudflare-one/traffic-policies/egress-policies/">Egress policies</a> cannot be shared between accounts.</li>
<li>Source accounts cannot share policies that use <a href="/cloudflare-one/reusable-components/posture-checks/">device posture</a> selectors, the <a href="/cloudflare-one/traffic-policies/network-policies/#detected-protocol">Detected protocol</a> selector, or the <a href="/cloudflare-one/traffic-policies/http-policies/#quarantine">Quarantine</a> action. Source and recipient accounts can still create and apply policies with these selectors and actions separately from the Organization share.</li>
<li>Policies can only be shared within an Organization. Sharing to sub-organizations is not supported.</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/6405.md")
</aside>
<h2 id="manage-policies">Manage policies</h2>
<p>You can create, configure, and share your tiered policies in the source account for your Cloudflare Organization.</p>
<h3 id="share-policy">Share policy</h3>
<p>To share a Gateway policy from a source account to a recipient account:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Traffic policies</strong> &gt; <strong>Firewall policies</strong>.</li>
<li>Choose the policy type you want to share. If you want to share a resolver policy, go to <strong>Traffic policies</strong> &gt; <strong>Resolver policies</strong>.</li>
<li>Find the policy you want to share from the list. In the three-dot menu, select <strong>Share</strong>. Alternatively, to bulk share multiple policies, you can select each policy you want to share, then select <strong>Actions</strong> &gt; <strong>Share</strong>.</li>
<li>In <strong>Select account</strong>, choose the accounts you want to share the policy with. To share the policy with all existing and future recipient accounts in your Organization, choose <em>Select all accounts in org</em>.</li>
<li>Select <strong>Continue</strong>, then select <strong>Share</strong>.</li>
</ol>
<p>A sharing icon will appear next to the policy's name. When sharing is complete, the policy will appear in and apply to the recipient accounts. Shared policies will appear grayed out in the recipient account's list of Gateway policies.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6404.md")
</aside>
<p>If a policy fails to share to recipient accounts, Gateway will retry deploying the policy automatically unless the error is unrecoverable.</p>
<h3 id="edit-share-recipients">Edit share recipients</h3>
<p>To change or remove recipients for a Gateway policy:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Traffic policies</strong> &gt; <strong>Firewall policies</strong>.</li>
<li>Choose the policy type you want to edit. If you want to edit a resolver policy, go to <strong>Traffic policies</strong> &gt; <strong>Resolver policies</strong>.</li>
<li>Find the policy you want to edit from the list.</li>
<li>In the three-dot menu, select <strong>Edit shared configuration recipients</strong>.</li>
<li>In <strong>Select account</strong>, choose the accounts you want to share the policy with. To remove a recipient, select <strong>Remove</strong> next to the recipient account's name.</li>
<li>Select <strong>Continue</strong>, then select <strong>Save</strong>.</li>
</ol>
<p>When sharing is complete, the policy sharing will update across the configured recipient accounts.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6403.md")
</aside>
<h3 id="unshare-policy">Unshare policy</h3>
<p>To stop sharing a policy with all recipient accounts:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Traffic policies</strong> &gt; <strong>Firewall policies</strong>.</li>
<li>Choose the policy type you want to remove. If you want to remove a resolver policy, go to <strong>Traffic policies</strong> &gt; <strong>Resolver policies</strong>.</li>
<li>Find the policy you want to remove from the list. In the three-dot menu, select <strong>Unshare</strong>. Alternatively, to bulk remove multiple policies, you can select each policy you want to remove, then select <strong>Actions</strong> &gt; <strong>Unshare</strong>.</li>
<li>Select <strong>Unshare</strong>.</li>
</ol>
<p>When sharing is complete, Gateway will stop sharing the policy with all recipient accounts and only apply the policy to the source account.</p>
<h3 id="edit-shared-policy">Edit shared policy</h3>
<p>Changes made to shared policies will apply to all recipient accounts. Deleting a shared policy will delete the policy from both the source account and all recipient accounts.</p>
<h2 id="manage-gateway-settings">Manage Gateway settings</h2>
<p>You can share certain Gateway settings - the Gateway block page and extended email address matching - from your source account to recipient accounts in your Cloudflare Organization. Other Gateway settings configured in a source account, such as <a href="/cloudflare-one/traffic-policies/http-policies/antivirus-scanning/">AV scanning</a> and <a href="/cloudflare-one/traffic-policies/http-policies/file-sandboxing/">file sandboxing</a>, will not affect recipient account configurations.</p>
<h3 id="share-gateway-block-page">Share Gateway block page</h3>
<p>To share your <a href="/cloudflare-one/reusable-components/custom-pages/gateway-block-page/">Gateway block page</a> settings from a source account to a recipient account:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Reusable components</strong> &gt; <strong>Custom pages</strong>.</li>
<li>In <strong>Account Gateway block page</strong>, select the three-dot menu and choose <strong>Share</strong>.</li>
<li>In <strong>Select account</strong>, choose the accounts you want to share the settings with. To share the settings with all existing and future recipient accounts in your Organization, choose <em>Select all accounts in org</em>.</li>
<li>Select <strong>Continue</strong>, then select <strong>Share</strong>.</li>
</ol>
<p>A sharing icon will appear next to the setting. When sharing is complete, the setting will appear in and apply to the recipient accounts.</p>
<p>To modify share recipients or unshare the setting, select the three-dot menu and choose <strong>Edit shared configuration recipients</strong> or <strong>Unshare</strong>.</p>
<h3 id="share-extended-email-address-matching">Share extended email address matching</h3>
<p>To share your <a href="/cloudflare-one/traffic-policies/identity-selectors/#extended-email-addresses">extended email address matching</a> settings from a source account to a recipient account:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Traffic policies</strong> &gt; <strong>Traffic settings</strong>.</li>
<li>In <strong>Firewall</strong> &gt; <strong>Matched extended email address</strong>, select the three-dot menu and choose <strong>Share</strong>.</li>
<li>In <strong>Select account</strong>, choose the accounts you want to share the settings with. To share the settings with all existing and future recipient accounts in your Organization, choose <em>Select all accounts in org</em>.</li>
<li>Select <strong>Continue</strong>, then select <strong>Share</strong>.</li>
</ol>
<p>A sharing icon will appear next to the setting. When sharing is complete, the setting will appear in and apply to the recipient accounts.</p>
<p>To modify share recipients or unshare the setting, select the three-dot menu and choose <strong>Edit shared configuration recipients</strong> or <strong>Unshare</strong>.</p>
