<p>Refer to this page for frequently asked questions about Cloudflare SSL/TLS certificate offerings and the CAs that Cloudflare partners with.</p>
<hr />
<h2 id="general">General</h2>
<h3 id="does-cloudflare-issue-both-rsa-and-ecdsa-certificates">Does Cloudflare issue both RSA and ECDSA certificates?</h3>
<p>Yes. Cloudflare can issue both RSA and ECDSA certificates.</p>
<h3 id="are-cloudflare-ssl-certificates-shared">Are Cloudflare SSL certificates shared?</h3>
<p>No. Cloudflare SSL/TLS certificates are not shared across domains nor across customers.</p>
<h3 id="if-i-have-multiple-cloudflare-certificates-which-one-is-used">If I have multiple Cloudflare certificates, which one is used?</h3>
<p>Cloudflare certificates are prioritized by a combination of hostname specificity, zone specificity, and certificate type. For more details, refer to <a href="/ssl/reference/certificate-and-hostname-priority/">Certificate and hostname priority</a>.</p>
<h3 id="why-do-i-see-a-cloudflare-certificate-when-an-ssl-certificate-is-installed-at-my-website">Why do I see a Cloudflare certificate when an SSL certificate is installed at my website?</h3>
<p>Cloudflare must decrypt traffic in order to cache and filter malicious traffic. Cloudflare either re-encrypts traffic or sends plain text traffic to the origin web server depending on your domain's <a href="/ssl/origin-configuration/ssl-modes/">encryption mode</a>.</p>
<hr />
<h2 id="certificate-authorities-cas">Certificate authorities (CAs)</h2>
<h3 id="which-certificate-authorities-does-cloudflare-use">Which certificate authorities does Cloudflare use?</h3>
<p>Cloudflare uses Let's Encrypt, Google Trust Services, SSL.com, and Sectigo. You can see a complete list of products and available CAs and algorithms in the <a href="/ssl/reference/certificate-authorities/">certificate authorities reference page</a>.</p>
<p>Sectigo is only used for <a href="/ssl/edge-certificates/backup-certificates/">backup certificates</a>.</p>
<h3 id="are-there-any-ca-limitations-i-should-know-about">Are there any CA limitations I should know about?</h3>
<p>Refer to the <a href="/ssl/reference/certificate-authorities/">certificate authorities reference page</a> for a list of limitations for every CA in our pipeline. There you can also find information about device and browser compatibility.</p>
<h3 id="i-do-not-want-to-use-the-cas-that-cloudflare-partners-with-what-can-i-do">I do not want to use the CAs that Cloudflare partners with. What can I do?</h3>
<p>If you are on a Business or Enterprise plan, you can <a href="/ssl/edge-certificates/custom-certificates/uploading/#upload-a-custom-certificate">upload a certificate</a> from the CA of your choice.</p>
<h3 id="i-am-missing-the-cas-that-cloudflare-uses-in-my-trust-store-what-should-i-do">I am missing the CAs that Cloudflare uses in my trust store. What should I do?</h3>
<p>You can use <a href="https://github.com/cloudflare/cfssl_trust">CFSSL trust store</a>, which includes all of the CAs that are used by Cloudflare managed certificates.</p>
<hr />
<h2 id="caa-records">CAA records</h2>
<h3 id="what-is-caa-and-how-can-i-create-one">What is CAA and how can I create one?</h3>
<p>A Certificate Authority Authorization (CAA) DNS record specifies which certificate authorities (CAs) are allowed to issue certificates for a domain. This record reduces the chance of unauthorized certificate issuance and promotes standardization across your organization.
<br /></p>
<p>For more details, refer to <a href="/ssl/edge-certificates/caa-records/">Add CAA records</a>.</p>
<h3 id="how-does-cloudflare-evaluate-caa-records">How does Cloudflare evaluate CAA records?</h3>
<p>CAA records are evaluated by a CA, not by Cloudflare. For details, refer to <a href="https://www.rfc-editor.org/rfc/rfc8659.html#name-relevant-resource-record-se">RFC 8659</a>.</p>
<p>Setting a CAA record to specify one or more particular CAs does not affect which CA Cloudflare uses to issue universal or advanced certificates for your domain. If you wish, you can specify CAs associated with Cloudflare certificates when <a href="/ssl/edge-certificates/advanced-certificate-manager/manage-certificates/">ordering an advanced certificate</a>.</p>
<h3 id="what-are-the-dangers-of-setting-caa-records">What are the dangers of setting CAA records?</h3>
<p>If you are part of a large organization or one where multiple parties are tasked with obtaining SSL certificates, <a href="/ssl/edge-certificates/caa-records/">include CAA records</a> that allow issuance for all CAs applicable for your organization. Failure to do so can inadvertently block SSL issuance for other parts of your organization.</p>
<h3 id="what-caa-records-do-i-need-to-allow-issuance-from-cloudflare-cas">What CAA records do I need to allow issuance from Cloudflare CAs?</h3>
<p>You can find CAA records associated with every Cloudflare CA in the <a href="/ssl/reference/certificate-authorities/#caa-records">certificate authorities reference page</a>. If you are using Cloudflare as your DNS provider, then the CAA records will be added on your behalf.</p>
<hr />
<h2 id="universal-ssl">Universal SSL</h2>
<h3 id="i-am-using-universal-ssl-and-i-would-like-to-use-a-different-ca-how-can-i-do-that">I am using Universal SSL and I would like to use a different CA. How can I do that?</h3>
<p>To be able to specify a CA, you must purchase <a href="/ssl/edge-certificates/advanced-certificate-manager/">Advanced Certificate Manager</a>. Through Advanced Certificate Manager, you can choose the certificate authority when ordering an advanced certificate or you can choose a default CA when using <a href="/ssl/edge-certificates/additional-options/total-tls/">Total TLS</a>.</p>
<p>If you are on a Business or Enterprise plan, you can <a href="/ssl/edge-certificates/custom-certificates/uploading/#upload-a-custom-certificate">upload a certificate</a> from the CA of your choice. In this case, certificate issuance and renewal will have to be managed by you.</p>
<h3 id="does-cloudflare-issue-both-rsa-and-ecdsa-certificates-for-universal-certificates">Does Cloudflare issue both RSA and ECDSA certificates for Universal certificates?</h3>
<p>Universal certificates on free zones only receive an ECDSA certificate. Paid zones receive an RSA and ECDSA certificate.</p>
