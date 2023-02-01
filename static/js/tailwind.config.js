module.exports = {
    content: [
      './js/static/templates/content/.{html,js}',
      './components/**/*.{html,js}',
    ],
    plugins: [
        // ...
        require('@tailwindcss/aspect-ratio'),
      ],
  }

 