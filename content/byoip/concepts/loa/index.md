<p>A Letter of Agency (LOA), sometimes referred to as a Letter of Authorization, is a document that authorizes Cloudflare to announce your IP prefixes on your behalf. Cloudflare's transit providers — the upstream networks that Cloudflare peers with to exchange routing information — require an LOA before they will accept the routes Cloudflare advertises for you.</p>
<p>The LOA must specify the prefixes you are authorizing Cloudflare to announce and the autonomous system number (ASN) they will be announced under. You can use your own ASN or Cloudflare's ASN (AS13335).</p>
<h2 id="requirements">Requirements</h2>
<ul>
<li>
<p>For all future onboardings, if using the Cloudflare ASN, you must use AS13335. Current customers who are already using Cloudflare's AS209242 do not need to make any changes and can continue using that ASN.</p>
</li>
<li>
<p>Cloudflare accepts digital signatures on an LOA, as long as it is clear who is signing the LOA.</p>
</li>
<li>
<p>An LOA is a formal document which should be on company letterhead and contain a wet signature. The Letter of Agency must be a PDF. Transit providers may reject the LOA if it is in a JPG or PNG format.</p>
</li>
</ul>
<h2 id="auto-generated-loa">Auto-generated LOA</h2>
<p>If you are onboarding your own IPs via the <a href="/byoip/get-started/">self-serve flow</a>, you can set <code>delegate_loa_creation</code> (in the <a href="/api/resources/addressing/subresources/prefixes/methods/create/">Add Prefix API call</a>) to <code>true</code> . This will allow Cloudflare to automatically generate the LOA, speeding up the process.</p>
<p>Auto-generated LOAs rely on <a href="/byoip/concepts/route-filtering-rpki/">RPKI-signed ROAs</a> and <a href="/byoip/get-started/#validate-prefix-ownership">ownership validation</a> checks.</p>
<h2 id="template">Template</h2>
<p>If you need to create an LOA document, you can use the template below.</p>
<pre><code class="language-txt">[COMPANY LETTERHEAD]&#10;&#10;LETTER OF AGENCY (&quot;LOA&quot;)&#10;&#10;[DATE]&#10;&#10;&#10;To whom it may concern:&#10;&#10;[COMPANY NAME] (the &quot;Company&quot;) authorizes Cloudflare, Inc. with AS13335 to advertise the following IP address blocks / originating ASNs:&#10;&#10;&#45; - - - - - - - - - - - - - - - - - -&#10;[Subnet &amp; Originating ASN]&#10;[Subnet &amp; Originating ASN]&#10;[Subnet &amp; Originating ASN]&#10;&#45; - - - - - - - - - - - - - - - - - -&#10;&#10;As a representative of the Company that is the owner of the aforementioned IP address blocks / originating ASNs, I hereby declare that I am authorized to sign this LOA on the Company’s behalf.&#10;&#10;Should you have any questions please email me at [E-MAIL ADDRESS], or call: [TELEPHONE NUMBER]&#10;&#10;Regards,&#10;&#10;&#10;[SIGNATURE]&#10;&#10;&#10;[NAME TYPED]&#10;[TITLE]&#10;[COMPANY NAME]&#10;[COMPANY ADDRESS]&#10;[COMPANY STAMP]&#10;</code></pre>
