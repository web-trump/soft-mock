(this["webpackJsonpsoft-mock-template"]=this["webpackJsonpsoft-mock-template"]||[]).push([[45],{444:function(t,e,n){!function(t){"use strict";t.defineMode("dtd",(function(t){var e,n=t.indentUnit;function r(t,n){return e=n,t}function a(t,e){var n=t.next();if("<"!=n||!t.eat("!")){if("<"==n&&t.eat("?"))return e.tokenize=c("meta","?>"),r("meta",n);if("#"==n&&t.eatWhile(/[\w]/))return r("atom","tag");if("|"==n)return r("keyword","seperator");if(n.match(/[\(\)\[\]\-\.,\+\?>]/))return r(null,n);if(n.match(/[\[\]]/))return r("rule",n);if('"'==n||"'"==n)return e.tokenize=i(n),e.tokenize(t,e);if(t.eatWhile(/[a-zA-Z\?\+\d]/)){var a=t.current();return null!==a.substr(a.length-1,a.length).match(/\?|\+/)&&t.backUp(1),r("tag","tag")}return"%"==n||"*"==n?r("number","number"):(t.eatWhile(/[\w\\\-_%.{,]/),r(null,null))}return t.eatWhile(/[\-]/)?(e.tokenize=u,u(t,e)):t.eatWhile(/[\w]/)?r("keyword","doindent"):void 0}function u(t,e){for(var n,u=0;null!=(n=t.next());){if(u>=2&&">"==n){e.tokenize=a;break}u="-"==n?u+1:0}return r("comment","comment")}function i(t){return function(e,n){for(var u,i=!1;null!=(u=e.next());){if(u==t&&!i){n.tokenize=a;break}i=!i&&"\\"==u}return r("string","tag")}}function c(t,e){return function(n,r){for(;!n.eol();){if(n.match(e)){r.tokenize=a;break}n.next()}return t}}return{startState:function(t){return{tokenize:a,baseIndent:t||0,stack:[]}},token:function(t,n){if(t.eatSpace())return null;var r=n.tokenize(t,n),a=n.stack[n.stack.length-1];return"["==t.current()||"doindent"===e||"["==e?n.stack.push("rule"):"endtag"===e?n.stack[n.stack.length-1]="endtag":"]"==t.current()||"]"==e||">"==e&&"rule"==a?n.stack.pop():"["==e&&n.stack.push("["),r},indent:function(t,r){var a=t.stack.length;return r.match(/\]\s+|\]/)?a-=1:">"===r.substr(r.length-1,r.length)&&("<"===r.substr(0,1)||"doindent"==e&&r.length>1||("doindent"==e?a--:">"==e&&r.length>1||"tag"==e&&">"!==r||("tag"==e&&"rule"==t.stack[t.stack.length-1]?a--:"tag"==e?a++:">"===r&&"rule"==t.stack[t.stack.length-1]&&">"===e?a--:">"===r&&"rule"==t.stack[t.stack.length-1]||("<"!==r.substr(0,1)&&">"===r.substr(0,1)?a-=1:">"===r||(a-=1)))),null!=e&&"]"!=e||a--),t.baseIndent+a*n},electricChars:"]>"}})),t.defineMIME("application/xml-dtd","dtd")}(n(45))}}]);
//# sourceMappingURL=45.130ee4dd.chunk.js.map