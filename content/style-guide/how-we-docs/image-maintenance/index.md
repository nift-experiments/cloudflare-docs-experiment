<p>Though valuable for user understanding, images are difficult to maintain. We have a few strategies that we use to help make this easier.</p>
<h2 id="guidelines">Guidelines</h2>
<p>We support a few different types of images in our docs, including:</p>
<ul>
<li><a href="/style-guide/documentation-content-strategy/component-attributes/images-and-diagrams/#diagrams">Diagrams</a></li>
<li><a href="/style-guide/documentation-content-strategy/component-attributes/images-and-diagrams/#screenshots">Screenshots</a></li>
</ul>
<p>Of these, we prefer Mermaid diagrams because they are searchable and easily changeable. The &quot;cost&quot; of updating a Mermaid diagram is much lower than re-taking a screenshot or working with a designer to update a diagram.</p>
<h2 id="maintenance">Maintenance</h2>
<p>The best way to improve image maintenance is to avoid using them.</p>
<p>The other way to streamline maintenance is to remove images that are no longer referenced in your documentation. This pattern becomes particularly helpful if you need to audit images for UI changes or leaked information, because then you are not wasting time looking at unused images too.</p>
<p>We do that through a combination of GitHub actions.</p>
<h3 id="flag-unused-images">Flag unused images</h3>
<p>We have a specific GitHub action to <a href="https://github.com/cloudflare/cloudflare-docs/blob/production/.github/workflows/image-audit.yml">flag unused images</a>.</p>
<p>What the GitHub action does is:</p>
<ol>
<li>Finds all <code>.png</code> or <code>.svg</code> files in our content.</li>
<li>Checks to see if those files are referenced in any of our MDX files.</li>
<li>Creates a <a href="https://github.com/cloudflare/cloudflare-docs/issues/23343">GitHub issue</a> if there are unreferenced files.</li>
</ol>
<h3 id="evaluate-image-paths">Evaluate image paths</h3>
<p>In combination with <a href="#flag-unused-images">flagging unused images</a>, we also have logic in our <a href="https://github.com/cloudflare/cloudflare-docs/blob/production/astro.config.ts">build process</a> to validate image paths.</p>
<pre><code class="language-ts">export default defineConfig({&#10;	site: &quot;https://developers.cloudflare.com&quot;,&#10;	markdown: {&#10;		smartypants: false,&#10;		remarkPlugins: [remarkValidateImages],&#10;		rehypePlugins: [&#10;			rehypeMermaid,&#10;			rehypeExternalLinks,&#10;			rehypeHeadingSlugs,&#10;			rehypeAutolinkHeadings,&#10;			// @ts-expect-error plugins types are outdated but functional&#10;			rehypeTitleFigure,&#10;			rehypeShiftHeadings,&#10;		],&#10;	},&#10;</code></pre>
<p>This ensures that the build-time <code>nimbus/image-ref</code> lint rule validates all image paths. If the path does not exist, we throw an error and prevent the site from building.</p>
<p>When paired with <a href="#flag-unused-images">flagging unused images</a>, this path validation ensures that a tech writer can safely delete unused files in a pull request. So long as the site builds correctly, you have only deleted image files that are not referenced anywhere.</p>
