//          Variable :

// Bad
const yyymmmdsas = new Date();
// Good
const currentDate = new Date();

// Bad 
getUserInfo();
getClientData();
getCustomerRecord();
// Good
getUser()

// Bad
setTimeout(blastOff, 86400000);
// Good 
const MILLISECONDS_IN_A_DAY = 24 * 60 * 60;
setTimeout(blastOff, MILLISECONDS_IN_A_DAY);

// Bad
const locations = ['Viet Nam', 'China', 'America']
locations.forEach(l => {
    // what is 'l'
})
// Good 
locations.forEach(location => {
    // ...
})

// Bad
const Car = {
    carMake: 'Honda',
    carColor: 'Red',
    carModel: 'Air Blade'
}
// Good
const Car = {
    make: 'Honda',
    color: 'Red',
    model: 'Air Blade'
}

// Bad 
function createName(name) {
    const name = name || 'Joe';
    // ...
}
// Good
function createName(name = 'Joe') {
    // ...
}

//          Function :

// function arguments should equal or less than 2
// if arguments great than 2, you should combine them into a object
// Bad 
function createMenu(title, body, buttonText, cancelLable) {
    //...
}
createMenu('Foo', 'Bar', 'Foo', True)
// Good
function createMenu({ title, body, buttonText, cancelLable }) {
    //...
}
createMenu({
    title: 'Foo',
    body: 'Bar',
    buttonText: 'Baz',
    cancelLable: true
})

// 1 function should only do 1 job
// Bad
const emailClients = (clients) => {
    clients.forEach(client => {
        let clientRecord = database.lookup(client);
        if (clientRecord.isActive()) {
            email(client)
        }
    })
}
// Good 
const emailClients = (clients) => {
    clients.filter(isClientActive).forEach(email)
}
const isClientActive = (client) => {
    let clientRecord = database.lookup(client)
    return clientRecord.isActive()
}

// function name should tell what it do
// Bad
function addToDate(date, month) {
    //...
}
// Good
function addMonthToDate(date, month) {
    //...
}

// use functional programming instead of impreative programming
const programmerOutput = [
    {
        name: 'A',
        linesOfCode: 500
    },
    {
        name: 'B',
        linesOfCode: 400
    },
    {
        name: 'C',
        linesOfCode: 600
    },
]
// Bad: impreative programming
let totalOutput = 0
for (let i = 0; i < programmerOutput.length; i++) {
    totalOutput += programmerOutput[i].linesOfCode
}
// Good: functional programming
let totalOutput = programmerOutput.map(programmer => programmer.linesOfCode)
    .reduce((acc, linesOfCode) => acc + linesOfCode, 0)


//          Class : SOLID

// S : single responsibility principle
// Bad 
class UserSettings {
    constructor(user) {
        this.user = user
    }

    changeSettings(settings) {
        if (this.verifyCredentials()) {
            //...
        }
    }

    verifyCredentials() {
        //...
    }
}
// Good
class UserAuth {
    constructor(user) {
        this.user = user
    }
    verifyCredentials() {
        //..
    }
}
class UserSettings {
    constructor(user) {
        this.user = user;
        this.auth = new UserAuth(user)
    }
    changeSettings(settings) {
        if (this.auth.verifyCredentials()) {
            //..
        }
    }
}

// O : open/closed principle
// Bad 
class AjaxAdapter extends Adapter {
    constructor() {
        super();
        this.name = 'ajaxAdapter';
    }
}

class NodeAdapter extends Adapter {
    constructor() {
        super();
        this.name = 'nodeAdapter';
    }
}

class HttpRequester {
    constructor(adapter) {
        this.adapter = adapter
    }
    fetch(url) {
        if (this.adapter.name === 'ajaxAdapter') {
            return makeAjaxCall(url).then((res) => {
                //..
            })
        } else if (this.adapter.name === 'nodeAdapter') {
            return makeHttpCall(url).then((res) => {
                //..
            })
        }
    }
    makeAjaxCall(url) {
        //..
    }
    makeHttpCall(url) {
        //..
    }
}
// Good :
class AjaxAdapter extends Adapter {
    constructor() {
        super();
        this.name = 'ajaxAdapter'
    }
    request(url) {
        //..
    }
}
class NodeAdapter extends Adapter {
    constructor() {
        super();
        this.name = 'nodeAdapter'
    }
    request(url) {
        //..
    }
}
class HttpRequester {
    constructor(adapter) {
        this.adapter = adapter;
    }
    fetch(url) {
        return this.adapter.request(url).then((res) => {
            //..
        })
    }
}
// L : liskov substitution principle

// I : interface segregation principle

// D : dependency inversion principle

// User continuous function
// Bad :
class Car {
    constructor() {
        this.make = 'Honda';
        this.model = 'Accord';
        this.color = 'red'
    }
    setMake(make) {
        this.make = make
    }
    setModel(model) {
        this.model = model
    }
    setColor(color) {
        this.color = color
    }
    save() {
        console.log(this.make, this.model, this.color)
    }
}
let car = new Car();
car.setColor('pink')
car.setMake('Ford')
car.setModel('F-159')
car.save()
// Good:
class Car {
    constructor() {
        this.make = 'Honda';
        this.model = 'Accord';
        this.color = 'red'
    }
    setMake(make) {
        this.make = make
        return this
    }
    setColor(color) {
        this.color = color
        return this
    }
    setModel(model) {
        this.model = model
        return this
    }
    save() {
        console.log(this.make, this.model, this.color)
        return this
    }
}
let car = new Car()
car.setColor('pink').setMake('Ford').setModel('F-140').save();

//          asynchronous
// promise is 'cleaner' than callback
// Bad
require('request').get(url, (err, res) => {
    if (err) {
        console.log(err)
    } else {
        //...
    }
})
// Good
require('request').get(url)
    .then(res => {
        //...
    })
    .catch(err => {
        console.log(err)
    })

// async/await is 'cleaner' than promise
// Bad
require('request').get(url)
    .then(res => {
        //...
    })
    .catch(err => {
        console.log(err)
    })
// Good
async function getRes() {
    try {
        let res = await require('request').get(url)
        //...
    } catch (err) {
        console.log(err)
    }
}

//          error handling
// do not just 'console.log(err)', do something else better
// Bad
try {
    //..
} catch (err) {
    console.log(err)
}
// Good 
try {
    //..
} catch (err) {
    console.log(err)
    notifyUserOfError(err);
    reportErrorToService(err);
}

//          format code
// use same principle of name in codebase
// Bad
const DAYS_IN_WEEK = 7
const daysInMonth = 30
const songs = ['song gio', 'a', 'b']
const Artists = ['Jack', 'MTP']
function createMenu() { }
function respon_data() { }
// Good
const DAYS_IN_WEEK = 7
const DATS_IN_MONTH = 30
const songs = ['Song Gio', 'Bac Phan']
const artists = ['Jack', 'MTP']
function createDatabase() { }
function restireDatabase() { }
class Animal { }

