/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",    // For React apps
    "./pages/**/*.{js,jsx,ts,tsx}",  // For Next.js pages
    "./components/**/*.{js,jsx,ts,tsx}", // For components
    "./app/**/*.{js,jsx,ts,tsx}",    // For Next.js app directory
    "./public/**/*.html",            // For HTML files
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}