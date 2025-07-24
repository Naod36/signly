/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "../templates/**/*.html", // Include all Django templates
    "../theme/templates/theme/**/*.html",
    "./src/**/*.{js,jsx,ts,tsx}", // If using JS/TS
  ],
  theme: {
    extend: {},
  },
  // plugins: [require("daisyui")],
  // daisyui: {
  //   themes: ["light", "dark"], // or customize later
  // },
  safelist: [
    "bg-blue-500",
    "hover:bg-primary-focus",
    "text-white",
    "rounded",
    "cursor-pointer",
    "transition",
    "text-lg",
    "text-gray-700",
    "border",
    "border-dashed",
    "rounded-lg",
    "p-10",
    "text-center",
    "shadow",
    "mt-4",
    "btn",
    "btn-primary",
    "px-6",
    "py-2",
    "hover:underline",
  ],
};
