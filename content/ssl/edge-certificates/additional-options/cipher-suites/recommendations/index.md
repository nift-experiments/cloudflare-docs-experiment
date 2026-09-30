<p>Refer to the sections below for three different security levels and how Cloudflare recommends that you set them up if you need to restrict the <a href="/ssl/edge-certificates/additional-options/cipher-suites/">cipher suites</a> used between Cloudflare and clients that access your website or application.</p>
<p>Refer to <a href="/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/">Customize cipher suites</a> to learn how to specify cipher suites at zone level or per hostname.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/14163.md")
</aside>
<h2 id="modern">Modern</h2>
<p>Offers the best security and performance, limiting your range of clients to modern devices and browsers. Supports TLS 1.2-1.3 cipher suites. All suites are forward-secret and support authenticated encryption (AEAD).</p>
<details class="nb-details"><summary>Cipher suites list</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/14164.md")
</div></details>
<p>If you are customizing cipher suites via API, refer to <a href="/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/api/#steps-and-api-examples">Steps and API examples</a> for a snippet you can copy with the formatted array.</p>
<h2 id="compatible">Compatible</h2>
<p>Provides broader compatibility with somewhat weaker security. Supports TLS 1.2-1.3 cipher suites. All suites are forward-secret.</p>
<details class="nb-details"><summary>Cipher suites list</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/14165.md")
</div></details>
<p>If you are customizing cipher suites via API, refer to <a href="/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/api/#steps-and-api-examples">Steps and API examples</a> for a snippet you can copy with the formatted array.</p>
<h2 id="legacy-default">Legacy (default)</h2>
<p>Includes all cipher suites that Cloudflare supports today. Broadest compatibility with the weakest security. Supports TLS 1.0-1.3 cipher suites.</p>
<details class="nb-details"><summary>Cipher suites list</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/14166.md")
</div></details>
<p>To reset your option to the default, <a href="/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/#reset-to-default-values">use an empty array</a>.</p>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">Same as `TLS_AES_128_GCM_SHA256`. Refer to [TLS 1.3 cipher suites](/ssl/edge-certificates/additional-options/cipher-suites/#tls-13) for details.</li>
<li id="footnote-2">Same as `TLS_AES_256_GCM_SHA384`. Refer to [TLS 1.3 cipher suites](/ssl/edge-certificates/additional-options/cipher-suites/#tls-13) for details.</li>
<li id="footnote-3">Same as `TLS_CHACHA20_POLY1305_SHA256`. Refer to [TLS 1.3 cipher suites](/ssl/edge-certificates/additional-options/cipher-suites/#tls-13) for details.</li>
<li id="footnote-4">Although configured independently, cipher suites interact with **Minimum TLS version** and **TLS 1.3**.</li></ol></section>
