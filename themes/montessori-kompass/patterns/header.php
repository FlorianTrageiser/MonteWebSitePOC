<?php
/**
 * Title: Kopfbereich
 * Slug: montessori-kompass/header
 * Categories: header
 * Inserter: yes
 * Block Types: core/template-part/header
 */
?>
<!-- wp:group {"className":"site-header","layout":{"type":"default"},"tagName":"header"} -->
<header class="wp-block-group site-header">
<!-- wp:group {"className":"topbar","layout":{"type":"default"}} -->
<div class="wp-block-group topbar">
<!-- wp:paragraph {"className":"topbar-msg"} -->
<p class="topbar-msg"><span class="pill">Schulaufnahme</span> Anmeldeschluss für die erste Klasse 2027/28: 3. Februar 2027 <a class="more" href="/termine/#aufnahme">Zur Aufnahme</a></p>
<!-- /wp:paragraph -->
<!-- wp:paragraph {"className":"topbar-links"} -->
<p class="topbar-links"><a href="https://www.montemanager.de/login.php">MonteManager</a> · <a href="/kontakt/">Kontakt</a></p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->
<!-- wp:group {"className":"header-inner","layout":{"type":"default"}} -->
<div class="wp-block-group header-inner">
<!-- wp:html -->
<a class="brand" href="/" aria-label="Montessori Erding – Startseite"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/logo-figuren.png' ) ); ?>" alt="" width="54" height="38"/><span class="brand-name">Montessori <span>Erding</span></span></a>
<!-- /wp:html -->
<!-- wp:navigation {"overlayMenu":"mobile","className":"main-nav","layout":{"type":"flex","justifyContent":"right"}} -->
<!-- wp:navigation-link {"label":"Kinderhaus","url":"/kinderhaus/","kind":"custom"} /-->
<!-- wp:navigation-link {"label":"Schule","url":"/schule/","kind":"custom"} /-->
<!-- wp:navigation-link {"label":"Verein","url":"/verein/","kind":"custom"} /-->
<!-- wp:navigation-link {"label":"Termine & Aufnahme","url":"/termine/","kind":"custom"} /-->
<!-- wp:navigation-link {"label":"Kontakt","url":"/kontakt/","kind":"custom"} /-->
<!-- /wp:navigation -->
<!-- wp:buttons {"className":"header-cta"} -->
<div class="wp-block-buttons header-cta">
<!-- wp:button {"className":"is-style-primary"} -->
<div class="wp-block-button is-style-primary"><a class="wp-block-button__link wp-element-button" href="/termine/#aufnahme">Aufnahme</a></div>
<!-- /wp:button -->
</div>
<!-- /wp:buttons -->
</div>
<!-- /wp:group -->
</header>
<!-- /wp:group -->
