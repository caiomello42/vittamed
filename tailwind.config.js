module.exports = {
  content: [
    './templates/**/*.html',    // Se os templates estão na pasta "templates" dentro da raiz
    './clinica/templates/**/*.html', // Se os templates de cada app estão em "clinica/templates"
    './**/*.py',                // Caso você tenha classes no Python também que estão gerando problemas
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
