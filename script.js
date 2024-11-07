function changeQuote() {
    const randomQuote = quotes[Math.floor(Math.random() * quotes.length)]
    quote.innerHTML = randomQuote.quote
    author.innerHTML = randomQuote.author
    source.innerHTML = randomQuote.source
}

let quotes = [];
fetch('quotes.json')
    .then(response => response.json())
    .then(data => {
        quotes = data;
        changeQuote()
    })
    .catch(error => {
        console.error('Error fetching the quotes:', error);
    });

let btn = document.querySelector('.btn')
let quote = document.querySelector('.quote')
let author = document.querySelector('.author')
let source = document.querySelector('.source')

btn.addEventListener('click', changeQuote)