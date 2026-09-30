<h2 id="lifecycle">Lifecycle</h2>
<p>Unless otherwise stated in the code repository, Cloudflare only provides active support for the latest major version of a library or tool. The exception to this policy is for critical security fixes, which will be reviewed on a case-by-case basis and take the vulnerability, impact, and mitigation required into consideration.</p>
<p>We provide three primary stages of development: early access, active support, and end of life.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8774.md")
</aside>
<h3 id="early-access">Early access</h3>
<p>During this stage, Cloudflare makes SDK changes available that we are seeking feedback on prior to releasing for general usage. Early access will  often include warning labels or caveats on functionality that is subject to change without notice. In general, early access SDKs are not suitable for production systems unless explicitly mentioned.</p>
<h3 id="active-support">Active support</h3>
<p>During the active support stage, planned changes and support are offered for the library or tool.</p>
<h3 id="end-of-life">End of life</h3>
<p>During the end of life stage, a new major version of the library or tool is released and Cloudflare marks the previous major version as no longer receiving improvements or bug fixes. If you continue to run end of life versions, support will be very limited.</p>
<p><img src="/assets/upstream/images/fundamentals/support-policy.png" alt="All lifecycle stages and their relation to one another" title="All lifecycle stages and their relation to one another" /></p>
<h2 id="previous-or-end-of-life-versions">Previous or end of life versions</h2>
<p>While Cloudflare cannot provide support for all older versions of our libraries or tools, we do not remove those versions so they can continued to be used without direct support.</p>
<h2 id="versioning">Versioning</h2>
<p>The SDK ecosystem follows semantic versioning, which defines versions as follows:</p>
<ul>
<li>MAJOR version when there are backward-incompatible changes made.</li>
<li>MINOR version when functionality is added in a backward compatible-manner.</li>
<li>PATCH version for backward-compatible bug fixes (without any improvements).</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/8773.md")
</aside>
<p>Depending on your needs, you should ensure your application's package manager versioning is configured correctly. At a minimum, restrict installation to the current major version of the library or tool you are using to prevent any major version upgrades occurring automatically.</p>
<h2 id="migration">Migration</h2>
<p>Where possible, Cloudflare provides an automated approach to performing major version upgrades to limit the disruption using codemods. Review the library or tool-specific release notes for how to use these migration tools.</p>
<p>Alongside the automatic migration approach, we provide documentation on the changes that have taken place in case you need to make the changes manually.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="https://semver.org/">Semantic versioning definitions</a></li>
<li><a href="/terraform/">Cloudflare's Terraform documentation</a></li>
</ul>
