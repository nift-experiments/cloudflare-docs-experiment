<p>Quickly view differences between versions to make sure your configurations are correct before <a href="/version-management/how-to/environments/#change-environment-version">promoting a version</a> to a new environment.</p>
<p>A common use case would be to compare the versions in staging and production to verify the changes before promoting the staging version to production.</p>
<p>To compare versions:</p>
<ol>
<li>Log in to the Cloudflare dashboard.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select your account and zone.</li>
<li>Go to <strong>Version Management</strong> &gt; <strong>Comparisons</strong>.</li>
<li>Select two different versions.</li>
<li>Select <strong>Compare</strong>.</li>
</ol>
<p>After a few seconds, the page will update automatically with a comparison on a per-product basis. The lower numbered version will always be presented on the left and the top will show you which environments the versions are assigned to so that you can ensure you are comparing the right versions.</p>
<p><img src="/assets/upstream/images/version-management/compare-versions.png" alt="View changes side-by-side between versions" /></p>
<p>Changes will be highlighted for new additions and removals for that service. Based on the comparison, you can then decide if more changes are necessary or if that new version is ready to be rolled out.</p>
