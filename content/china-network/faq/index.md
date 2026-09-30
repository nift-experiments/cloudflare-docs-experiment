<h2 id="prerequisites-and-onboarding">Prerequisites and onboarding</h2>
<h3 id="what-are-the-requirements-to-enable-cloudflare-china-network-service-from-cloudflare">What are the requirements to enable Cloudflare China Network service from Cloudflare?</h3>
<p>Refer to <a href="/china-network/get-started/">Get started</a> for more information.</p>
<h3 id="can-i-use-my-current-account-to-access-cloudflare-china-network-service">Can I use my current account to access Cloudflare China Network service?</h3>
<p>Yes, you can use your current Cloudflare account and dashboard.</p>
<h3 id="what-are-the-requirements-for-requesting-a-cloudflare-china-network-poc">What are the requirements for requesting a Cloudflare China Network PoC?</h3>
<p>Cloudflare requires that you have a valid <a href="/china-network/concepts/icp/">ICP (Internet Content Provider)</a> number and content vetting approval from JD Cloud to provide you with a Cloudflare China Network PoC (Proof of Concept). If you are interested in a PoC, please contact your sales team.</p>
<h2 id="data-storage">Data storage</h2>
<h3 id="will-my-cloudflare-account-or-configuration-information-be-stored-in-china">Will my Cloudflare account or configuration information be stored in China?</h3>
<p>Cloudflare has taken numerous steps to ensure your security and the integrity of your data in China. Your identification information such as email addresses, password hashes, and billing information are never stored on Cloudflare China Network or shared with the Cloudflare partner except for Zone configuration information and bindings with Cloudflare’s Developer Suite which are stored on the China Network operated by our partners in China upon your enabling the China Service for a particular Zone.</p>
<h2 id="compliance">Compliance</h2>
<h3 id="does-cloudflare-have-an-miit-license-to-provide-cdn-services-in-china">Does Cloudflare have an MIIT license to provide CDN services in China?</h3>
<p>As a US company, Cloudflare does not have a license from China's Ministry of Industry and Information Technology (MIIT). However, Cloudflare's partner JD Cloud has all the licenses required by the MIIT to operate and provide CDN services in China.</p>
<h3 id="can-cloudflare-or-jd-cloud-help-me-to-get-the-icp">Can Cloudflare or JD Cloud help me to get the ICP?</h3>
<p>No, neither Cloudflare nor JD Cloud is responsible for <a href="/china-network/concepts/icp/">ICP (Internet Content Provider)</a> applications. However, Cloudflare can help provide referrals to ICP partners specialized in ICP applications. For more information, refer to <a href="/china-network/concepts/icp/#obtain-an-icp-number">Obtain an ICP number</a>.</p>
<h3 id="why-is-my-icp-filing-license-revoked">Why is my ICP filing/license revoked?</h3>
<p>The application and revocation of ICP filings or licenses is managed by China's local authorities. Usually, either the customer or the agency processing the ICP application will receive a notification with more details. Cloudflare cannot provide the ICP revocation reasons.</p>
<h3 id="what-would-happen-if-my-icp-filing-license-got-revoked">What would happen if my ICP filing/license got revoked?</h3>
<p>Cloudflare's partner JD Cloud and the local authorities continuously track the status of the ICP. If your ICP gets revoked, JD Cloud may terminate or suspend your access to the China Service at any time and without liability, in accordance with China local regulations.
To mitigate the impact on your Internet properties, Cloudflare will reroute the traffic for the affected domains to the nearest data centers outside of China.</p>
<h3 id="what-is-content-vetting-and-why-do-i-need-jd-cloud-to-vet-my-domain-s-content-before-onboarding">What is content vetting and why do I need JD Cloud to vet my domain's content before onboarding?</h3>
<p>The JD Cloud network is proxying content inside of China for customers who have purchased Cloudflare China Network. To ensure compliance with China’s Internet regulations and with <a href="https://docs.jdcloud.com/cn/product-service-agreement/starshield-terms-of-service">JD Cloud's service terms</a>, JD Cloud must review the content of all the domains before onboarding those domains to their network. They can approve or reject any domain based on the nature of its content. For more information, contact your sales team.</p>
<h2 id="products-and-features">Products and features</h2>
<h3 id="how-does-ipv6-work-on-china-network">How does IPv6 work on China Network?</h3>
<p>All sites hosted in Mainland China must have IPv6 enabled. China Network automatically enables IPv6 for domains to fulfill this requirement and it is not possible to disable it. According to internal testing, IPv6 connections in Mainland China are more reliable and offer better latency.</p>
<h3 id="is-turnstile-available-in-mainland-china">Is Turnstile available in Mainland China?</h3>
<p><a href="/turnstile/">Turnstile</a> is not supported in Mainland China. Therefore, both China Network zones and <a href="/fundamentals/concepts/accounts-and-zones/#zones">global zones</a> with users visiting your content from Mainland China may experience issues with Turnstile.</p>
<h3 id="is-pages-available-in-mainland-china">Is Pages available in Mainland China?</h3>
<p><a href="/pages/">Pages</a> is not available in Mainland China due to pages.dev certificate not residing within Mainland China. However, Pages from a global zone may potentially be extended into Mainland China.</p>
