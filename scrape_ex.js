var rp = require('request-promise');
var cheerio = require('cheerio');

//

// rp('https://dgps.gujarat.gov.in/webcontroller/page/government-resolutions')
rp('https://news.ycombinator.com/')
    .then((html) => {
    let $ = cheerio.load(html);
    console.log(html);
    $('a').each(function(i, element){
        var b = $(this).prev();
        console.log(b.text());
        });
    })
    .catch(console.error.bind(console));
    