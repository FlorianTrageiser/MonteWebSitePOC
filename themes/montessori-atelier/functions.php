<?php
/**
 * Montessori Erding – Atelier
 */

add_action( 'wp_enqueue_scripts', function () {
	wp_enqueue_style( 'montessori-atelier-fonts', 'https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Manrope:wght@400;500;600;700&display=swap', array(), null );
	wp_enqueue_style( 'montessori-atelier', get_stylesheet_uri(), array(), wp_get_theme()->get( 'Version' ) );
} );

add_filter( 'body_class', function ( $classes ) {
	$classes[] = 'v4';
	return $classes;
} );

add_action( 'after_setup_theme', function () {
	add_editor_style( array( 'https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Manrope:wght@400;500;600;700&display=swap', 'style.css' ) );
} );

add_action( 'init', function () {
	register_block_pattern_category( 'montessori', array( 'label' => 'Montessori Erding' ) );
	register_block_style( 'core/button', array( 'name' => 'primary', 'label' => 'Primär' ) );
	register_block_style( 'core/button', array( 'name' => 'secondary', 'label' => 'Sekundär' ) );
} );
