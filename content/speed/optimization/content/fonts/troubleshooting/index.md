<h2 id="validate-the-fonts-feature-is-working">Validate the Fonts feature is working</h2>
<p>To test that the Fonts feature is working correctly, follow these steps:</p>
<ol>
<li>With the Fonts feature disabled, navigate to your webpage and open the network panel in your browser's developer tools. For Chrome, right click on the webpage and select <strong>Inspect</strong>, which open the developer tools. Next, navigate to the <strong>Network</strong> tab within the console.</li>
<li>Reload the page.</li>
<li>In the Network tab, you should have a request to <code>fonts.googleapis.com</code>, and a request to <code>fonts.gstatic.com</code>. This means that Google Fonts are being downloaded for this page. If you do not have these requests in the list, either your webpage is not using Google Fonts, or your hosting provider might be optimizing the Google Fonts in some other way.</li>
<li><a href="/speed/optimization/content/fonts/#get-started">Enable Cloudflare Fonts</a> and wait for a few seconds.</li>
<li>In the inspect window, toggle <strong>Disable cache</strong> on and reload the page.</li>
<li>In the network panel, you should now have a request to your zone on the <code>/cf-fonts/</code> path prefix. The requests to <code>fonts.googleapis.com</code> and <code>fonts.gstatic.com</code> should have disappeared. This means the feature is working correctly.</li>
</ol>
<h2 id="feature-is-not-working">Feature is not working</h2>
<p>For the feature to work, the response HTML (when the feature is disabled) must include a link tag with <code>href</code> pointing to <code>fonts.googleapis.com</code>. You can check this on the browser by viewing the source code of the webpage. As an example of what to look for, the following link tag is for the Roboto Google Font:</p>
<pre><code class="language-html">&lt;link href=&quot;https://fonts.googleapis.com/css2?family=Roboto&amp;display=swap&quot; rel=&quot;stylesheet&quot;&gt;&#10;</code></pre>
<p>If the tag does not exist in the HTML, but you are still sure that your page is using Google Fonts, it might be that your hosting provider is optimizing your Google Fonts on the server. This can prevent Cloudflare Fonts from working properly.</p>
<h2 id="other-issues-with-cloudflare-fonts">Other issues with Cloudflare Fonts</h2>
<p>If you experience any issues or have questions while using Cloudflare Fonts, refer to the <a href="https://community.cloudflare.com/">Cloudflare Community</a> pages or contact <a href="/support/contacting-cloudflare-support/">Cloudflare Support</a> for assistance.</p>
