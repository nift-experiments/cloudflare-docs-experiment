<p>If you receive a <a href="/client-side-security/alerts/alert-types/">client-side resource alert</a>, sometimes you need to perform some manual investigation to confirm the nature of the script. Use the guidance provided in this page as a starting point for your investigation.</p>
<h2 id="1-understand-what-triggered-the-alert"><ol>
<li>Understand what triggered the alert</li>
</ol></h2>
<p>Start by identifying the <a href="/client-side-security/how-it-works/malicious-script-detection/">detection system</a> that triggered the alert. A link is provided in the alert that will send you directly to the Cloudflare dashboard to the relevant resource that needs reviewing. Alternatively, do the following:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/4008.md")
</div>
<p>The details page will specify which detection system triggered the alert. Check the values of the following fields:</p>
<ul>
<li><strong>Malicious code</strong></li>
<li><strong>Malicious URL</strong></li>
<li><strong>Malicious domain</strong></li>
</ul>
<p>Different detection mechanisms may consider the script malicious at the same time. This increases the likelihood of the detection not being a false positive.</p>
<h2 id="2-find-the-page-where-the-resource-was-detected"><ol start="2">
<li>Find the page where the resource was detected</li>
</ol></h2>
<p>If you received an alert for a potentially malicious script:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/4009.md")
</div>
<p>If you received an alert for a potentially malicious connection:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/4010.md")
</div>
<p>If you find the script or connection, this means the script is being loaded (or the connection is being established) for all website visitors — proceed to <a href="#3-check-the-script-reputation">step 3</a>.</p>
<p>If you do not find the script being loaded or the connection being made, this could mean one of the following:</p>
<ul>
<li>The script is being loaded (or the connection is being made) by visitors' browser extensions.</li>
<li>Your current state will not load the script or make the connection. Complex applications might load scripts and establish connections based on state.</li>
<li>You are not in the correct geographic location (or similar condition).</li>
<li>The attacker is only loading the script or making the connection for a percentage of visitors or visitors with specific browsers/signatures.</li>
</ul>
<p>In this case, in addition to the steps indicated below, the best approach is:</p>
<ul>
<li>From a safe virtual environment, use online search tools and search for the given resource. Review results and resource metadata, for example domain registration details;</li>
<li>If in doubt, scan the application codebase for the resource and if found, clarify the purpose.</li>
</ul>
<h2 id="3-check-the-script-reputation"><ol start="3">
<li>Check the script reputation</li>
</ol></h2>
<p>If Cloudflare considers the resource’s domain a &quot;malicious domain&quot;, it is likely that the domain does not have a good reputation. The domain may be known for hosting malware or for being used for phishing attacks. Usually, reviewing the domain/hostname is sufficient to understand why you received the alert. You can use tools like Cloudflare's <a href="https://dash.cloudflare.com/?to=/:account/security-center/investigate">Security Center Investigate</a> platform to help with this validation.</p>
<p>If Cloudflare's internal systems classified the script as containing &quot;malicious code&quot;, external tools may not confirm the detection you got from Cloudflare, since the machine learning (ML) model being used is Cloudflare-specific technology.</p>
<p>If you believe that Cloudflare's classification is a false positive, contact your account team so that we can further improve client-side security's underlying technology.</p>
<h2 id="4-optional-analyze-the-script-content"><ol start="4">
<li>(Optional) Analyze the script content</li>
</ol></h2>
<p>You could use a virtual machine to perform some of the following analysis:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/4011.md")
</div>
<hr />
<h2 id="conclusion">Conclusion</h2>
<p>If a resource which triggered a malicious resource alert:</p>
<ul>
<li>Is actively present in your application</li>
<li>Is being loaded from a malicious host or IP address, or has malicious code</li>
<li>Has malicious hostnames or IP addresses in its source code, which may be obfuscated/encoded</li>
</ul>
<p>You should investigate further, since these indicators can be a sign of an ongoing active compromise.</p>
