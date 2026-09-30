<p>Though <a href="/style-guide/style-and-grammar/formatting/structure/links/">links</a> are an important part of documentation, they also have their own maintenance cost.</p>
<p>We have a few strategies we use to make link maintenance easier.</p>
<h2 id="link-types">Link types</h2>
<p>Documentation uses three <a href="/style-guide/style-and-grammar/formatting/structure/links/#types-of-links">types of links</a>: external, internal, and anchor. For each type, we think through a few different aspects of the experience.</p>
<ul>
<li><strong>External</strong>:
<ul>
<li><em>Source of truth</em>: Another site.</li>
<li><em>Why does it break</em>: Another site changed its content.</li>
<li><em>Customer experience of a break</em>: <code>404</code> page on another site.</li>
</ul>
</li>
<li><strong>Internal</strong>:
<ul>
<li><em>Source of truth</em>: Your site.</li>
<li><em>Why does it break</em>: Your site changed its content.</li>
<li><em>Customer experience of a break</em>: <code>404</code> page on your site.</li>
</ul>
</li>
<li><strong>Anchor</strong>:
<ul>
<li><em>Source of truth</em>: Your site.</li>
<li><em>Why does it break</em>: Your site changed its content.</li>
<li><em>Customer experience of a break</em>: Page load on your site. Content might be further down the page or have been moved to another page.</li>
</ul>
</li>
</ul>
<h2 id="checks">Checks</h2>
<h3 id="internal-links">Internal links</h3>
<p>Of these three <a href="#link-types">link types</a>, only <strong>Internal</strong> links:</p>
<ul>
<li>Happen <em>within</em> the context of a change to your site's content.</li>
<li>Universally lead to a bad customer experience (a <code>404</code> page).</li>
<li>Are easily auditable within the current context.</li>
</ul>
<p>For these reasons, we choose to make a build <strong>fail</strong> based on broken internal links. For our implementation, we rely on <a href="https://nimbus-docs.com/">Nimbus</a>'s <code>nimbus/internal-link</code> <a href="https://nimbus-docs.com/writing/linting/">lint rule</a>, configured in <a href="https://github.com/cloudflare/cloudflare-docs/blob/production/astro.config.ts"><code>astro.config.ts</code></a>.</p>
<p>We also make two intentional decisions about this link auditing:</p>
<ul>
<li><strong>Absolute links, not relative</strong>: We enforce absolute links (<code>/style-guide/how-we-docs/metadata/</code>) and fail on relative links (<code>../metadata/</code>) to avoid time-consuming maintenance in the future. This decision also helps with find/replace work and any future platform migrations.</li>
<li><strong>No redirects</strong>: We do not consider redirects when evaluating links. We have the current source of truth, so we should utilize that truth to its fullest (as well as helping us avoid redirect chains and future maintenance).</li>
</ul>
<h3 id="external-links">External links</h3>
<p>Though external links are not good for the customer experience, they also don't change within the context of a change to your site's content. Additionally, external link checking can be time consuming and error prone, which can slow down contributions.</p>
<p>We use an external SEO tool to help flag these broken external links for us, addressing them as needed (instead of making a build fail because of them).</p>
<h3 id="anchor-links">Anchor links</h3>
<p>Anchor links do not have as dramatic as consequences of being wrong as internal links. If you have a broken anchor link, a customer will either need to manually scroll to the header or, in some cases, go to another page.</p>
<p>Because of these characteristics, we run <a href="https://github.com/cloudflare/cloudflare-docs/blob/production/.github/workflows/anchor-link-audit.yml">periodic, background checks</a> to flag broken anchor links, using the <code>htmltest</code> library.</p>
