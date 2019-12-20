const rp = require('request-promise');
const cheerio = require('cheerio');
const app = express();

app.get('/api/kenpom',(req,res,next) => {
    const options = {
        uri: 'https://kenpom.com/',
        transform:function (body) {
            return cheerio.load(body);
        }
    };

    rp(options)
        .then(($) => {
            const dataArr = []
            $('td').each(function (idx) {
                dataArr.push($(this).text())
            })
            
            res.json(dataArr);
        })
        .catch((err) => {
            console.log(err);
        }); 
})

app.listen(1700, () => console.log('listening'))