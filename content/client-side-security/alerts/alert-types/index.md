<p>You can configure alerts for resources detected in your domain. Refer to <a href="/client-side-security/alerts/">Alerts</a> for more information.</p>
<h2 id="new-resource-alerts">New resource alerts</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4020.md")
</aside>
<p>New resource alerts notify you about new resources detected on your domain, resources detected from new host domains, or issues with the URL length of newly detected resources.</p>
<details><summary>Client-side security New Resources Alert</summary><strong>Who is it for?</strong><p><a href="/client-side-security/">Client-side security</a> customers who want to receive a notification when new resources appear in their domain.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Business plans or higher.</p>
<strong>What should you do if you receive one?</strong><p>Investigate to confirm that it is an expected change.</p>
<strong>Additional information</strong><p>Triggered daily. If configured with a zone filter, the alert is triggered immediately.</p>
</details>
<details><summary>Client-side security New Domain Alert</summary><strong>Who is it for?</strong><p><a href="/client-side-security/">Client-side security</a> customers who want to receive a notification when resources from new host domains appear in their domain.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Business plans or higher.</p>
<strong>What should you do if you receive one?</strong><p>Investigate to confirm that it is an expected change.</p>
<strong>Additional information</strong><p>Triggered hourly. If configured with a zone filter, the alert is triggered immediately.</p>
</details>
<details><summary>Client-side security New Resource Exceeds Max URL Length Alert</summary><strong>Who is it for?</strong><p><a href="/client-side-security/">Client-side security</a> customers who want to receive a notification when a resource's URL exceeds the maximum allowed length.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Business plans or higher.</p>
<strong>What should you do if you receive one?</strong><p>Manually check the resource.</p>
</details>
<h2 id="code-change-alert">Code change alert</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4019.md")
</aside>
<p>This alert notifies you about <a href="/client-side-security/detection/review-changed-scripts/">code changes</a> in previously detected scripts.</p>
<details><summary>Client-side security New Code Change Detection Alert</summary><strong>Who is it for?</strong><p><a href="/client-side-security/">Client-side security</a> customers who want to receive a notification when JavaScript dependencies change in the pages of their domain.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Customers with Client-Side Security Advanced.</p>
<strong>What should you do if you receive one?</strong><p>Investigate to confirm that it is an expected change.</p>
<strong>Additional information</strong><p>Triggered daily. If configured with a zone filter, the alert is triggered immediately.</p>
</details>
<h2 id="malicious-resource-alerts">Malicious resource alerts</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4018.md")
</aside>
<p>Malicious resource alerts notify you about <a href="/client-side-security/how-it-works/malicious-script-detection/">resources considered malicious</a>, based on their <a href="/client-side-security/how-it-works/malicious-script-detection/#malicious-domain-checks">domain</a>, <a href="/client-side-security/how-it-works/malicious-script-detection/#malicious-url-checks">URL</a>, or <a href="/client-side-security/how-it-works/malicious-script-detection/#malicious-script-detection">script content</a>.</p>
<details><summary>Client-side security New Malicious Domain Alert</summary><strong>Who is it for?</strong><p><a href="/client-side-security/">Client-side security</a> customers who want to receive a notification when resources from a known malicious domain appear in their domain. For more information, refer to <a href="/client-side-security/how-it-works/malicious-script-detection/">Malicious script and connection detection</a>.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Customers with Client-Side Security Advanced.</p>
<strong>What should you do if you receive one?</strong><p>Review the information in the client-side security dashboard about the detected malicious resources, then update the pages where those resources were detected.</p>
<p>For more information, refer to <a href="/client-side-security/detection/review-malicious-scripts/">Review scripts and connections considered malicious</a>.</p>
</details>
<details><summary>Client-side security New Malicious URL Alert</summary><strong>Who is it for?</strong><p><a href="/client-side-security/">Client-side security</a> customers who want to receive a notification when resources from a known malicious URL appear in their domain. For more information, refer to <a href="/client-side-security/how-it-works/malicious-script-detection/">Malicious script and connection detection</a>.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Customers with Client-Side Security Advanced.</p>
<strong>What should you do if you receive one?</strong><p>Review the information in the client-side security dashboard about the detected malicious resources, then update the pages where those resources were detected.</p>
<p>For more information, refer to <a href="/client-side-security/detection/review-malicious-scripts/">Review scripts and connections considered malicious</a>.</p>
</details>
<details><summary>Client-side security New Malicious Script Alert</summary><strong>Who is it for?</strong><p><a href="/client-side-security/">Client-side security</a> customers who want to receive a notification when Cloudflare classifies JavaScript dependencies in their domain as malicious. For more information, refer to <a href="/client-side-security/how-it-works/malicious-script-detection/">Malicious script and connection detection</a>.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>Customers with Client-Side Security Advanced.</p>
<strong>What should you do if you receive one?</strong><p>Review the information in the client-side security dashboard about the detected malicious resources, then update the pages where those resources were detected.</p>
<p>For more information, refer to <a href="/client-side-security/detection/review-malicious-scripts/">Review scripts and connections considered malicious</a>.</p>
</details>
<p>Malicious resource alerts will only include resources with an <em>Active</em> status. Refer to <a href="/client-side-security/reference/script-statuses/">Script and connection statuses</a> for more information.</p>
