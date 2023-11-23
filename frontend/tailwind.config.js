/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./public/index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  theme: {
    extend: {
      fontFamily: {
        corme: "Cormorant Garamond",
        rale: "Raleway",
        roboto: "Roboto",
        monster: "Montserrat",
      },
      colors: {
        "dark-gray": "#31343B",
        "whitesmoke": "#f3f3f3",
        "redGod": "#C52148",
        "blueGod": "#0095da",
      },
    },
  },
  plugins: [],
};
