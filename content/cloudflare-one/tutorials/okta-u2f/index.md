<p>Many identity providers, like Okta, support multiple multifactor authentication (MFA) options simultaneously. For example, Okta will allow you to login with your password and a temporary code generated in an app or a U2F hard key like a Yubikey.</p>
<p>Some second factor methods are more resistant to phishing. U2F options require you to have access to a physical device, also known as a hardware key. Without that key, a user cannot impersonate you even if they have your password. You can build rules in Cloudflare Access to require that users authenticate with a hardware key - even if your provider supports multiple options. When users login with a less secure option, like an app-based code, Access will block them.</p>
<p><strong>This tutorial covers how to:</strong></p>
<ul>
<li>Integrate Cloudflare Access with Okta</li>
<li>Configure Okta for U2F enrollment</li>
<li>Build an <a href="/cloudflare-one/access-controls/policies/">Access policy</a> that require users login with a hardware key</li>
<li>Specify that policy to apply to certain Access applications</li>
</ul>
<p>The first two sections of this tutorial link to guides to set up Cloudflare Access and integrate Okta. If you already use Cloudflare Access with Okta, you can skip ahead to the fourth section.</p>
<p><strong>Time to complete:</strong></p>
<p>20 minutes</p>
<hr />
<h2 id="configure-cloudflare-access">Configure Cloudflare Access</h2>
<p>Before you begin, you'll need to follow <a href="/cloudflare-one/setup/">these instructions</a> to set up Cloudflare Access in your account. The hardware key feature is available on any plan, including the free plan.</p>
<h2 id="integrate-okta">Integrate Okta</h2>
<p>Follow <a href="/cloudflare-one/integrations/identity-providers/okta/">these instructions</a> to integrate Okta with your Cloudflare Access account. Once integrated, Access will be able to apply rules using identity, group membership, and multifactor method from Okta.</p>
<h2 id="configure-okta-for-u2f">Configure Okta for U2F</h2>
<p>An Okta administrator in your organization must first <a href="https://help.okta.com/en/prod/Content/Topics/Security/MFA.htm">enable U2F support</a> in your Okta account <strong>and</strong> <a href="https://help.okta.com/en/prod/Content/Topics/Security/healthinsight/required-factors.htm">configure users</a> to be prompted for it. This is a global setting; if your account has already configured U2F, you do not need to do anything unique to use it with Cloudflare Access.</p>
<h2 id="test-u2f-in-access">Test U2F in Access</h2>
<p>You can begin building U2F policies by testing your Okta integration.</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Access settings</strong>.</li>
<li>In <strong>Manage your App Launcher</strong>, select <strong>Manage</strong>.</li>
<li>Choose <strong>Login methods</strong>.</li>
<li>Choose the row for Okta and select <strong>Test</strong>.</li>
</ol>
<p>Cloudflare Access will prompt you to login with your Okta account. For the purposes of the test, use a second factor option like an app-based code. Okta will return <code>amr</code> values to Cloudflare Access - these are standard indicators of multifactor methods shared between identity control systems.</p>
<p>The <code>mfa</code> value is sent by Okta to tell Cloudflare Access that you used a multifactor authentication option. The <code>pwd</code> value indicates you used a password. In this example, the <code>otp</code> value is sent because the user authenticatd with an app-based code.</p>
<p>You can test with a hardkey by logging out of Okta and returning to the list of providers in Access. Select <strong>Test</strong> again, but this time use your hardware key as a second factor. Cloudflare Access will now see Okta share <code>hwk</code> in the <code>amr</code> fields.</p>
<p><img src="/assets/upstream/images/cloudflare-one/zero-trust-security/require-yubikey/with-hwk.png" alt="Test MFA" /></p>
<h2 id="build-a-zero-trust-policy-to-require-u2f">Build a Zero Trust policy to require U2F</h2>
<p>You can use this information to build a rule in Access. Go to the <code>Applications</code> list in the Cloudflare Access section of the dashboard. Choose an application that you have already built or create a new one. This example adds the requirement to an existing application.</p>
<p>Select <strong>Edit</strong> to edit the existing <code>Allow</code> rule.</p>
<p>Add a <code>Require</code> rule and select <code>Authentication Method</code> from the list. Choose <code>hwk</code> as the required <code>Authentication Method</code>. Select <strong>Save rule</strong>.</p>
<p><img src="/assets/upstream/images/cloudflare-one/zero-trust-security/require-yubikey/require-hwk.png" alt="Require Rule" /></p>
<p>Optional: you can also configure Cloudflare Access to only show users Okta for this application if you have multiple other providers integrated. In the <code>Authentication</code> Tab, choose <code>Okta</code> as the only option to show users.</p>
<h2 id="testing-the-rule">Testing the rule</h2>
<p>You can now test the rule. Visit the application and attempt to login using an app-based code or method other than a hardware security key. Access will block the attempt.</p>
<p><img src="/assets/upstream/images/cloudflare-one/zero-trust-security/require-yubikey/blocked-user.png" alt="Blocked" /></p>
<p>If you sign out of Okta, and reattempt with a hardware key, Access will then allow the connection.</p>
