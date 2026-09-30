<p>Consider the following recommendations on custom <a href="/ssl/edge-certificates/additional-options/cipher-suites/">cipher suites</a> for when your organization needs to comply with regulatory standards.</p>
<p>Refer to <a href="/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/">Customize cipher suites</a> to learn how to specify cipher suites at zone level or per hostname.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/14168.md")
</aside>
<h2 id="pci-dss">PCI DSS</h2>
<p>Recommended cipher suites for compliance with the <a href="https://www.pcisecuritystandards.org/standards/pci-dss/">Payment Card Industry Data Security Standard (PCI DSS)</a>. Enhances payment card data security.</p>
<details class="nb-details"><summary>Cipher suites list</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/14169.md")
</div></details>
<p>If you are customizing cipher suites via API, refer to <a href="/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/api/#steps-and-api-examples">Steps and API examples</a> for a snippet you can copy with the formatted array.</p>
<h2 id="fips-140-3">FIPS-140-3</h2>
<p>Recommended cipher suites for compliance with the <a href="https://csrc.nist.gov/pubs/fips/140-3/final">Federal Information Processing Standard (140-3)</a>. Used to approve cryptographic modules.</p>
<details class="nb-details"><summary>Cipher suites list</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/14170.md")
</div></details>
<p>If you are customizing cipher suites via API, refer to <a href="/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/api/#steps-and-api-examples">Steps and API examples</a> for a snippet you can copy with the formatted array.</p>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">Same as `TLS_AES_128_GCM_SHA256`. Refer to [TLS 1.3 cipher suites](/ssl/edge-certificates/additional-options/cipher-suites/#tls-13) for details.</li>
<li id="footnote-2">Same as `TLS_AES_256_GCM_SHA384`. Refer to [TLS 1.3 cipher suites](/ssl/edge-certificates/additional-options/cipher-suites/#tls-13) for details.</li>
<li id="footnote-3">Same as `TLS_CHACHA20_POLY1305_SHA256`. Refer to [TLS 1.3 cipher suites](/ssl/edge-certificates/additional-options/cipher-suites/#tls-13) for details.</li></ol></section>
