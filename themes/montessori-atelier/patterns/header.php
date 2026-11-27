<?php
/**
 * Title: Kopfbereich
 * Slug: montessori-atelier/header
 * Categories: header
 * Inserter: yes
 * Block Types: core/template-part/header
 */
?>
<!-- wp:group {"className":"site-header side","layout":{"type":"default"},"tagName":"header"} -->
<header class="wp-block-group site-header side">
<!-- wp:group {"className":"side-top","layout":{"type":"default"}} -->
<div class="wp-block-group side-top">
<!-- wp:html -->
<a class="brand" href="/" aria-label="Montessori Erding – Startseite"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/logo-figuren.png' ) ); ?>" alt="" width="54" height="38"/><span class="brand-name">Montessori<br/><span>Erding</span></span></a>
<!-- /wp:html -->
<!-- wp:navigation {"overlayMenu":"mobile","className":"main-nav","layout":{"type":"flex","justifyContent":"right"}} -->
<!-- wp:navigation-link {"label":"Kinderhaus","url":"/kinderhaus/","kind":"custom"} /-->
<!-- wp:navigation-link {"label":"Schule","url":"/schule/","kind":"custom"} /-->
<!-- wp:navigation-link {"label":"Verein","url":"/verein/","kind":"custom"} /-->
<!-- wp:navigation-link {"label":"Termine & Aufnahme","url":"/termine/","kind":"custom"} /-->
<!-- wp:navigation-link {"label":"Kontakt","url":"/kontakt/","kind":"custom"} /-->
<!-- /wp:navigation -->
</div>
<!-- /wp:group -->
<!-- wp:group {"className":"side-bottom","layout":{"type":"default"}} -->
<div class="wp-block-group side-bottom">
<!-- wp:buttons {"className":"header-cta"} -->
<div class="wp-block-buttons header-cta">
<!-- wp:button {"className":"is-style-primary"} -->
<div class="wp-block-button is-style-primary"><a class="wp-block-button__link wp-element-button" href="/termine/#aufnahme">Aufnahme 2027/28</a></div>
<!-- /wp:button -->
</div>
<!-- /wp:buttons -->
<!-- wp:paragraph {"className":"side-job"} -->
<p class="side-job"><a href="https://montessori-erding.de/jobs/"><strong>Wir suchen</strong> eine Lehrkraft (m/w/d) für die Grundschule</a></p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"className":"side-meta"} -->
<p class="side-meta">Kinderhaus Erding<br/>Schule Aufkirchen</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->
</header>
<!-- /wp:group -->
