<p>Cloudflare Realtime billing is based on data sent from Cloudflare edge to your application.</p>
<p>Cloudflare Realtime SFU and TURN services cost $0.05 per GB of data egress.</p>
<p>There is a free tier of 1,000 GB before any charges start. This free tier includes usage from both SFU and TURN services, not two independent free tiers. Cloudflare Realtime billing appears as a single line item on your Cloudflare bill, covering both SFU and TURN.</p>
<p>Traffic between Cloudflare Realtime TURN and Cloudflare Realtime SFU or Cloudflare Stream (WHIP/WHEP) does not get double charged, so if you are using both SFU and TURN at the same time, you will get charged for only one.</p>
<h3 id="turn">TURN</h3>
<p>Please see the <a href="/realtime/turn/faq">TURN FAQ page</a>, where there is additional information on specifically which traffic path from RFC8656 is measured and counts towards billing.</p>
<h3 id="sfu">SFU</h3>
<p>Only traffic originating from Cloudflare towards clients incurs charges. Traffic pushed to Cloudflare incurs no charge even if there is no client pulling same traffic from Cloudflare.</p>
