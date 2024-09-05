/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./views/pages/*.html",
    "./views/js/*.js"
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
        "45x65": "minmax(45rem, 80rem) auto"
      },
      padding: {
        '8': '8rem',
        '10': '10rem',
        '12': '12rem',
      },
      spacing: {
        '12': '20rem',
      }
    },
  },
  plugins: [],
}

