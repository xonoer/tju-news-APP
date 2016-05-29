//Function.prototype.partial = function () {
//    var fn = this;
//    var args = Array.prototype.slice.call(arguments);
//    return function (){
//        var arg = 0;
//        for(var i = 0; i < args.length && arg < arguments.length;i++){
//            if (args[i] === undefined){
//                args[i] = arguments[arg++];
//            }
//        }
//        return fn.apply(this,args);
//    };
//};
//
//var delay = setTimeout.partial(undefined,1000);
//delay(function(){
//    console.log("hhhhhhhhhhhhhhhhhh");
//})
//
//
//
//Function.prototype.memoized = function(key){
//    this._values = this._values || {};
//    return this._values[key] !== undefined ? this._values[key] : this._values[key] = this.apply(this,arguments);
//};
//
//
//Function.prototype.memoize = function(key){
//    var fn = this;
//    return function (){
//        return fn.memoized.apply(fn,arguments);
//    }
//}
//
//
//var isPrime = (function(num){
//    var prime = num !=1;
//    for (var i = 2; i < num;i++){
//        if(num%i == 0){
//            prime = false;
//            break;
//        }
//    }
//    return prime;
//}).memoize();
//
//console.log(isPrime(5));
//
//
//(function(){
//    console.log("sglkjaildgj");
//})();
//
//
////使用类风格来编写代码
//
////
////
////(function(){
////    var initializing = false;
////    var superPattern = /xyz/.test(function(){
////        xyz;
////    })?/\b_super\b/ : /.*/;
////    Object.subClass = function(properties){
////        var _super = this.prototype;
////        initializing = true;
////        var proto = new this();
////        initializing = false;
////
////        for(var name in properties){
////            proto[name] = typeof properties[name] == "function" &&
////            typeof _super[name] == "function" &&
////            superPattern.test(properties[name])?
////                (function(name,fn){
////                    return function() {
////                        var temp = this._super;
////                        this_super = _super[name];
////                        var ret = fn.apply(this,arguments);
////                        this_super = temp;
////                        return ret;
////                    }
////                })(name,properties[name]):properties[name];
////        }
////        function Class(){
////            if(!initializing && this.init){
////                this.init.apply(this,arguments);
////            }
////
////        }
////        Class.prototype = proto;
////        Class.constructor = Class;
////        Class.subClass = arguments.callee;
////        return Class;
////    };
////
////
////})();
////
////var Person = Object.subClass({
////    init:function(isDancing){
////        this.dancing = isDancing;
////    },
////    dance: function () {
////        return this.dancing;
////    }
////});
////
////var Ninja = Person.subClass({
////    init:function(){
////        this._super(false);
////    },
////    dance:function(){
////        return this._super();
////    },
////    swingSword:function(){
////        return true;
////    }
////});
////
////var person = new Person(true);
////console.log(person.dance());
////
////var ninja = new Ninja();
////console.log(ninja.swingSword());
////console.log(!ninja.dance());
////
////console.log(ninja instanceof Person);
////console.log(person instanceof Person);
////console.log(ninja instanceof Ninja);
//
//function isa(name){
//    return /\d{5}-\d{4}/.test(name);
//}
//
//console.log(isa('88888-5555'));

//
//function qSort(arr){
//    if(arr.length == 0){
//        return [];
//    }
//    var left = [];
//    var right = [];
//    var pivot = arr[0];
//    for(var i = 1;i < arr.length; i++){
//        if(arr[i] < pivot){
//            left.push(arr[i]);
//        }else{
//            right.push(arr[i]);
//        }
//    }
//    return qSort(left).concat(pivot,qSort(right));
//}
//
//var a = [];
//for (var i = 0;i < 10;++i){
//    a[i] = Math.floor(Math.random()*100);
//}
//console.log(a);
//console.log(qSort(a));



//function countNum(str){
//    var count = {};
//    for(var i = 0; i < str.length; i++){
//        if(!count[str[i]]){
//            count[str[i]] = 0
//        }
//        count[str[i]] ++;
//    }
//    console.log(count);
//}
//countNum("aaaabbbccccddfgh");
//
//function sum(){
//    var  s = 0;
//    var arr = Array.prototype.slice.call(arguments);
//    arr.forEach(function(item){
//        s += item;
//    });
//    return s;
//}


//console.log(sum(2,5,78,2));

//function Foo() {
//    getName = function () { console.log(1);};
//    return this;
//}
//Foo.getName = function () { console.log(2);};
//Foo.prototype.getName = function () { console.log(3);};
//var getName = function () { console.log(4);};
//function getName() { console.log(5);}
//
//
////请写出以下输出结果：
//Foo.getName();
//getName();
//Foo().getName();
//getName();
//new Foo.getName();
//new Foo().getName();
//new new Foo().getName();


//var promise = new Promise(function(resolve,reject){
//    if(){
//        resolve(value);
//    }else{
//        reject(error);
//    }
//});
//
//promise.then(function(value){
//    //resloved状态的回调函数
//
//},function (value){
//    //rejected状态的回调函数,可选，不一定需要提供
//});

var getJSON = function(url){
    var promise = new Promise(function(reslove,reject){
        var client = new XMLHttpRequest();
        client.open('GET',url);
        client.onreadystatechange = handler;
        client.responseType = 'json';
        client.setRequestHeader('Accept','application/json');
        client.send();

        function handler(){
            if(this.readyState !== 4){
                return;
            }
            if(this.status === 200){
                reslove(this.response);
            }else{
                reject(new Error(this.statusText));
            }
        }
    });
    return promise;
}

getJSON('/posts.json').then(function(json){
    console.log(json);
},function(error){
    console.log(error);
});//then()可支持链式操作，绑定多个回调函数，并且后一个回调函数依赖前一个回调函数
















