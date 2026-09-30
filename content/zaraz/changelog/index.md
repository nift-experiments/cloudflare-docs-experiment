<h2 id="2025-02-11">2025-02-11</h2><ul>
<li><strong>Logpush</strong>: Add Logpush support for Zaraz</li>
</ul><h2 id="2024-12-16">2024-12-16</h2><ul>
<li><strong>Consent Management</strong>: Allow forcing the consent modal language</li>
</ul>
<ul>
<li><strong>Zaraz Debugger</strong>: Log the response status and body for server-side requests</li>
</ul>
<ul>
<li><strong>Monitoring</strong>: Introduce &quot;Advanced Monitoring&quot; with new reports such as geography, user timeline, funnel, retention and more</li>
<li><strong>Monitoring</strong>: Show information about server-side requests success rate</li>
</ul>
<ul>
<li><strong>Zaraz Types</strong>: Update the <code>zaraz-types</code> package</li>
<li><strong>Custom HTML Managed Component</strong>: Apply syntax highlighting for inlined JavaScript code</li>
</ul><h2 id="2024-11-12">2024-11-12</h2><ul>
<li><strong>Facebook Component</strong>: Update to version 21 of the API, and fail gracefully when e-commerce payload doesn't match schema</li>
</ul>
<ul>
<li><strong>Zaraz Monitoring</strong>: Show all response status codes from the Zaraz server-side requests in the dashboard</li>
<li><strong>Zaraz Debugger</strong>: Fix a bug that broke the display when Custom HTML included backticks</li>
<li><strong>Context Enricher</strong>: It's now possible to programatically edit the Zaraz <code>config</code> itself, in addition to the <code>system</code> and <code>client</code> objects</li>
<li><strong>Rocker Loader</strong>: Issues with using Zaraz next to Rocket Loader were fixed</li>
<li><strong>Automatic Actions</strong>: The tools setup flow now fully supports configuring Automatic Actions</li>
<li><strong>Bing Managed Component</strong>: Issues with setting the currency field were fixed</li>
<li><strong>Improvement</strong>: The allowed size for a Zaraz config was increased by 250x</li>
<li><strong>Improvement</strong>: The Zaraz runtime should run faster due to multiple code optimizations</li>
<li><strong>Bugfix</strong>: Fixed an issue that caused the dashboard to sometimes show &quot;E-commerce&quot; option for tools that do not support it</li>
</ul><h2 id="2024-09-17">2024-09-17</h2><ul>
<li><strong>Automatic Actions</strong>: E-commerce support is now integrated with Automatic Actions</li>
<li><strong>Consent Management</strong>: Support styling the Consent Modal when CSP is enabled</li>
<li><strong>Consent Management</strong>: Fix an issue that could cause tools to load before consent was granted when TCF is enabled</li>
<li><strong>Zaraz Debugger</strong>: Remove redundant messages related to empty values</li>
<li><strong>Amplitude Managed Component</strong>: Respect the EU endpoint setting</li>
</ul><h2 id="2024-08-23">2024-08-23</h2><ul>
<li><strong>Automatic Actions</strong>: Automatic Event Tracking is now fully available</li>
<li><strong>Consent Management</strong>: Fixed issues with rendering the Consent modal on iOS</li>
<li><strong>Zaraz Debugger</strong>: Remove redundant messages related to <code>__zarazEcommerce</code></li>
<li><strong>Zaraz Debugger</strong>: Fixed bug that prevented the debugger to load when certain Custom HTML tools were used</li>
</ul><h2 id="2024-08-15">2024-08-15</h2><ul>
<li><strong>Automatic Actions</strong>: Automatic Pageview tracking is now fully available</li>
<li><strong>Google Analytics 4</strong>: Support Google Consent signals when using e-commerce tracking</li>
<li><strong>HTTP Events API</strong>: Ignore bot score detection on the HTTP Events API endpoint</li>
<li><strong>Zaraz Debugger</strong>: Show client-side network requests initiated by Managed Components</li>
</ul><h2 id="2024-08-12">2024-08-12</h2><ul>
<li><strong>Automatic Actions</strong>: New tools now support Automatic Pageview tracking</li>
<li><strong>HTTP Events API</strong>: Respect Google consent signals</li>
</ul><h2 id="2024-07-23">2024-07-23</h2><ul>
<li><strong>Embeds</strong>: Add support for server-side rendering of X (Twitter) and Instagram embeds</li>
<li><strong>CSP Compliance</strong>: Remove <code>eval</code> dependency</li>
<li><strong>Google Analytics 4 Managed Component</strong>: Allow customizing the document title and client ID fields</li>
<li><strong>Custom HTML Managed Component</strong>: Scripts included in a Custom HTML will preserve their running order</li>
<li><strong>Google Ads Managed Component</strong>: Allow linking data with Google Analytics 4 instances</li>
<li><strong>TikTok Managed Component</strong>: Use the new TikTok Events API v2</li>
<li><strong>Reddit Managed Component</strong>: Support custom events</li>
<li><strong>Twitter Managed Component</strong>: Support setting the <code>event_id</code>, using custom fields, and improve conversion tracking</li>
<li><strong>Bugfix</strong>: Cookie life-time cannot exceed one year anymore</li>
<li><strong>Bugfix</strong>: Zaraz Debugger UI does not break when presenting really long lines of information</li>
</ul><h2 id="2024-06-21">2024-06-21</h2><ul>
<li><strong>Dashboard</strong>: Add an option to disable the automatic <code>Pageview</code> event</li>
</ul><h2 id="2024-06-18">2024-06-18</h2><ul>
<li><strong>Amplitude Managed Component</strong>: Allow users to choose data center</li>
<li><strong>Bing Managed Component</strong>: Fix e-commerce events handling</li>
<li><strong>Google Analytics 4 Managed Component</strong>: Mark e-commerce events as conversions</li>
<li><strong>Consent Management</strong>: Fix IAB Consent Mode tools not showing with purposes</li>
</ul><h2 id="2024-05-03">2024-05-03</h2><ul>
<li><strong>Dashboard</strong>: Add setting for Google Consent mode default</li>
<li><strong>Bugfix</strong>: Cookie values are now decoded</li>
<li><strong>Bugfix</strong>: Ensure context enricher worker can access the <code>context.system.consent</code> object</li>
<li><strong>Google Ads Managed Component</strong>: Add conversion linker on pageviews without sending a pageview event</li>
<li><strong>Pinterest Conversion API Managed Component</strong>: Bugfix handling of partial e-commerce event payloads</li>
</ul><h2 id="2024-04-19">2024-04-19</h2><ul>
<li><strong>Instagram Managed Component</strong>: Improve performance of Instagram embeds</li>
<li><strong>Mixpanel Managed Component</strong>: Include <code>gclid</code> and <code>fbclid</code> values in Mixpanel requests if available</li>
<li><strong>Consent Management</strong>: Ensure consent platform is enabled when using IAB TCF compliant mode when there's at least one TCF-approved vendor configured</li>
<li><strong>Bugfix</strong>: Ensure track data payload keys take priority over preset-keys when using enrich-payload feature for custom actions</li>
</ul><h2 id="2024-04-08">2024-04-08</h2><ul>
<li><strong>Consent Management</strong>: Add <code>consent</code> object to <code>context.system</code> for finer control over consent preferences</li>
<li><strong>Consent Management</strong>: Add support for IAB-compliant consent mode</li>
<li><strong>Consent Management</strong>: Add &quot;zarazConsentChoicesUpdated&quot; event</li>
<li><strong>Consent Management</strong>: Modal now respects system dark mode prefs when present</li>
<li><strong>Google Analytics 4 Managed Component</strong>: Add support for Google Consent Mode v2</li>
<li><strong>Google Ads Managed Component</strong>: Add support for Google Consent Mode v2</li>
<li><strong>Twitter Managed Component</strong>: Enable tweet embeds</li>
<li><strong>Bing Managed Component</strong>: Support running without setting cookies</li>
<li><strong>Bugfix</strong>: <code>client.get</code> for Custom Managed Components fixed</li>
<li><strong>Bugfix</strong>: Prevent duplicate pageviews in monitoring after consent granting</li>
<li><strong>Bugfix</strong>: Prevent Managed Component routes from blocking origin routes unintentionally</li>
</ul><h2 id="2024-02-15">2024-02-15</h2><ul>
<li><strong>Single Page Applications</strong>: Introduce <code>zaraz.spaPageview()</code> for manually triggering SPA pageviews</li>
<li><strong>Pinterest Managed Component</strong>: Add ecommerce support</li>
<li><strong>Google Ads Managed Component</strong>: Append url and rnd params to pagead/landing endpoint</li>
<li><strong>Bugfix</strong>: Add noindex robots headers for Zaraz GET endpoint responses</li>
<li><strong>Bugfix</strong>: Gracefully handle responses from custom Managed Components without mapped endpoints</li>
</ul><h2 id="2024-02-05">2024-02-05</h2><ul>
<li><strong>Dashboard</strong>: rename &quot;tracks&quot; to &quot;events&quot; for consistency</li>
<li><strong>Pinterest Conversion API Managed Component</strong>: update parameters sent to api</li>
<li><strong>HTTP Managed Component</strong>: update _settings prefix usage handling</li>
<li><strong>Bugfix</strong>: better minification of client-side js</li>
<li><strong>Bugfix</strong>: fix bug where anchor link click events were not bubbling when using click listener triggers</li>
<li><strong>API update</strong>: begin migration support from deprecated <code>tool.neoEvents</code> array to <code>tool.actions</code> object config schema migration</li>
</ul><h2 id="2023-12-19">2023-12-19</h2><ul>
<li><strong>Google Analytics 4 Managed Component</strong>: Fix Google Analytics 4 average engagement time metric.</li>
</ul><h2 id="2023-11-13">2023-11-13</h2><ul>
<li><strong>HTTP Request Managed Component</strong>: Re-added <code>__zarazTrack</code> property.</li>
</ul><h2 id="2023-10-31">2023-10-31</h2><ul>
<li><strong>Google Analytics 4 Managed Component</strong>: Remove <code>debug_mode</code> key if falsy or <code>false</code>.</li>
</ul><h2 id="2023-10-26">2023-10-26</h2><ul>
<li><strong>Custom HTML</strong>: Added support for non-JavaScript script tags.</li>
</ul><h2 id="2023-10-20">2023-10-20</h2><ul>
<li><strong>Bing Managed Component</strong>: Fixed an issue where some events were not being sent to Bing even after being triggered.</li>
<li><strong>Dashboard</strong>: Improved welcome screen for new Zaraz users.</li>
</ul><h2 id="2023-10-03">2023-10-03</h2><ul>
<li><strong>Bugfix</strong>: Fixed an issue that prevented some server-side requests from arriving to their destination</li>
<li><strong>Google Analytics 4 Managed Component</strong>: Add support for <code>dbg</code> and <code>ir</code> fields.</li>
</ul><h2 id="2023-09-13">2023-09-13</h2><ul>
<li><strong>Consent Management</strong>: Add support for custom button translations.</li>
<li><strong>Consent Management</strong>: Modal stays fixed when scrolling.</li>
<li><strong>Google Analytics 4 Managed Component</strong>: <code>hideOriginalIP</code> and <code>ga-audiences</code> can be set from tool event.</li>
</ul><h2 id="2023-09-11">2023-09-11</h2><ul>
<li><strong>Reddit Managed Component</strong>: Support new &quot;Account ID&quot; formats (e.g. &quot;ax_xxxxx&quot;).</li>
</ul><h2 id="2023-09-06">2023-09-06</h2><ul>
<li><strong>Consent Management</strong>: Consent cookie name can now be customized.</li>
</ul><h2 id="2023-09-05">2023-09-05</h2><ul>
<li><strong>Segment Managed Component</strong>: API Endpoint can be customized.</li>
</ul><h2 id="2023-08-21">2023-08-21</h2><ul>
<li><strong>TikTok Managed Component</strong>: Support setting <code>ttp</code> and <code>event_id</code>.</li>
<li><strong>Consent Management</strong>: Accessibility improvements.</li>
<li><strong>Facebook Managed Component</strong>: Support for using &quot;Limited Data Use&quot; features.</li>
</ul>
