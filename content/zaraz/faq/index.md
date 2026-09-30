<p>Below you will find answers to our most commonly asked questions. If you cannot find the answer you are looking for, refer to the <a href="https://community.cloudflare.com/">community page</a> or <a href="https://discord.cloudflare.com">Discord channel</a> to explore additional resources.</p>
<ul>
<li><a href="#general">General</a></li>
<li><a href="#tools">Tools</a></li>
<li><a href="#consent">Consent</a></li>
</ul>
<p>If you're looking for information regarding Zaraz Pricing, see the <a href="/zaraz/pricing-info/">Zaraz Pricing</a> page.</p>
<hr />
<h2 id="general">General</h2>
<h3 id="setting-up-zaraz">Setting up Zaraz</h3>
<h4 id="why-is-zaraz-not-working">Why is Zaraz not working?</h4>
<p>If you are experiencing issues with Zaraz, there could be multiple reasons behind it. First, it's important to verify that the Zaraz script is loading properly on your website.</p>
<p>To check if the script is loading correctly, follow these steps:</p>
<ol>
<li>Open your website in a web browser.</li>
<li>Open your browser's Developer Tools.</li>
<li>In the Console, type <code>zaraz</code>.</li>
<li>If you see an error message saying <code>zaraz is not defined</code>, it means that Zaraz failed to load.</li>
</ol>
<p>If Zaraz is not loading, please verify the following:</p>
<ul>
<li>The domain running Zaraz <a href="/dns/proxy-status/">is proxied by Cloudflare</a>.</li>
<li>Auto Injection is enabled in your <a href="/zaraz/reference/settings/#auto-inject-script">Zaraz Settings</a>.</li>
<li>Your website's HTML is valid and includes <code>&lt;head&gt;</code> and <code>&lt;/head&gt;</code> tags.</li>
<li>You have at least <a href="/zaraz/get-started/">one enabled tool</a> configured in Zaraz.</li>
</ul>
<h4 id="the-browser-extension-i-m-using-cannot-find-the-tool-i-have-added-why">The browser extension I'm using cannot find the tool I have added. Why?</h4>
<p>Zaraz is loading tools server-side, which means code running in the browser will not be able to see it. Running tools server-side is better for your website performance and privacy, but it also means you cannot use normal browser extensions to debug your Zaraz tools.</p>
<h4 id="i-m-seeing-some-data-discrepancies-is-there-a-way-to-check-what-data-reaches-zaraz">I'm seeing some data discrepancies. Is there a way to check what data reaches Zaraz?</h4>
<p>Yes. You can use the metrics in <a href="/zaraz/monitoring/">Zaraz Monitoring</a> and <a href="/zaraz/web-api/debug-mode/">Debug Mode</a> to help you find where in the workflow the problem occurred.</p>
<h4 id="can-i-use-zaraz-with-rocket-loader">Can I use Zaraz with Rocket Loader?</h4>
<p>We recommend disabling <a href="/speed/optimization/content/rocket-loader/">Rocket Loader</a> when using Zaraz. While Zaraz can be used together with Rocket Loader, there's usually no need to use both. Rocket Loader can sometimes delay data from reaching Zaraz, causing issues.</p>
<h4 id="is-zaraz-compatible-with-content-security-policies-csp">Is Zaraz compatible with Content Security Policies (CSP)?</h4>
<p>Yes. To learn more about how Zaraz compatibility with [<div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/10.md")
</div>](/fundamentals/reference/policies-compliances/content-security-policies/) configurations works, refer to the [Cloudflare Zaraz supports CSP](https://blog.cloudflare.com/cloudflare-zaraz-supports-csp/) blog post.
<h4 id="does-cloudflare-process-my-html-removing-existing-scripts-and-then-injecting-zaraz">Does Cloudflare process my HTML, removing existing scripts and then injecting Zaraz?</h4>
<p>Cloudflare Zaraz does not remove other third-party scripts from the page. Zaraz <a href="/zaraz/reference/settings/#auto-inject-script">can be auto-injected or not</a>, depending on your configuration, but if you have existing scripts that you intend to load with Zaraz, you should remove them.</p>
<h4 id="does-zaraz-work-with-cloudflare-s-client-side-security">Does Zaraz work with Cloudflare's client-side security?</h4>
<p>Yes. Refer to <a href="/client-side-security/">client-side security</a> (formerly known as Page Shield) for more information related to this product.</p>
<h4 id="is-there-a-way-to-prevent-zaraz-from-loading-on-specific-pages-like-under-wp-admin">Is there a way to prevent Zaraz from loading on specific pages, like under <code>/wp-admin</code>?</h4>
<p>To prevent Zaraz from loading on specific pages, refer to <a href="/zaraz/advanced/load-selectively/">Load Zaraz selectively</a>.</p>
<h4 id="how-can-i-remove-my-zaraz-configuration">How can I remove my Zaraz configuration?</h4>
<p>Resetting your Zaraz configuration will erase all of your configuration settings, including any tools, triggers, and variables you've set up. This action will disable Zaraz immediately. If you want to start over with a clean slate, you can always reset your configuration.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Settings</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to <strong>Advanced</strong>.</li>
<li>Click &quot;Reset&quot; and follow the instructions.</li>
</ol>
<h3 id="zaraz-web-api">Zaraz Web API</h3>
<h4 id="why-would-the-zaraz-ecommerce-method-returns-an-undefined-error">Why would the <code>zaraz.ecommerce()</code> method returns an undefined error?</h4>
<p>E-commerce tracking needs to be enabled in <a href="/zaraz/reference/settings/#e-commerce-tracking">the Zaraz Settings page</a> before you can start using the E-commerce Web API.</p>
<h4 id="how-would-i-trigger-pageviews-manually-on-a-single-page-application-spa">How would I trigger pageviews manually on a Single Page Application (SPA)?</h4>
<p>Zaraz comes with built-in <a href="/zaraz/reference/settings/#single-page-application-support">Single Page Application (SPA) support</a> that automatically sends pageview events when navigating through the pages of your SPA. However, if you have advanced use cases, you might want to build your own system to trigger pageviews. In such cases, you can use the internal SPA pageview event by calling <code>zaraz.spaPageview()</code>.</p>
<hr />
<h2 id="tools">Tools</h2>
<h3 id="google-analytics">Google Analytics</h3>
<h4 id="after-moving-from-google-analytics-4-to-zaraz-i-can-no-longer-see-demographics-data-why">After moving from Google Analytics 4 to Zaraz, I can no longer see demographics data. Why?</h4>
<p>You probably have enabled <strong>Hide Originating IP Address</strong> in the <a href="/zaraz/custom-actions/edit-tools-and-actions/">Settings option</a> for Google Analytics 4. This tells Zaraz to not send the IP address to Google. To have access to demographics data and anonymize your visitor's IP, you should use <a href="#i-see-two-ways-of-anonymizing-ip-address-information-on-the-third-party-tool-google-analytics-one-in-privacy-and-one-in-additional-fields-which-is-the-correct-one"><strong>Anonymize Originating IP Address</strong></a> instead.</p>
<h4 id="i-see-two-ways-of-anonymizing-ip-address-information-on-the-third-party-tool-google-analytics-one-in-privacy-and-one-in-additional-fields-which-is-the-correct-one">I see two ways of anonymizing IP address information on the third-party tool Google Analytics: one in Privacy, and one in Additional fields. Which is the correct one?</h4>
<p>There is not a correct option, as the two options available in Google Analytics (GA) do different things.</p>
<p>The &quot;Hide Originating IP Address&quot; option in <a href="/zaraz/custom-actions/edit-tools-and-actions/">Tool Settings</a> prevents Zaraz from sending the IP address from a visitor to Google. This means that GA treats Zaraz's Worker's IP address as the visitor's IP address. This is often close in terms of location, but it might not be.</p>
<p>With the <strong>Anonymize Originating IP Address</strong> available in the <a href="/zaraz/custom-actions/additional-fields/">Add field</a> option, Cloudflare sends the visitor's IP address to Google as is, and passes the 'aip' parameter to GA. This asks GA to anonymize the data.</p>
<h4 id="if-i-set-up-event-reporting-enhanced-measurements-for-google-analytics-why-does-zaraz-only-report-page-view-session-start-and-first-visit">If I set up Event Reporting (enhanced measurements) for Google Analytics, why does Zaraz only report Page View, Session Start, and First Visit?</h4>
<p>This is not a bug. Zaraz does not offer all the automatic events the normal GA4 JavaScript snippets offer out of the box. You will need to build <a href="/zaraz/custom-actions/create-trigger/">triggers</a> and <a href="/zaraz/custom-actions/">actions</a> to capture those events. Refer to <a href="/zaraz/get-started/">Get started</a> to learn more about how Zaraz works.</p>
<h4 id="can-i-set-up-custom-dimensions-for-google-analytics-with-zaraz">Can I set up custom dimensions for Google Analytics with Zaraz?</h4>
<p>Yes. Refer to <a href="/zaraz/custom-actions/additional-fields/">Additional fields</a> to learn how to send additional data to tools.</p>
<h4 id="how-do-i-attach-a-user-property-to-my-events">How do I attach a User Property to my events?</h4>
<p>In your Google Analytics 4 action, select <strong>Add field</strong> &gt; <strong>Add custom field...</strong> and enter a field name that starts with <code>up.</code> — for example, <code>up.name</code>. This will make Zaraz send the field as a User Property and not as an Event Property.</p>
<h4 id="how-can-i-enable-google-consent-mode-signals">How can I enable Google Consent Mode signals?</h4>
<p>Zaraz has built-in support for Google Consent Mode v2. Learn more on how to use it in <a href="/zaraz/advanced/google-consent-mode/">Google Consent Mode page</a>.</p>
<h3 id="facebook-pixel">Facebook Pixel</h3>
<h4 id="if-i-set-up-facebook-pixel-on-my-zaraz-account-why-am-i-not-seeing-data-coming-through">If I set up Facebook Pixel on my Zaraz account, why am I not seeing data coming through?</h4>
<p>It can take between 15 minutes to several hours for data to appear on Facebook's interface, due the way Facebook Pixel works. You can also use <a href="/zaraz/web-api/debug-mode/">debug mode</a> to confirm that data is being properly sent from your Zaraz account.</p>
<h3 id="google-ads">Google Ads</h3>
<h4 id="what-is-the-expected-format-for-conversion-id-and-conversion-label">What is the expected format for Conversion ID and Conversion Label</h4>
<p>Conversion ID and Conversion Label are usually provided by Google Ads as a &quot;gtag script&quot;. Here's an example for a $1 USD conversion:</p>
<pre><code class="language-js">gtag(&quot;event&quot;, &quot;conversion&quot;, {&#10;	send_to: &quot;AW-123456789/AbC-D_efG-h12_34-567&quot;,&#10;	value: 1.0,&#10;	currency: &quot;USD&quot;,&#10;});&#10;</code></pre>
<p>The Conversion ID is the first part of <code>send_to</code> parameter, without the <code>AW-</code>. In the above example it would be <code>123456789</code>. The Conversion Label is the second part of the <code>send_to</code> parameter, therefore <code>AbC-D_efG-h12_34-567</code> in the above example. When setting up your Google Ads conversions through Zaraz, take the information from the original scripts you were asked to implement.</p>
<h3 id="custom-html">Custom HTML</h3>
<h4 id="can-i-use-google-tag-manager-together-with-zaraz">Can I use Google Tag Manager together with Zaraz?</h4>
<p>You can load Google Tag Manager using Zaraz, but it is not recommended. Tools configured inside Google Tag Manager cannot be optimized by Zaraz, and cannot be restricted by the Zaraz privacy controls. In addition, Google Tag Manager could slow down your website because it requires additional JavaScript, and its rules are evaluated client-side. If you are currently using Google Tag Manager, we recommend replacing it with Zaraz by configuring your tags directly as Zaraz tools.</p>
<h4 id="why-should-i-prefer-a-native-tool-integration-instead-of-an-html-snippet">Why should I prefer a native tool integration instead of an HTML snippet?</h4>
<p>Adding a tool to your website via a native Zaraz integration is always better than using an HTML snippet. HTML snippets usually depends on additional client-side requests, and require client-side code execution, which can slow down your website. They are often a security risk, as they can be hacked. Moreover, it can be very difficult to control their affect on the privacy of your visitors. Tools included in the Zaraz library are not suffering from these issues - they are fast, executed at the edge, and be controlled and restricted because they are sandboxed.</p>
<h4 id="how-can-i-set-my-custom-html-to-be-injected-just-once-in-my-single-page-app-spa-website">How can I set my Custom HTML to be injected just once in my Single Page App (SPA) website?</h4>
<p>If you have enabled &quot;Single Page Application support&quot; in Zaraz Settings, your Custom HTML code may be unnecessarily injected every time a new SPA page is loaded. This can result in duplicates. To avoid this, go to your Custom HTML action and select the &quot;Add Field&quot; option. Then, add the &quot;Ignore SPA&quot; field and enable the toggle switch. Doing so will prevent your code from firing on every SPA pageview and ensure that it is injected only once.</p>
<h3 id="other-tools">Other tools</h3>
<h4 id="what-if-i-want-to-use-a-tool-that-is-not-supported-by-zaraz">What if I want to use a tool that is not supported by Zaraz?</h4>
<p>The Zaraz engineering team is adding support to new tools all the time. You can also refer to the <a href="https://community.cloudflare.com/c/developers/integrationrequest/68">community space</a> to ask for new integrations.</p>
<h4 id="i-cannot-get-a-tool-to-load-when-the-website-is-loaded-do-i-have-to-add-code-to-my-website">I cannot get a tool to load when the website is loaded. Do I have to add code to my website?</h4>
<p>If you proxy your domain through Cloudflare, you do not need to add any code to your website. By default, Zaraz includes an automated <code>Pageview</code> trigger. Some tools, like Google Analytics, automatically add a <code>Pageview</code> action that uses this trigger. With other tools, you will need to add it manually. Refer to <a href="/zaraz/get-started/">Get started</a> for more information.</p>
<h4 id="i-am-a-vendor-how-can-i-integrate-my-tool-with-zaraz">I am a vendor. How can I integrate my tool with Zaraz?</h4>
<p>The Zaraz team is working with third-party vendors to build their own Zaraz integrations using the Zaraz SDK. To request a new tool integration, or to collaborate on our SDK, contact us at <a href="mailto:zaraz@cloudflare.com">zaraz@cloudflare.com</a>.</p>
<hr />
<h2 id="consent">Consent</h2>
<h3 id="how-do-i-show-the-consent-modal-again-to-all-users">How do I show the consent modal again to all users?</h3>
<p>In such a case, you can change the cookie name in the <em>Consent cookie name</em> field in the Zaraz Consent configuration. This will cause the consent modal to reappear for all users. Make sure to use a cookie name that has not been used for Zaraz on your site.</p>
