<?php
/**
 * Title: Kopfbereich
 * Slug: montessori-wurzeln/header
 * Categories: header
 * Inserter: yes
 * Block Types: core/template-part/header
 */
?>
<!-- wp:group {"className":"site-header","layout":{"type":"default"},"tagName":"header"} -->
<header class="wp-block-group site-header">
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
