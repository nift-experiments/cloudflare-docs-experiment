<p>A DLP profile defines what sensitive data Cloudflare detects in your traffic. A profile combines one or more of the following building blocks:</p>
<ul>
<li><strong><a href="/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/">Detection entries</a></strong> — reusable detection logic that identifies sensitive content, such as patterns, datasets, document fingerprints, predefined detections, and AI prompt topics.</li>
<li><strong>Data classes</strong> — reusable classification rules that combine detection entries and other signals into a single rule.</li>
<li><strong>Labels</strong> — sensitivity levels and data tags that describe matched content.</li>
</ul>
<p>Data classes and labels are part of <a href="/cloudflare-one/data-loss-prevention/data-classification/">Data Classification</a>. Cloudflare DLP offers three types of profiles:</p>
<ul>
<li><strong><a href="/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/">Predefined profiles</a></strong> — Cloudflare-managed profiles for common sensitive data types such as credit card numbers, national identifiers, and AI prompts.</li>
<li><strong>Custom profiles</strong> — profiles you <a href="#build-a-custom-profile">build</a> from detection entries, data classes, and labels, specific to your data, organization, and risk tolerance.</li>
<li><strong><a href="/cloudflare-one/data-loss-prevention/dlp-profiles/integration-profiles/">Integration profiles</a></strong> — profiles populated with data classifications from a third-party platform, such as Microsoft Purview sensitivity labels (requires Cloudflare CASB).</li>
</ul>
<p>To decide which data types to focus on, use <a href="/cloudflare-one/data-loss-prevention/passive-detection/">Passive Detection</a> to explore detections in sampled Gateway traffic before creating a DLP policy.</p>
<h2 id="configure-a-predefined-profile">Configure a predefined profile</h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Data loss prevention</strong> &gt; <strong>Profiles</strong>.</li>
<li>Choose a <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/">predefined profile</a> and select <strong>Edit</strong>.</li>
<li>Enable one or more <strong>Detection entries</strong> according to your preferences.</li>
<li>Select <strong>Save profile</strong>.</li>
</ol>
<p>Most predefined profiles match when any enabled detection entry matches. The <strong>Personally Identifiable Information (PII) Record</strong> profile is an exception and requires at least three unique detection entries in close proximity before the profile matches.</p>
<p>You can now use this profile in a <a href="/cloudflare-one/data-loss-prevention/dlp-policies/#2-create-a-dlp-policy">DLP policy</a>, <a href="/cloudflare-one/cloud-and-saas-findings/casb-dlp/">CASB integration</a>, <a href="/ai-gateway/features/dlp/set-up-dlp/">AI Gateway DLP policy</a>, or <a href="/cloudflare-one/email-security/outbound-dlp/">Email Security outbound DLP policy</a>.</p>
<h2 id="build-a-custom-profile">Build a custom profile</h2>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Data loss prevention</strong> &gt; <strong>Profiles</strong>.</p>
</li>
<li>
<p>Select <strong>Create profile</strong>.</p>
</li>
<li>
<p>Enter a name and optional description for the profile.</p>
</li>
<li>
<p>Add detection entries to the profile.</p>
<details class="nb-details"><summary>Create a custom entry</summary><div class="nb-details-body">
</li>
</ol>
@markup("md", "content/.markup/bodies/4898.md")
</div></details>
   <details class="nb-details"><summary>Add existing entries</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/4899.md")
</div></details>
<ol start="5">
<li>
<p>(Optional) Add data classes to include reusable classification rules.</p>
<ul>
<li>Select <strong>Add data classes</strong></li>
<li>Choose the data classes you want to add, then select <strong>Confirm</strong></li>
</ul>
</li>
<li>
<p>(Optional) Use labels as match criteria for the profile.</p>
<ul>
<li>Select a sensitivity schema and minimum sensitivity level.</li>
<li>Select a data tag group and one or more data tags.</li>
</ul>
<p>For more information on labels, templates, and data classes, refer to <a href="/cloudflare-one/data-loss-prevention/data-classification/">Data Classification</a>.</p>
</li>
<li>
<p>(Optional) Configure <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/advanced-settings/"><strong>profile settings</strong></a> for the profile.</p>
</li>
<li>
<p>Select <strong>Save profile</strong>.</p>
</li>
</ol>
<p>Before you apply a custom profile to production traffic, use <a href="/cloudflare-one/data-loss-prevention/test-scan/">Test scan</a> to confirm that it detects the content you expect.</p>
<p>You can now use this profile in a <a href="/cloudflare-one/data-loss-prevention/dlp-policies/#2-create-a-dlp-policy">DLP policy</a>, <a href="/cloudflare-one/cloud-and-saas-findings/casb-dlp/">CASB integration</a>, <a href="/ai-gateway/features/dlp/set-up-dlp/">AI Gateway DLP policy</a>, or <a href="/cloudflare-one/email-security/outbound-dlp/">Email Security outbound DLP policy</a>.</p>
