// render a variable as html in react (like .html() in jQuery) 
<div id="preview" dangerouslySetInnerHTML={{ __html: variable }}></div>

//  marked allows line break in js 
marked.setOptions({
    breaks: true
});

//  even listener in js
document.addEventListener(event, function () { }, optional(useCapture));
document.addEventListener("keydown", this.handleKeyPress);

//  settimeout function in js 
setTimeOut(function () { }, time);

//  clear all interval when dont has variable in js
for (var i = 1; i < 99999; i++) { window.clearInterval(i); }

//  play pause audio in js 
document.getElementById('audio').play();
document.getElementById('audio').pause();
//  add after pause to reset audio 
document.getElementById('audio').currentTime = 0;

//  twiter tweet
http://twitter.com/intent/tweet?text=

//  add event on d3 shape
on('event name', function (envent, d) {

})
eventname: mouseover, mouseout, click

/* redirect url in experssjs */
res.redirect('/')

/* evaluates or executes an argument. */
eval(string)

/* get url */
var pathname = window.location.pathname; // Returns path only (/path/example.html)
var url = window.location.href;     // Returns full URL (https://example.com/path/example.html)
var origin = window.location.origin;   // Returns base URL (https://example.com)

// bcrypt async:
bcrypt.hash(string, 12, (err, hash) => {
    //exam hash: $2b$12$/51RX2Jpp11h.J9CQXUhEuMxHQTipXUyZUTi1eAGclY5KNLCzD6gy
})
bcrypt.compare(string, hash, (err, res) => {
    //res is True of False
})
// bcrypt sync:
hash = bcrypt.hashSync(string, 12); //exam hash: $2b$12$/51RX2Jpp11h.J9CQXUhEuMxHQTipXUyZUTi1eAGclY5KNLCzD6gy
res = bcrypt.compareSync(string, hash); //res is True of False