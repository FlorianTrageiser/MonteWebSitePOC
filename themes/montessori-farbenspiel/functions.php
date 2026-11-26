<?php
/**
 * Montessori Erding – Farbenspiel
 */

add_action( 'wp_enqueue_scripts', function () {
	wp_enqueue_style( 'montessori-farbenspiel-fonts', 'https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=Nunito+Sans:opsz,wght@6..12,400;6..12,600;6..12,700&display=swap', array(), null );
	wp_enqueue_style( 'montessori-farbenspiel', get_stylesheet_uri(), array(), wp_get_theme()->get( 'Version' ) );
} );

add_filter( 'body_class', function ( $classes ) {
	$classes[] = 'v3';
	return $classes;
} );

add_action( 'after_setup_theme', function () {
	add_editor_style( array( 'https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=Nunito+Sans:opsz,wght@6..12,400;6..12,600;6..12,700&display=swap', 'style.css' ) );
} );

add_action( 'init', function () {
	register_block_pattern_category( 'montessori', array( 'label' => 'Montessori Erding' ) );
	register_block_style( 'core/button', array( 'name' => 'primary', 'label' => 'Primär' ) );
	register_block_style( 'core/button', array( 'name' => 'secondary', 'label' => 'Sekundär' ) );
} );
