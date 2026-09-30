<p>The Child Sexual Abuse Material (CSAM) Scanning Tool allows website owners to proactively identify and take action on CSAM located on their website. By enabling this tool, Cloudflare will compare content served for your website through the Cloudflare cache to known lists of CSAM. These lists are provided to Cloudflare by leading child safety advocacy groups such as the National Center for Missing and Exploited Children (NCMEC).</p>
<p>Remember, by enabling the Service, you agree to the <a href="https://www.cloudflare.com/service-specific-terms-application-services/#csam-scanning-tool-terms">Service-Specific Terms</a> for the CSAM Scanning Tool. You agree to use this tool solely for the purposes of preventing the spread of CSAM.</p>
<hr />
<h2 id="why-would-a-url-be-blocked">Why would a URL be blocked?</h2>
<p>Because knowingly distributing or viewing CSAM is illegal, the owner of the website has enabled Cloudflare's CSAM scanning tool to proactively identify and block images identified as CSAM located on their website.</p>
<hr />
<h2 id="configure-the-csam-scanning-tool">Configure the CSAM scanning tool</h2>
<p>To enable the tool:</p>
<ol>
<li>Log into the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>.</li>
<li>Select your account and zone.</li>
<li>Go to <strong>Caching</strong> &gt; <strong>Configuration</strong>.</li>
<li>For <strong>CSAM Scanning Tool</strong>, select <strong>Configure</strong>.</li>
</ol>
<p>You must provide an email address, which will be used to notify you in the event Cloudflare detects a positive match.</p>
<hr />
<h2 id="what-happens-when-a-match-is-detected">What happens when a match is detected?</h2>
<p>When a potential match is detected with the tool:</p>
<ol>
<li>An email is sent to you once per day to inform you of any detections made in the past 24 hours. This email will include the file paths of any content that was matched.</li>
<li>If possible, a block is placed to prevent further serving of the matched content. If a block fails, we will indicate that the content has not been blocked in the email.</li>
</ol>
<hr />
<h2 id="what-action-should-i-take-when-a-match-is-detected">What action should I take when a match is detected?</h2>
<p>You are responsible for understanding and complying with any legal obligations you have as a website owner when made aware of any potential CSAM. Although legal obligations vary based on the provider and the jurisdiction, website owners often have obligations to report apparent CSAM, to remove content, and to preserve records. Some of those possible obligations are as follows:</p>
<ul>
<li>You likely have an obligation to report apparent CSAM to the appropriate authorities. You can file a report to NCMEC with additional information via NCMEC's CyberTip reporting form or find the preferred reporting portal for your jurisdiction via the INHOPE website.</li>
</ul>
<br />
<ul>
<li>You may need to preserve and securely store a copy of the content and related data in the case NCMEC or law enforcement reach out for additional details.</li>
<li>You likely have an obligation to securely preserve certain information related to your report for one year in the case of an investigation. To ensure that access to the content is limited, take care not to store this information anywhere accessible to anyone but those within your organization responsible for legal requests.</li>
</ul>
<br />
<ul>
<li>You should remove the content and notify Cloudflare of the removal.</li>
<li>Once any preservation obligations have been fulfilled, you should remove the content from your website. This is especially important if Cloudflare's notice to you indicates that our block was unsuccessful.</li>
</ul>
<hr />
<h2 id="how-do-i-have-a-block-removed-from-my-website">How do I have a block removed from my website?</h2>
<p>To disable a block, either because you have determined that the blocked content is not CSAM (a false positive) or because you have taken down the blocked content, view <a href="/fundamentals/reference/report-abuse/blocked-content/">Blocked Content in the Security Center</a> in the Cloudflare Dashboard and request reviews on the relevant blocks. A request to remove a block must be accompanied by a representation from you confirming that the blocked content is not CSAM or has been removed.</p>
<p>These actions are available to users with the following roles:</p>
<ul>
<li>Admin</li>
<li>Super Admin</li>
<li>Trust &amp; Safety</li>
</ul>
<hr />
<h2 id="additional-resources">Additional Resources</h2>
<p><a href="https://www.cloudflare.com/supplemental-terms/">CSAM Scanning Tool Supplemental Terms</a></p>
<p><a href="https://www.missingkids.org/">National Center for Missing and Exploited Children (NCMEC)</a></p>
<p><a href="https://www.missingkids.org/gethelpnow/cybertipline">NCMEC CyberTipline</a></p>
<p><a href="https://www.inhope.org/">INHOPE</a></p>
