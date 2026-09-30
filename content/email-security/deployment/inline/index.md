<aside class="nb-aside note">
<h3 class="nb-aside-title" id="area-1-has-been-renamed">Area 1 has been renamed</h3>
@markup("md", "content/.markup/bodies/8506.md")
</aside>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="access-to-area-1">Access to Area 1</h3>
@markup("md", "content/.markup/bodies/8505.md")
</aside>
<p>With an <strong>Inline deployment</strong> for your <a href="/email-security/deployment/">Email Security (formerly Area 1) setup</a>, Email Security evaluates email messages before they reach a user's inbox.</p>
<p>More technically, Email Security becomes a hop in the <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/8507.md")
</div> processing chain and physically interacts with incoming email messages. Based on your policies, various messages are blocked before reaching the inbox.
<p><img src="/assets/upstream/images/email-security/deployment/inline-setup/inline-deployment-diagram.png" alt="With inline deployment, messages travel through Email Security's email filter before reaching your users." /></p>
<h2 id="benefits">Benefits</h2>
<p>When you choose an inline deployment, you get the following benefits:</p>
<ul>
<li>Messages are processed and physically blocked before delivery to a user's mailbox.</li>
<li>Your deployment is simpler, because any complex processing can happen downstream and without modification.</li>
<li>Email Security can <a href="/email-security/email-configuration/email-policies/text-addons/">modify delivered messages</a>, adding subject or body mark-ups.</li>
<li>Email Security can offer high availability and adaptive message pooling.</li>
<li>You can set up advanced handling downstream for non-quarantined messages with <a href="/email-security/reference/dispositions-and-attributes/">added <code>X-headers</code></a>.</li>
</ul>
<h2 id="limitations">Limitations</h2>
<p>Inline deployments are not without their disadvantages. If you deploy Email Security as your MX record, you will have to make changes to your DNS. If not — and you deploy Email Security after your MX record — you will have a more complex SMTP architecture.</p>
<p>Additionally, this setup may require policy duplication on multiple solutions and the Mail Transfer Agent (MTA).</p>
<h2 id="get-started">Get started</h2>
<p>For help getting started, refer to our <a href="/email-security/deployment/inline/setup/">setup guides</a>.</p>
