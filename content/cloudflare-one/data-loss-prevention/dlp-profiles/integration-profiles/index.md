<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4897.md")
</aside>
<p>Integration profiles let you use data classifications from a third-party platform (such as Microsoft Purview sensitivity labels) directly in Cloudflare DLP. Instead of recreating classification rules yourself, Cloudflare retrieves them from the third-party platform and populates them as <a href="/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/">detection entries</a> in a DLP profile. You can then enable the entries you want and create a DLP policy to allow or block matching data.</p>
<p>Detection entries in integration profiles are managed by the third-party platform. You cannot manually add, edit, or delete these entries within Cloudflare DLP.</p>
<h2 id="microsoft-purview-information-protection-mip-sensitivity-labels">Microsoft Purview Information Protection (MIP) sensitivity labels</h2>
<p>Microsoft provides <a href="https://learn.microsoft.com/en-us/purview/sensitivity-labels">Purview Information Protection sensitivity labels</a> to classify and protect sensitive data.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/4896.md")
</aside>
<h3 id="setup">Setup</h3>
<p>To add MIP sensitivity labels to a DLP profile, integrate your Microsoft account with <a href="/cloudflare-one/integrations/cloud-and-saas/microsoft-365/">Cloudflare CASB</a>. A new integration profile will appear under <strong>Zero Trust</strong> &gt; <strong>Data loss prevention</strong> &gt; <strong>Profiles</strong>. The profile is named <strong>MIP Sensitivity Labels</strong> followed by the name of the CASB integration.</p>
<p>MIP sensitivity labels can also be added to a <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/#build-a-custom-profile">custom DLP profile</a> as an existing entry.</p>
<h3 id="syncing">Syncing</h3>
<p>Allow 24 hours for label additions and edits in your Microsoft account to propagate to Cloudflare DLP. Deletions in your Microsoft account will not delete entries in your Cloudflare DLP profile.</p>
