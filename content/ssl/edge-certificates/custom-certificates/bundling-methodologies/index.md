<p>When an SSL certificate is deployed to Cloudflare's global network, it may be augmented with intermediate and root certificates to assist the user agent in finding a chain to a publicly trusted root.</p>
<p>You can control the mechanics of how certificates are bundled by specifying a bundling methodology.</p>
<h2 id="intermediate-and-root-certificates">Intermediate and root certificates</h2>
<p>Cloudflare maintains intermediate and root certificates used for bundling on a <a href="https://github.com/cloudflare/cfssl_trust">GitHub repository</a>. As the certificates expire or are removed by certificate authorities, Cloudflare removes and adds them accordingly.</p>
<p>Expiration values for these certificates may appear in the <code>expires_on</code> field when you use the <a href="/api/resources/ssl/subresources/analyze/methods/create/">Analyze Certificate endpoint</a> - often when the methodology you specify is <a href="#compatible">Compatible</a>. However, these expiration values reflect intermediate and root certificates - which are handled by Cloudflare -, not the leaf certificate you would have previously uploaded to Cloudflare.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14095.md")
</aside>
<h2 id="methodologies">Methodologies</h2>
<h3 id="compatible">Compatible</h3>
<p>Compatible is the default methodology and uses common and well distributed intermediate certificates to complete the chain. This ensures that the resulting bundle is compatible with as many clients as possible.</p>
<p>The related value for the <code>bundle_method</code> parameter when using the <a href="/api/resources/custom_certificates/methods/create/">API</a> is <code>ubiquitous</code>.</p>
<h3 id="modern">Modern</h3>
<p>Modern consists of attempts to make the chain as efficient as possible, often by using newer or fewer intermediate certificates.</p>
<p>The related value for the <code>bundle_method</code> parameter when using the <a href="/api/resources/custom_certificates/methods/create/">API</a> is <code>optimal</code>.</p>
<h3 id="user-defined">User-defined</h3>
<p>User-defined allows you to paste your own certificate chain and present that bundle to clients. If you are using a self-signed certificate (not recommended), you must use this mode.</p>
<p>The related value for the <code>bundle_method</code> parameter when using the <a href="/api/resources/custom_certificates/methods/create/">API</a> is <code>force</code>.</p>
