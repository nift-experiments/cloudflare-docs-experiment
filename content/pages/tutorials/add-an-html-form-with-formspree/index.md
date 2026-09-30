<p>Almost every website, whether it is a simple HTML portfolio page or a complex JavaScript application, will need a form to collect user data. <a href="https://formspree.io">Formspree</a> is a back-end service that handles form processing and storage, allowing developers to include forms on their website without writing server-side code or functions.</p>
<p>In this tutorial, you will create a <code>&lt;form&gt;</code> using plain HTML and CSS and add it to a static HTML website hosted on Cloudflare Pages. Refer to the <a href="/pages/get-started/">Get started guide</a> to familiarize yourself with the platform. You will use Formspree to collect the submitted data and send out email notifications when new submissions arrive, without requiring any JavaScript or back-end coding.</p>
<h2 id="setup">Setup</h2>
<p>To begin, create a <a href="https://repo.new/">new GitHub repository</a>. Then create a new local directory on your machine, initialize git, and attach the GitHub location as a remote destination:</p>
<pre><code class="language-sh">&#35; create new directory&#10;mkdir new-project&#10;&#35; enter new directory&#10;cd new-project&#10;&#35; initialize git&#10;git init&#10;&#35; attach remote&#10;git remote add origin git@github.com:&lt;username&gt;/&lt;repo&gt;.git&#10;&#35; change default branch name&#10;git branch -M main&#10;</code></pre>
<p>You may now begin working in the <code>new-project</code> directory you created.</p>
<h2 id="the-website-markup">The website markup</h2>
<p>You will only be using plain HTML for this example project. The home page will include a Contact Us form that accepts a name, email address, and message.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10867.md")
</aside>
<p>The form code:</p>
<pre><code class="language-html">&lt;form method=&quot;POST&quot; action=&quot;/&quot;&gt;&#10;	&lt;label for=&quot;name&quot;&gt;Full Name&lt;/label&gt;&#10;	&lt;input id=&quot;name&quot; type=&quot;text&quot; name=&quot;name&quot; pattern=&quot;[A-Za-z]+&quot; required /&gt;&#10;&#10;	&lt;label for=&quot;email&quot;&gt;Email Address&lt;/label&gt;&#10;	&lt;input id=&quot;email&quot; type=&quot;email&quot; name=&quot;email&quot; required /&gt;&#10;&#10;	&lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;&#10;	&lt;textarea id=&quot;message&quot; name=&quot;message&quot; required&gt;&lt;/textarea&gt;&#10;&#10;	&lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;&#10;&lt;/form&gt;&#10;</code></pre>
<p>The <code>action</code> attribute determines where the form data is sent. You will update this later to send form data to Formspree. All <code>&lt;input&gt;</code> tags must have a unique <code>name</code> in order to capture the user's data. The <code>for</code> and <code>id</code> values must match in order to link the <code>&lt;label&gt;</code> with the corresponding <code>&lt;input&gt;</code> for accessibility tools like screen readers.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10866.md")
</aside>
<p>To add this form to your website, first, create a <code>public/index.html</code> in your project directory. The <code>public</code> directory should contain all front-end assets, and the <code>index.html</code> file will serve as the home page for the website.</p>
<p>Copy and paste the following content into your <code>public/index.html</code> file, which includes the above form:</p>
<pre><code class="language-html">&lt;html lang=&quot;en&quot;&gt;&#10;	&lt;head&gt;&#10;		&lt;meta charset=&quot;utf8&quot; /&gt;&#10;		&lt;title&gt;Form Demo&lt;/title&gt;&#10;		&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,initial-scale=1&quot; /&gt;&#10;	&lt;/head&gt;&#10;	&lt;body&gt;&#10;		&lt;!-- the form from above --&gt;&#10;&#10;		&lt;form method=&quot;POST&quot; action=&quot;/&quot;&gt;&#10;			&lt;label for=&quot;name&quot;&gt;Full Name&lt;/label&gt;&#10;			&lt;input id=&quot;name&quot; type=&quot;text&quot; name=&quot;name&quot; pattern=&quot;[A-Za-z]+&quot; required /&gt;&#10;&#10;			&lt;label for=&quot;email&quot;&gt;Email Address&lt;/label&gt;&#10;			&lt;input id=&quot;email&quot; type=&quot;email&quot; name=&quot;email&quot; required /&gt;&#10;&#10;			&lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;&#10;			&lt;textarea id=&quot;message&quot; name=&quot;message&quot; required&gt;&lt;/textarea&gt;&#10;&#10;			&lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;&#10;		&lt;/form&gt;&#10;	&lt;/body&gt;&#10;&lt;/html&gt;&#10;</code></pre>
<p>Now you have an HTML document containing a Contact Us form with several fields for the user to fill out. However, you have not yet set the <code>action</code> attribute to a server that can handle the form data. You will do this in the next section of this tutorial.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="github-repository">GitHub Repository</h3>
@markup("md", "content/.markup/bodies/10865.md")
</aside>
<h2 id="the-formspree-back-end">The Formspree back end</h2>
<p>The HTML form is complete, however, when the user submits this form, the data will be sent in a <code>POST</code> request to the <code>/</code> URL. No server exists to process the data at that URL, so it will cause an error. To fix that, create a new Formspree form, and copy its unique URL into the form's <code>action</code>.</p>
<p>To create a Formspree form, sign up for <a href="https://formspree.io/register">an account on Formspree</a>.</p>
<p>Next, create a new form with the <strong>+ New form</strong> button. Name it <code>Contact-us form</code> and update the recipient email to an email where you wish to receive your form submissions. Then select <strong>Create Form</strong>.</p>
<p><img src="/assets/upstream/images/pages/tutorials/new-form-dialog.png" alt="Creating a Formspree form" /></p>
<p>You will then be presented with instructions on how to integrate your new form.</p>
<p><img src="/assets/upstream/images/pages/tutorials/form-endpoint.png" alt="Formspree endpoint" /></p>
<p>Copy the <code>Form Endpoint</code> URL and paste it into the <code>action</code> attribute of the form you created above.</p>
<pre><code class="language-html">&lt;form method=&quot;POST&quot; action=&quot;https://formspree.io/f/mqldaqwx&quot;&gt;&#10;	&lt;!-- replace with your own formspree endpoint --&gt;&#10;&lt;/form&gt;&#10;</code></pre>
<p>Now when you submit your form, you should be redirected to a Thank You page. The form data will be submitted to your account on <a href="https://formspree.io/">Formspree.io</a>.</p>
<p>You can now adjust your form processing logic to change the <a href="https://help.formspree.io/hc/en-us/articles/360012378333--Thank-You-redirect">redirect page</a>, update the <a href="https://help.formspree.io/hc/en-us/articles/115008379348-Changing-a-form-email-address">notification email address</a>, or add plugins like <a href="https://help.formspree.io/hc/en-us/articles/360036563573-Use-Google-Sheets-to-send-your-submissions-to-a-spreadsheet">Google Sheets</a>, <a href="https://help.formspree.io/hc/en-us/articles/360045648933-Send-Slack-notifications">Slack</a> and more.</p>
<p>For more help setting up Formspree, refer to the following resources:</p>
<ul>
<li>For general help with Formspree, refer to the <a href="https://help.formspree.io/hc/en-us">Formspree help site</a>.</li>
<li>For examples and inspiration for your own HTML forms, review the <a href="https://formspree.io/library">Formspree form library</a>.</li>
<li>For tips on integrating Formspree with popular platforms like Next.js, Gatsby and Eleventy, refer to the <a href="https://formspree.io/guides">Formspree guides</a>.</li>
</ul>
<h2 id="deployment">Deployment</h2>
<p>You are now ready to deploy your project.</p>
<p>If you have not already done so, save your progress within <code>git</code> and then push the commit(s) to the GitHub repository:</p>
<pre><code class="language-sh">&#35; Add all files&#10;git add -A&#10;&#35; Commit w/ message&#10;git commit -m &quot;working example&quot;&#10;&#35; Push commit(s) to remote&#10;git push -u origin main&#10;</code></pre>
<p>Your work now resides within the GitHub repository, which means that Pages is able to access it too.</p>
<p>If this is your first Cloudflare Pages project, refer to <a href="/pages/get-started/">Get started</a> for a complete setup guide. After selecting the appropriate GitHub repository, you must configure your project with the following build settings:</p>
<ul>
<li><strong>Project name</strong> – Your choice</li>
<li><strong>Production branch</strong> – <code>main</code></li>
<li><strong>Framework preset</strong> – None</li>
<li><strong>Build command</strong> – None / Empty</li>
<li><strong>Build output directory</strong> – <code>public</code></li>
</ul>
<p>After selecting <strong>Save and Deploy</strong>, your Pages project will begin its first deployment. When successful, you will be presented with a unique <code>*.pages.dev</code> subdomain and a link to your live demo.</p>
<p>In this tutorial, you built and deployed a website using Cloudflare Pages and Formspree to handle form submissions. You created a static HTML document with a form that communicates with Formspree to process and store submission requests and send notifications.</p>
<p>If you would like to review the full source code for this application, you can find it on <a href="https://github.com/formspree/formspree-example-cloudflare-html">GitHub</a>.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/pages/tutorials/add-a-react-form-with-formspree/">Add a React form with Formspree</a></li>
<li><a href="/pages/tutorials/forms/">HTML Forms</a></li>
</ul>
