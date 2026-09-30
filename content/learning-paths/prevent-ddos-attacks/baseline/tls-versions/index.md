<p>In some circumstances - specifically when an application allows client-initiated SSL/TLS renegotiation - previous versions of SSL/TLS can be more vulnerable to DDoS attacks.</p>
<p>When you use an SSL/TLS certificate issued by Cloudflare<sup><a href="#footnote-1">1</a></sup>, you can reduce the impact of this vulnerability by:</p>
<ul>
<li>Updating the <a href="/ssl/edge-certificates/additional-options/minimum-tls/">Minimum TLS Version</a> accepted by your application.</li>
<li>Allowing <a href="/ssl/edge-certificates/additional-options/tls-13/">TLS 1.3</a>.</li>
</ul>
<h2 id="additional-resources">Additional resources</h2>
<p>For more details on this vulnerability, refer to <a href="https://crashtest-security.com/secure-client-initiated-ssl-renegotiation/">Secure Server- and Client-Initiated SSL Renegotiation</a>.</p>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">Meaning either [Universal](/ssl/edge-certificates/universal-ssl/) or [Advanced](/ssl/edge-certificates/advanced-certificate-manager/) certificates.</li></ol></section>
