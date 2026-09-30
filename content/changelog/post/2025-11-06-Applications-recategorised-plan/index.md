<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>November 6, 2025</time><h2 id="post-title">Applications to be remapped to the new categories</h2>
<div class="changelog-badges"><span>gateway</span></div><div class="changelog-body"><p>We have previously added new application categories to better reflect their content and improve HTTP traffic management: refer to <a href="/cloudflare-one/changelog/gateway/#2025-10-28">Changelog</a>.
While the new categories are live now, we want to ensure you have ample time to review and adjust any existing rules you have configured against old categories.
The remapping of existing applications into these new categories will be completed by January 30, 2026.
This timeline allows you a dedicated period to:</p>
<ul>
<li>Review the new category structure.</li>
<li>Identify any policies you have that target the older categories.</li>
<li>Adjust your rules to reference the new, more precise categories before the old mappings change.
Once the applications have been fully remapped by January 30, 2026, you might observe some changes in the traffic being mitigated or allowed by your existing policies. We encourage you to use the intervening time to prepare for a smooth transition.</li>
</ul>
<p><strong>Applications being remappedd</strong></p>
<table>
<thead>
<tr>
<th>Application Name</th>
<th>Existing Category</th>
<th>New Category</th>
</tr>
</thead>
<tbody>
<tr>
<td>Google Photos</td>
<td>File Sharing</td>
<td>Photography &amp; Graphic Design</td>
</tr>
<tr>
<td>Flickr</td>
<td>File Sharing</td>
<td>Photography &amp; Graphic Design</td>
</tr>
<tr>
<td>ADP</td>
<td>Human Resources</td>
<td>Business</td>
</tr>
<tr>
<td>Greenhouse</td>
<td>Human Resources</td>
<td>Business</td>
</tr>
<tr>
<td>myCigna</td>
<td>Human Resources</td>
<td>Health &amp; Fitness</td>
</tr>
<tr>
<td>UnitedHealthcare</td>
<td>Human Resources</td>
<td>Health &amp; Fitness</td>
</tr>
<tr>
<td>ZipRecruiter</td>
<td>Human Resources</td>
<td>Business</td>
</tr>
<tr>
<td>Amazon Business</td>
<td>Human Resources</td>
<td>Business</td>
</tr>
<tr>
<td>Jobcenter</td>
<td>Human Resources</td>
<td>Business</td>
</tr>
<tr>
<td>Jobsuche</td>
<td>Human Resources</td>
<td>Business</td>
</tr>
<tr>
<td>Zenjob</td>
<td>Human Resources</td>
<td>Business</td>
</tr>
<tr>
<td>DocuSign</td>
<td>Legal</td>
<td>Business</td>
</tr>
<tr>
<td>Postident</td>
<td>Legal</td>
<td>Business</td>
</tr>
<tr>
<td>Adobe Creative Cloud</td>
<td>Productivity</td>
<td>Photography &amp; Graphic Design</td>
</tr>
<tr>
<td>Airtable</td>
<td>Productivity</td>
<td>Development</td>
</tr>
<tr>
<td>Autodesk Fusion360</td>
<td>Productivity</td>
<td>IT Management</td>
</tr>
<tr>
<td>Coursera</td>
<td>Productivity</td>
<td>Education</td>
</tr>
<tr>
<td>Microsoft Power BI</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>Tableau</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>Duolingo</td>
<td>Productivity</td>
<td>Education</td>
</tr>
<tr>
<td>Adobe Reader</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>AnpiReport</td>
<td>Productivity</td>
<td>Travel</td>
</tr>
<tr>
<td>ビズリーチ</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>doda (デューダ)</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>求人ボックス</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>マイナビ2026</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>Power Apps</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>RECRUIT AGENT</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>シフトボード</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>スタンバイ</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>Doctolib</td>
<td>Productivity</td>
<td>Health &amp; Fitness</td>
</tr>
<tr>
<td>Miro</td>
<td>Productivity</td>
<td>Photography &amp; Graphic Design</td>
</tr>
<tr>
<td>MyFitnessPal</td>
<td>Productivity</td>
<td>Health &amp; Fitness</td>
</tr>
<tr>
<td>Sentry Mobile</td>
<td>Productivity</td>
<td>Travel</td>
</tr>
<tr>
<td>Slido</td>
<td>Productivity</td>
<td>Photography &amp; Graphic Design</td>
</tr>
<tr>
<td>Arista Networks</td>
<td>Productivity</td>
<td>IT Management</td>
</tr>
<tr>
<td>Atlassian</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>CoderPad</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>eAgreements</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>Vmware</td>
<td>Productivity</td>
<td>IT Management</td>
</tr>
<tr>
<td>Vmware Vcenter</td>
<td>Productivity</td>
<td>IT Management</td>
</tr>
<tr>
<td>AWS Skill Builder</td>
<td>Productivity</td>
<td>Education</td>
</tr>
<tr>
<td>Microsoft Office 365 (GCC)</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>Microsoft Exchange Online (GCC)</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>Canva</td>
<td>Sales &amp; Marketing</td>
<td>Photography &amp; Graphic Design</td>
</tr>
<tr>
<td>Instacart</td>
<td>Shopping</td>
<td>Food &amp; Drink</td>
</tr>
<tr>
<td>Wawa</td>
<td>Shopping</td>
<td>Food &amp; Drink</td>
</tr>
<tr>
<td>McDonald's</td>
<td>Shopping</td>
<td>Food &amp; Drink</td>
</tr>
<tr>
<td>Vrbo</td>
<td>Shopping</td>
<td>Travel</td>
</tr>
<tr>
<td>American Airlines</td>
<td>Shopping</td>
<td>Travel</td>
</tr>
<tr>
<td>Booking.com</td>
<td>Shopping</td>
<td>Travel</td>
</tr>
<tr>
<td>Ticketmaster</td>
<td>Shopping</td>
<td>Entertainment &amp; Events</td>
</tr>
<tr>
<td>Airbnb</td>
<td>Shopping</td>
<td>Travel</td>
</tr>
<tr>
<td>DoorDash</td>
<td>Shopping</td>
<td>Food &amp; Drink</td>
</tr>
<tr>
<td>Expedia</td>
<td>Shopping</td>
<td>Travel</td>
</tr>
<tr>
<td>EasyPark</td>
<td>Shopping</td>
<td>Travel</td>
</tr>
<tr>
<td>UEFA Tickets</td>
<td>Shopping</td>
<td>Entertainment &amp; Events</td>
</tr>
<tr>
<td>DHL Express</td>
<td>Shopping</td>
<td>Business</td>
</tr>
<tr>
<td>UPS</td>
<td>Shopping</td>
<td>Business</td>
</tr>
</tbody>
</table>
<p>For more information on creating HTTP policies, refer to <a href="/cloudflare-one/traffic-policies/application-app-types/">Applications and app types</a>.</p>
</div></article></div>
