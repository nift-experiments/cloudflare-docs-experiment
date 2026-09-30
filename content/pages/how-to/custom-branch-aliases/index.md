<p>In this guide, you will learn how to add a custom domain (<code>staging.example.com</code>) that will point to a specific branch (<code>staging</code>) on your Pages project.</p>
<p>This will allow you to have a custom domain that will always show the latest build for a specific branch on your Pages project.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10896.md")
</aside>
<p>First, make sure that you have a successful deployment on the branch you would like to set up a custom domain for.</p>
<p>Next, add a custom domain under your Pages project for your desired custom domain, for example, <code>staging.example.com</code>.</p>
<p><img src="/assets/upstream/images/pages/how-to//pages_custom_domain-1.png" alt="Follow the instructions below to access the custom domains overview in the Pages dashboard." /></p>
<p>To do this:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select your Pages project.
3. Select **Custom domains** > **Setup a custom domain**.
4. Input the domain you would like to use, such as `staging.example.com`
5. Select **Continue** > **Activate domain**
<p><img src="/assets/upstream/images/pages/how-to//pages_custom_domain-2.png" alt="After selecting your custom domain, you will be asked to activate it." /></p>
<p>After activating your custom domain, go to <a href="https://dash.cloudflare.com/?to=/:account/:zone/dns">DNS</a> for the <code>example.com</code> zone and find the <code>CNAME</code> record with the name <code>staging</code> and change the target to include your branch alias.</p>
<p>In this instance, change <code>your-project.pages.dev</code> to <code>staging.your-project.pages.dev</code>.</p>
<p><img src="/assets/upstream/images/pages/how-to//pages_custom_domain-3.png" alt="After activating your custom domain, change the CNAME target to include your branch name." /></p>
<p>Now the <code>staging</code> branch of your Pages project will be available on <code>staging.example.com</code>.</p>
