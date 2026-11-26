<?php
/**
 * Montessori Erding – Wurzeln
 */

add_action( 'wp_enqueue_scripts', function () {
	wp_enqueue_style( 'montessori-wurzeln-fonts', 'https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600&family=Figtree:wght@400;500;600;700&display=swap', array(), null );
	wp_enqueue_style( 'montessori-wurzeln', get_stylesheet_uri(), array(), wp_get_theme()->get( 'Version' ) );
} );

add_filter( 'body_class', function ( $classes ) {
	$classes[] = 'v1';
	return $classes;
} );

add_action( 'after_setup_theme', function () {
	add_editor_style( array( 'https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600&family=Figtree:wght@400;500;600;700&display=swap', 'style.css' ) );
} );

add_action( 'init', function () {
	register_block_pattern_category( 'montessori', array( 'label' => 'Montessori Erding' ) );
	register_block_style( 'core/button', array( 'name' => 'primary', 'label' => 'Primär' ) );
	register_block_style( 'core/button', array( 'name' => 'secondary', 'label' => 'Sekundär' ) );
} );
