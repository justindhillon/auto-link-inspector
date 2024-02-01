import cheerio from 'cheerio';
import fetch from 'node-fetch';

const data = await fetch('https://github.com/trending');
const $ = cheerio.load(await data.text());

console.log($('a').find('a'));
