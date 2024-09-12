
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./views/pages/*.html",
    "./views/js/*.js",
    "./musify/templates/*.html"
  ],
  theme: {
    extend: {
      colors: {
        "maroon": "#292626",
        "pr-green": {
            800: "#0FAF3C"
          },
        "pr-gray": {
          200: "#B1B1B1"
        },
        "pr-black":
        {
          600: "#121212"
        }
      },
      borderRadius: {
        '4xl': '2rem',
      },
      fontFamily: {
        "raleway": ["Raleway", "sans-serif"]
      },
      gridTemplateColumns:
      {
        '2x': "16rem 1fr",
        "45x65": "auto 24rem",
      },
      padding: {
        '1r': "1rem",
        '2r': "2rem",
        '4r': "4rem",
        '8': '8rem',
        '10': '10rem',
        '12': '12rem',
      },
      margin: {
        '2r': '2rem',
        '4r': '4rem',
        '8r': '8rem',
        '10r': '10rem',
        '12r': '12rem',
      },
      spacing: {
        '20': '20rem',
        '24': '24rem',
        '32': '32rem',
      }
    },
  },
  plugins: [],
}

