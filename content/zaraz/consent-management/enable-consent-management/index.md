<ol>
<li>In the Cloudflare dashboard, go to the <strong>Consent</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Turn on **Enable Consent Management**.
3. In **Consent modal text** fill in any legal information required in your country. Use HTML code to format your information as you would in any other HTML editor.
4. Under **Purposes**, select **Add new Purpose**. Give your new purpose a name and a description. Purposes are the reasons for using third-party tools in your website.
5. In **Assign purpose to tools**, match tools to purposes by selecting one of the purposes previously created from the drop-down menu. Do this for all your tools.
6. Select **Save**.
<p>Your Consent Management platform is ready. Your website should now display a modal asking for consent for the tools you have configured.</p>
<h2 id="adding-different-languages">Adding different languages</h2>
<p>In your Zaraz consent settings, you can add your consent modal text and purposes in various languages.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Consent</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select a default language of your choice. The default setting is English.
3. In **Consent modal text** and **Purposes**, you can select different languages and add translations.
<h2 id="overriding-the-consent-modal-language">Overriding the consent modal language</h2>
<p>By default, the Zaraz Consent Management Platform will try to match the language of the consent modal with the language requested by the browser, using the <code>Accept-Language</code> HTTP header.
If, for any reason, you would like to force the consent modal language to a specific one, you can use the <code>zaraz.set</code> Web API to define the default <code>__zarazConsentLanguage</code> value.</p>
<p>Below is an example that forces the language shown to be American English.</p>
<pre><code class="language-html">&lt;script&gt;&#10;  zaraz.set(&#x27;__zarazConsentLanguage&#x27;, &#x27;en-US&#x27;)&#10;&lt;/script&gt;&#10;</code></pre>
<h2 id="next-steps">Next steps</h2>
<p>If the default consent modal does not suit your website's design, you can use the <a href="/zaraz/consent-management/custom-css/">Custom CSS tool</a> to add your own custom design.</p>
